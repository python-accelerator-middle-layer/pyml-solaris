def parse_list(device_string):
    """
    Creates a device list out of parser input string.

    Parameters
    ----------
    device_string: str


    Returns
    -------
    device_list
        list of str, int or tuples. The list is not checked for correctness

    Written by Mikolaj Wrobel
    May 2024
    """

    # check for input
    if not device_string:
        return

    # remove whitespaces and divide into list
    device_string = device_string.replace(' ', '')
    str_list = device_string.split(',')

    device_list = []
    for i in range(len(str_list)):
        try:
            # try to convert to integer
            device_list.append(int(str_list[i]))
        except ValueError:
            # check for device list format: (1,1), (1,2) etc.
            if str_list[i].startswith('(') and str_list[i+1].endswith(')'):
                device_list.append(eval(str_list[i] + ',' + str_list[i + 1]))
            elif str_list[i].endswith(')'):
                pass
            else:
                # keep it as string
                device_list.append(str_list[i])

    return device_list
