import argparse
from datetime import datetime
import json

import numpy as np

from ..data.accelerator_objects import AcceleratorObjects
from ..data.accelerator_data import AcceleratorData

from ..util.get_device_index import get_device_index
from ..util.get_active_device_list import get_active_device_list
from measure_response_matrix import measure_response_matrix
from ..util.parse_list import parse_list


def measure_bpm_response(**flags):
    """
    Measures the BPM response matrix in the horizontal and vertical planes, based on online data.

    Parameters
    ----------
    **flags: dict, optional
        By default passed from argument parser, but can be called on its own. Available keywords:
            hcm_kick: float
                Change in HCM correctors (Default: read from HCOR response matrix)
            vcm_kick: float
                Change in VCM correctors (Default: read from VCOR response matrix)
            hcm_list: list or int or str
                List of HCM correctors used in the measurement (Default: all HCMs)
            vcm_list: list or int or str
                List of VCM correctors used in the measurement (Default: all VCMs)
            bpm_x_list: list or int or str
                List of xBPMs that are performing the measurement (Default: all BPMs)
            bpm_y_list: list or int or str
                List of yBPMs that are performing the measurement (Default: all BPMs)
            wait: float
                Wait time between measurements in seconds (Default: 0)
            unipolar: bool
                Set modulation method to unipolar
                (Changes the RF from master frequency to delta_rf, default is by +/- delta_rf/2)
            physics: bool
                Archive and display data in physics units (Default: Hardware units, m/Hz)
            no_display: bool
                Do not draw plots from measured data (Default: Draw)
            save: bool
                Save measured data in .dat file (Default: Do not save)
            archive: bool
                Save measured data in archive file (Default: Do not save)

    See also
    --------
    measure_dispersion, measure_chromaticity, monitor_bpm

    Notes
    -----
    Inputs are passed from script via argument parser or with keyword arguments, all are optional
    WARNING: Function has not yet been tested online TODO
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann, Jeff Corbett and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    May 2024
    """

    # Initialising arguments
    hcm_kicks = flags.get('hcm_kick')
    vcm_kicks = flags.get('vcm_kick')
    wait = 0

    hcm_list = []
    vcm_list = []
    bpm_x_list = []
    bpm_y_list = []

    # Initialising values from flags (bool arguments kept as flag attributes)
    if flags.get('wait'):
        wait = flags.get('wait')

    if flags.get('hcm_list'):
        hcm_list = flags.get('hcm_list')

    if flags.get('vcm_list'):
        vcm_list = flags.get('vcm_list')

    if flags.get('bpm_x_list'):
        bpm_x_list = flags.get('bpm_x_list')

    if flags.get('bpm_y_list'):
        bpm_y_list = flags.get('bpm_y_list')

    qui = input('\nYou are about to measure an orbit response matrix\n'
                'Please check the following steps have been performed before starting:\n\n'
                'Do not forget to switch OFF QT magnets before any measurement\n'
                '1. All feedbacks are OFF \n'
                '2. Tune excitations are OFF \n'
                '3. Booster tuned to economic mode \n'
                '4. Dispersion function has been measured and archived \n'
                '5. BPM noise has been measured and looks fine \n\n'
                'Do you want to continue? (y/n): ')
    if qui != 'y':
        print("Orbit measurement aborted.\n")
        return

    # Get list of active correctors
    hcm_list = get_active_device_list(AcceleratorObjects.HCOR, hcm_list)
    vcm_list = get_active_device_list(AcceleratorObjects.VCOR, vcm_list)

    hcm_idx = get_device_index(AcceleratorObjects.HCOR, hcm_list)
    vcm_idx = get_device_index(AcceleratorObjects.VCOR, vcm_list)

    # Read kick value from AO or verify input type
    if hcm_kicks is None:
        hcm_kicks = [AcceleratorObjects.HCOR.Setpoint.delta_resp_mat[i] for i in hcm_idx]

    elif not isinstance(hcm_kicks, (list, tuple, float, int)):
        print("Incorrect data type of hcm kick\n")
        return
    elif isinstance(hcm_kicks, (list, tuple)) and len(hcm_kicks) != len(hcm_list):
        print("Number of passed hcm kick values should match number of active called HCMs or be a single value")
        return

    if vcm_kicks is None:
        vcm_kicks = [AcceleratorObjects.VCOR.Setpoint.delta_resp_mat[i] for i in vcm_idx]
    elif not isinstance(vcm_kicks, (list, tuple, float, int)):
        print("Incorrect data type of vcm kick")
        return
    elif isinstance(vcm_kicks, (list, tuple)) and len(vcm_kicks) != len(vcm_list):
        print("Number of passed vcm kick values should match number of active called VCMs or be a single value")
        return

    # Measure response matrix
    print("Begin BPM response measurement")

    resp_h = measure_response_matrix([AcceleratorObjects.BPMx, AcceleratorObjects.BPMz],
                                     [bpm_x_list, bpm_y_list], AcceleratorObjects.HCOR, hcm_list, hcm_kicks,
                                     flags.get("unipolar"), wait, flags.get("archive"))

    resp_v = measure_response_matrix([AcceleratorObjects.BPMx, AcceleratorObjects.BPMz],
                                     [bpm_x_list, bpm_y_list], AcceleratorObjects.VCOR, vcm_list, vcm_kicks,
                                     flags.get("unipolar"), wait, flags.get("archive"))

    # Print results
    if not flags.get('no_display') and flags.get('archive'):
        print("Horizontal response:")
        print(resp_h.data)

        print("\nVertical response:")
        print(resp_v.data)

    elif not flags.get('no_display'):
        print("Horizontal response:")
        print(resp_h)

        print("\nVertical response:")
        print(resp_v)

    # Save results to numeric file
    if flags.get('save'):
        file_path = AcceleratorData.Directory.BPM_response
        file_fullname = (file_path + AcceleratorData.Default.BPM_archive_file + '_'
                         + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.dat')

        resp = np.hstack([resp_h, resp_v])
        np.savetxt(file_fullname, resp, delimiter=' ')

        print("Data saved to {}\nBPM response measurement complete\n".format(file_fullname))
        return file_fullname

    # Save results to archive object similar to MATLAB's structure
    if flags.get('archive'):
        file_path = AcceleratorData.Directory.BPM_response
        file_fullname = (file_path + AcceleratorData.Default.BPM_archive_file + '_'
                         + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.json')

        with open(file_fullname, 'w') as archive:
            json.dump(resp_h, archive)
            archive.write("\n")
            json.dump(resp_v, archive)

        print("Data saved to {}\nBPM response measurement complete\n".format(file_fullname))
        return file_fullname

    print("BPM response measurement complete\n")


# -------------------------------------------------------------------------------------------------------------------
# Argument parser
parser = argparse.ArgumentParser(
    prog='measure_bpm_response',
    description='Measures the BPM response matrix in the horizontal and vertical planes')

parser.add_argument('--hcm_kick',
                    help='Change in HCM correctors (Default: read from HCOR response matrix)')
parser.add_argument('--vcm_kick',
                    help='Change in VCM correctors (Default: read from VCOR response matrix)')
parser.add_argument('--hcm_list',
                    help='List of HCM correctors used in the measurement (Default: all HCMs)')
parser.add_argument('--vcm_list',
                    help='List of VCM correctors used in the measurement (Default: all VCMs)')
parser.add_argument('--bpm_x_list', '-x',
                    help='List of xBPMs that are performing the measurement (Default: all BPMs)')
parser.add_argument('--bpm_y_list', '-y',
                    help='List of yBPMs that are performing the measurement (Default: all BPMs)')
parser.add_argument('--wait', '-w',
                    help='Wait time between measurements in seconds (Default: 0)')
parser.add_argument('--unipolar', action='store_true',
                    help='Set modulation method to unipolar (Changes the RF from master frequency to delta_rf, '
                         'default is by +/- delta_rf/2)')
parser.add_argument('--physics', action='store_true',
                    help='Archive and display data in physics units (Default: Hardware)')
parser.add_argument('--no_display', action='store_true',
                    help='Do not draw plots from measured data (Default: Draw)')
parser.add_argument('--save', action='store_true',
                    help='Save measured data in .dat file (Default: Do not save)')
parser.add_argument('--archive', action='store_true',
                    help='Save measured data in archive object (Default: Do not save)')

# Parse arguments
args = parser.parse_args()
args = vars(args)

# Correct input types
args["hcm_kick"] = float(args["hcm_kick"]) if args.get("hcm_kick") else None
args["vcm_kick"] = float(args["vcm_kick"]) if args.get("vcm_kick") else None

args["hcm_list"] = parse_list(args["hcm_list"])
args["vcm_list"] = parse_list(args["vcm_list"])

args["bpm_x_list"] = parse_list(args["bpm_x_list"])
args["bpm_y_list"] = parse_list(args["bpm_y_list"])

args["wait"] = float(args["wait"]) if args.get("wait") else None

# execute function
measure_bpm_response(**args)
