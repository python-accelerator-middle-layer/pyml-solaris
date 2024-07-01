from warnings import warn


def get_device_index(family, device_list):
    """
        Returns a list of indexes of devices, based on passed device list

        Parameters
        ----------
        family: object
        device_list: list of tuples or ints or strings
            Recognised identifiers: device number, device id, device name, device common name. Passing an empty list
            returns full list of identifiers

        Returns
        -------
        indexes
            list of indexes of devices, based on passed device list. Indexes start from 0

        Adapted from MATLAB code by Gregory J. Portmann and Laurent S. Nadolski
        Written by Mikolaj Wrobel
        May 2024
        """

    # Check for list
    if not device_list:
        indexes = getattr(family, "element_list")
        indexes = [0] if isinstance(indexes, int) else [i - 1 for i in indexes]
        return indexes

    # Force list
    device_list = [device_list] if not isinstance(device_list, list) else device_list

    # Read lists of possible device identifiers
    int_list = getattr(family, "element_list")
    id_list = getattr(family, "device_list")
    common_list = getattr(family, "common_names")
    name_list = getattr(family, "device_name")

    # Force list use
    int_list = [int_list] if isinstance(int_list, int) else list(int_list)
    id_list = [id_list] if not all(isinstance(i, tuple) for i in id_list) else list(id_list)
    common_list = [common_list] if isinstance(common_list, str) else list(common_list)
    name_list = [name_list] if isinstance(name_list, str) else list(name_list)

    indexes = []

    # Check element index
    for dev in device_list:
        if dev in int_list:
            indexes.append(int_list.index(dev))
        elif dev in id_list:
            indexes.append(id_list.index(dev))
        elif dev in common_list:
            indexes.append(common_list.index(dev))
        elif dev in name_list:
            indexes.append(name_list.index(dev))
        else:
            warn("'{}' is not a correct identifier.".format(dev))

    if not indexes:
        warn("No correct identifier has been passed. Reading full device list")
        indexes = [i - 1 for i in int_list]

    return indexes
