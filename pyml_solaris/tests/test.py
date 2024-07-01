"""
TESTING SCRIPT
"""
import argparse

from ..util.parse_list import parse_list


def printer(**flags):
    print(flags)


def optional_args(*opts):
    return opts


# -------------------------------------------------------------------------------------------------------------------
# Argument parser
parser = argparse.ArgumentParser(
    prog='printer',
    description='test parser behaviour')

parser.add_argument('--delta_rf',
                    help='Change in RF frequency in Hz (Default: 0.2% energy change)')
parser.add_argument('--bpm_x_list',
                    help='List of xBPMs that are performing the measurement (Default: all BPMs)')
parser.add_argument('--wait',
                    help='Wait time between measurements in seconds (Default: 5)')
parser.add_argument('--no_display', action='store_true',
                    help='Do not draw plots from measured data (Default: Draw)')
parser.add_argument('--archive', action='store_true',
                    help='Save measured data in archive object (Default: Only draw)')

# Parse arguments
args = parser.parse_args(['--bpm_x_list', '14, 33, (1, 2), (3, 3), 06BPMx02'])
args = vars(args)

args["bpm_x_list"] = parse_list(args["bpm_x_list"])

# execute function
printer(**args)
