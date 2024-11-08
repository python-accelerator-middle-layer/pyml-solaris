import numpy as np

from typing import Union, Iterable, Optional, Sequence, List
from time import sleep

from ..data.globals import Family
from ..data.context import AcceleratorObjects


def measure_response_matrix(
        monitor_names: Union[str, Iterable[str]],
        actuator_names: Union[str, Iterable[str]],
        actuator_deltas: Union[float, Sequence[float]],
        wait: Optional[float] = 0., unipolar: Optional[bool] = False
) -> List:
    """
    Measures a response matrix of given actuators using given monitors

    Parameters
    ----------
    monitor_names: str or iterable of str
        names of monitor families
    actuator_names: str or iterable of str
        names of actuator families
    actuator_deltas: float or iterable of float
    wait: optional, float
        Wait time before measurement in seconds (Default: 0)
    unipolar: optional, bool
        If true, sets modulation method to unipolar, which changes the actuator
        from default value to delta.
        Default modulation method is bipolar (by +/- delta/2)

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
    2nd version
    October 2024
    """

    # Get monitor and actuator families from AcceleratorObjects
    if isinstance(monitor_names, str):
        monitors = (getattr(AcceleratorObjects, monitor_names),)
    else:
        monitors = tuple(getattr(AcceleratorObjects, name) for name in monitor_names)

    if isinstance(actuator_names, str):
        actuators = (getattr(AcceleratorObjects, actuator_names),)
    else:
        actuators = tuple(getattr(AcceleratorObjects, name) for name in actuator_names)

    # Verify actuator delta
    if not actuator_deltas:
        raise ValueError("Actuator delta cannot be 0.")

    try:
        # Check if input is iterable
        iter(actuator_deltas)

        # Verify length
        if len(actuator_deltas) != len(actuators):
            raise ValueError(f"Expected a sequence of length {len(actuators)}, "
                             f"but got a sequence of length {len(actuator_deltas)}.")

    except TypeError:  # This suggests only a float was given
        actuator_deltas = (actuator_deltas,)

    # Measure response of each actuator
    response_matrix = []
    for actuator, delta in zip(actuators, actuator_deltas):
        response_matrix += _measure_actuator_response(
                               monitors, actuator, delta, wait, unipolar
                           )

    return response_matrix


def _measure_actuator_response(
        monitors: Sequence[Family], actuator: Family, delta: float,
        wait: float, unipolar: bool
) -> List[np.ndarray]:
    """Helper function performing scan on one actuator family"""

    # Get initial actuator positions
    for device in actuator:
        device.initial_position = device.monitor()
    units = actuator.hw_units

    # Note: range checking is unnecessary, as it's built into setpoint method

    # Initialize measurement
    print(f"Measuring response of {actuator.family_name} Family using ", end='')
    if unipolar:
        print("unipolar actuator method")
    else:
        print("bipolar actuator method")

    response = []
    for device in actuator:
        # Step down
        if not unipolar:
            delta = abs(delta)
            print(f"Changing actuator by -{delta / 2} {units} from nominal value")
            device.setpoint(device.initial_position - delta / 2)

        if wait:
            print(f"waiting {wait} seconds...")
            sleep(wait)

        positions_down = np.array([mon.monitor() for mon in monitors])

        # Step up (or down, if unipolar delta is negative)
        if unipolar:
            print(f"Changing actuator by {delta} {units} from nominal value")
            device.setpoint(device.initial_position + delta)
        else:
            print(f"Changing actuator by +{delta / 2} {units} from nominal value")
            device.setpoint(device.initial_position + delta / 2)

        if wait:
            print(f"waiting {wait} seconds...")
            sleep(wait)

        positions_up = np.array([mon.monitor() for mon in monitors])

        # Restore actuators
        print("Resetting actuator to nominal value")
        device.setpoint(device.initial_position)

        if wait:
            print(f"waiting {wait} seconds...")
            sleep(wait)

        # Compute differences and add to list
        r = (positions_up - positions_down) / delta
        response.append(r)

    # End of actuator loop

    # Reformat response list
    stacked_response = np.stack(response)
    response = [stacked_response[:, i, :] for i in range(len(monitors))]

    # Build output DataFrame
    # ActuatorResponse = namedtuple(
    #     "ActuatorResponse", ["actuator", "monitor", "response"]
    # )
    #
    # actuator_response = [
    #     ActuatorResponse(actuator.family_name, monitor.family_name, resp)
    #     for monitor, resp in zip(monitors, response)
    # ]

    return response
