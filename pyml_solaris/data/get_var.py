import time
from tango import AttributeProxy
from warnings import warn

from ..util.get_device_index import get_device_index
from accelerator_data import AcceleratorData


def get_var(family, device_list):
    """
    Returns a variable from an online system or model

    Parameters
    ----------
    family: object
    device_list: list or int or str

    Returns
    -------
    var
        Variable of passed family, can be a list or a float

    See also
    --------
    set_var

    Notes
    -----
    Local functions: get_model, get_online
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    May 2024
    """

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

    # read machine address
    machine = AcceleratorData.machine_address

    # read tango names, force list use, clear whitespaces, add missing machine address
    tango_names = getattr(tango_family, "tango_names")
    tango_names = [tango_names] if isinstance(tango_names, str) else list(tango_names)
    tango_names = [machine + name.replace(' ', '') for name in tango_names]

    # Read data
    var = get_online(tango_names, indexes)

    return var

# TODO: get_model()


def get_online(tango_names, indexes):
    # read data from online system
    var = []
    for idx in indexes:
        var.append(AttributeProxy(tango_names[idx]).read().value)

    # format into float if there's only one variable
    var = var[0] if len(var) == 1 else var

    return var
