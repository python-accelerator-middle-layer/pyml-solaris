import time

import numpy as np

from ..data.get_var import get_var
from ..data.set_var import set_var
from ..util.get_device_index import get_device_index

from ..data.output_struct import OutputStruct


def measure_response_matrix(
        monitor_objects, monitor_list, actuator_object, actuator_list, actuator_delta, unipolar_flag, wait, archive
):
    """
    Measures a response matrix on one actuator family using one or more monitor families

    Parameters
    ----------
    monitor_objects: object or list of objects
    monitor_list: list or int or str
    actuator_object: object
    actuator_list: list or int or str
    actuator_delta: float
    unipolar_flag: bool or none
        If true, sets modulation method to unipolar, which changes the actuator from default value to delta.
        Default modulation method is bipolar (by +/- delta/2)
    wait: float
        Wait time before measurement in seconds (Default: 0)
    archive: bool or none
        If true, function returns an OutputStruct object

    Returns
    -------
    resp_mat
        Response matrix for given actuators

    See also
    --------
    measure_dispersion, measure_bpm_response

    Notes
    -----
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    May 2024
    """

    # Force list use on monitors to avoid type conflicts
    if not isinstance(monitor_objects, list):
        monitor_objects = [monitor_objects]
        monitor_list = [monitor_list]

    # Check for actuator delta
    if not actuator_delta:
        print('Delta cannot be zero. Aborting...\n')
        return

    # Get initial actuator value
    actuator_init = get_var(actuator_object, actuator_list)

    # Check for 'Setpoint' object
    if hasattr(actuator_object, "Setpoint"):
        actuator_setpoint = getattr(actuator_object, "Setpoint")
    else:
        print("No 'Setpoint' object found, actuator data cannot be acquired. Aborting...\n")
        return

    # Get actuator units (forced hardware, might be a subject for change)
    actuator_unit = getattr(actuator_setpoint, "hw_units")

    # Get actuator ranges (only of passed devices)
    actuator_range = getattr(actuator_setpoint, "range")
    device_indexes = get_device_index(actuator_object, actuator_list)
    actuator_range = actuator_range if all(isinstance(r, list) for r in actuator_range) else [actuator_range]
    delta_tol = [actuator_range[idx] for idx in device_indexes]

    # Reformat into numpy array and subtract initial value to get tolerances
    delta_tol = np.array(delta_tol)
    if isinstance(actuator_init, list):
        delta_tol -= np.array(actuator_init)[:, np.newaxis]
    else:
        delta_tol -= actuator_init

    # Check if actuator delta exceeds any tolerances
    limits = [
        unipolar_flag and (any(delta_tol[:, 0] > actuator_delta) or any(actuator_delta > delta_tol[:, 1])),
        not unipolar_flag and (any(actuator_delta > delta_tol[:, 1] * 2) or any(actuator_delta < delta_tol[:, 0] * 2))
    ]

    if any(limits):
        print('Delta too large, actuator limits exceeded. Aborting...\n')
        return

    # Initialize measurement
    print("Measuring response of {} family using ".format(actuator_object.__name__), end='')
    if unipolar_flag:
        print("unipolar actuator method\n")
    else:
        print("bipolar actuator method\n")

    # Get actuator list if none was passed, force list use
    if not actuator_list:
        actuator_list = getattr(actuator_object, "element_list")
        actuator_list = [actuator_list] if isinstance(actuator_list, int) else list(actuator_list)

    # Force list use for actuator loop
    actuator_delta = actuator_delta if isinstance(actuator_delta, list) else [actuator_delta,] * len(actuator_list)
    actuator_init = actuator_init if isinstance(actuator_init, list) else [actuator_init] * len(actuator_list)
    resp_mat = []

    # Loop over actuator devices
    for actuator, init, delta in zip(actuator_list, actuator_init, actuator_delta):

        # Step down
        if not unipolar_flag:
            delta = abs(delta)
            print("Changing actuator by -{} {} from nominal value".format(delta/2, actuator_unit))
            set_var(actuator_object, actuator, init - delta/2)

        if wait:
            print(f"waiting {wait} seconds...")
            time.sleep(wait)

        positions_down = [get_var(family, monitors) for family, monitors in zip(monitor_objects, monitor_list)]

        # Step up (or down, if unipolar delta is negative)
        if unipolar_flag:
            print("Changing actuator by {} {} from nominal value".format(delta, actuator_unit))
            set_var(actuator_object, actuator, init + delta)
        else:
            print("Changing actuator by +{} {} from nominal value".format(delta/2, actuator_unit))
            set_var(actuator_object, actuator, init + delta/2)

        if wait:
            print(f"waiting {wait} seconds...")
            time.sleep(wait)

        positions_up = [get_var(family, monitors) for family, monitors in zip(monitor_objects, monitor_list)]

        # Restore actuators
        print("Resetting actuator to nominal value")
        set_var(actuator_object, actuator, init)

        if wait:
            print(f"waiting {wait} seconds...")
            time.sleep(wait)

        # Compute differences
        positions_up = np.array(positions_up)
        positions_down = np.array(positions_down)
        r = (positions_up - positions_down) / delta
        resp_mat.append(r)

    # End of actuator loop
    resp_mat = resp_mat[0] if len(resp_mat) == 1 else resp_mat

    if archive:
        resp_mat = OutputStruct(resp_mat)

    return resp_mat
