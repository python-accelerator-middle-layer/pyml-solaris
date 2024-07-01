# import datetime
from tango import AttributeProxy

from ..util.get_device_index import get_device_index
from accelerator_data import AcceleratorData


def set_var(family, device_list, values):
    """
    Sets a variable in an online system or model

    Parameters
    ----------
    family: object
    device_list: list or int or str
    values: float or int or bool or list of former

    See also
    --------
    get_var

    Notes
    -----
    local functions: set_model, set_online
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann
    Written by Mikolaj Wrobel
    May 2024
    """

    # Starting time
    # t0 = datetime.datetime.now    # not used for now

    # Force list for values
    if type(values) is not list:
        values = [values]

    # Parse input device list
    indexes = get_device_index(family, device_list)

    # check for 'Setpoint' or 'Monitor' object
    if hasattr(family, "Monitor"):
        tango_family = getattr(family, "Monitor")
    elif hasattr(family, "Setpoint"):
        tango_family = getattr(family, "Setpoint")
    else:
        print("No 'Monitor' or 'Setpoint' object, data cannot be acquired.")
        return

    # Check mode and write data
    if getattr(tango_family, "mode") in ['Model', 'Simulator']:
        set_model(tango_family, indexes, values)
    else:
        set_online(tango_family, indexes, values)


def set_model(family, indexes, values):  # TODO
    pass


def set_online(family, indexes, values):

    # read machine name
    machine = AcceleratorData.machine_address

    # read tango names, force list use, clear whitespaces, add missing machine address
    tango_names = getattr(family, "tango_names")
    tango_names = [tango_names] if isinstance(tango_names, str) else list(tango_names)
    tango_names = [name.replace(' ','') for name in tango_names]
    tango_names = [machine + name for name in tango_names]

    i = 0
    for idx in indexes:
        AttributeProxy(tango_names[idx]).write(values[i])
        i += 1
