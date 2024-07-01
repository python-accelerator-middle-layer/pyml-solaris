from warnings import warn

from get_device_index import get_device_index


def get_active_device_list(family, device_list):
    """
    Returns a list of devices with status = 1, based on passed device list.

    Parameters
    ----------
    family: object
    device_list: list of tuples or ints or strings
        Recognised identifiers: device number, device id, device name, device common name. Passing an empty list
        is interpreted as full device list

    Returns
    -------
    active_device_list
        list of indexes of devices, based on passed device list. List is in the format of AO device list
        [(1,1),(1,2),(1,3) etc.]

    Adapted from MATLAB code by Gregory J. Portmann and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    May 2024
    """

    # Get indexes of active devices, indexes of passed devices, and full device list
    active_device_indexes = [idx for idx, status in enumerate(getattr(family, "status")) if status == 1]
    device_indexes = get_device_index(family, device_list)
    full_device_list = getattr(family, "device_list")

    # Verify if passed devices are active
    active_device_list = []

    for idx in device_indexes:
        active_device = full_device_list[idx]

        if idx in active_device_indexes:
            active_device_list.append(active_device)
        elif len(device_indexes) != len(full_device_list):
            warn("{} is inactive".format(active_device))

    return active_device_list
