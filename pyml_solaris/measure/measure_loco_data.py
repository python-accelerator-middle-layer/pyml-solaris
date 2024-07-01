import argparse
from time import time
from datetime import datetime
from shutil import copy
from os import makedirs

from measure_dispersion import measure_dispersion
from measure_bpm_response import measure_bpm_response
from monitor_bpm import monitor_bpm

from ..data.accelerator_data import AcceleratorData


def measure_loco_data(**flags):
    """
    Measures the set of LOCO data

    Parameters
    ----------
    **flags: dict, optional
        By default passed from argument parser, but can be called on its own. Available keywords:
        dir: str
            Directory name where LOCO data files will be saved
        no_display: bool
            Do not draw plots from measured data (Default: Draw)

    See also
    --------
    measure_dispersion, measure_bpm_response, monitor_bpm

    Notes
    -----
    Inputs are passed from script via argument parser, all are optional
    WARNING: Function has not yet been tested online TODO
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann
    Written by Mikolaj Wrobel
    May 2024
    """

    # Set or create target directory
    if flags.get('dir'):
        loco_path = flags.get('dir')
    else:
        loco_path = (AcceleratorData.Directory.LOCO_data + '/' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
        makedirs(loco_path)

    print("Chosen LOCO directory: {}".format(loco_path))

    print("Before measurement, make sure the orbit is OK.")
    qui = input("Start the LOCO measurement? (y/n): ")
    if qui != 'y':
        print("LOCO measurement aborted.\n")
        return

    start_time = time()
    # TODO?: save current machine settings (when dynamic AO object is introduced)

    # Measure dispersion
    print("Measuring dispersion...\n")
    dispersion_file = measure_dispersion(archive=True, no_display=flags.get('no_display'))

    # Measure BPM response
    print("Measuring BPM response...\n")
    bpm_response_file = measure_bpm_response(archive=True, no_display=flags.get('no_display'))

    # Measure BPM sigma
    print("Measuring BPM sigma...\n")
    bpm_sigma_file = monitor_bpm(archive=True, no_display=flags.get('no_display'))

    # Copy files to chosen directory
    copy(dispersion_file, loco_path)
    copy(bpm_response_file, loco_path)
    copy(bpm_sigma_file, loco_path)

    meas_time = (time()-start_time)/60
    print("LOCO measurement complete. Total measurement time was {} minutes\n".format(meas_time))


# -------------------------------------------------------------------------------------------------------------------
# Argument parser
parser = argparse.ArgumentParser(
    prog='measure_loco_data',
    description='Measures the set of LOCO data')

parser.add_argument('--dir',
                    help='Directory name where LOCO data files will be saved')
parser.add_argument('--no_display', action='store_true',
                    help='Do not draw plots from measured data (Default: Draw)')

# Parse arguments
args = parser.parse_args()
args = vars(args)

# execute function
measure_loco_data(**args)
