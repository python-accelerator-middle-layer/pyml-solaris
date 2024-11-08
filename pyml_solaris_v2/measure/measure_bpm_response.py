import argparse
from datetime import datetime

import numpy as np

from . import measure_response_matrix
from ..data.context import AcceleratorObjects


def measure_bpm_response(
        hcm_kick: float = None, vcm_kick: float = None,
        hcm_list=None, vcm_list=None, bpm_x_list=None, bpm_y_list=None,
        wait: float = 0, unipolar: bool = False, physics: bool = False,
        no_display: bool = False, save: bool = False, archive: bool = False,
) -> str:
    """
    Measures the BPM response matrix to correction magnet kicks.

    Parameters
    ----------
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
    WARNING: Function has not yet been tested online TODO
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann, Jeff Corbett and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    2nd version
    November 2024
    """
    ao = AcceleratorObjects()

    qui = input('\nYou are about to measure an orbit response matrix\n'
                'Please check the following steps have been performed before starting:\n'
                'Do not forget to switch OFF QT magnets before any measurement\n'
                '1. All feedbacks are OFF \n'
                '2. Tune excitations are OFF \n'
                '3. Booster tuned to economic mode \n'
                '4. Dispersion function has been measured and archived \n'
                '5. BPM noise has been measured and looks fine \n\n'
                'Do you want to continue? (y/n): ')
    if qui != 'y':
        print("Orbit response matrix measurement aborted.\n")
        return ''

    # Read kick value from AO or verify input type
    if not hcm_kick:
        hcm_kick = ao.HCOR.default_delta

    if not vcm_kick:
        vcm_kick = ao.VCOR.default_delta

    # Measure response matrix
    print("Begin BPM response measurement")

    resp_mat = measure_response_matrix(
        ('BPMx', 'BPMz'), ('HCOR', 'VCOR'),
        (hcm_kick, vcm_kick), wait, unipolar
    )

    # Print results
    # if not no_display and archive:
    #     print("Horizontal response:")
    #     print(resp_mat.hdata)
    #
    #     print("\nVertical response:")
    #     print(resp_mat.vdata)

    if not no_display and not archive:
        print("Horizontal response:")
        print(resp_mat[0], resp_mat[2])

        print("\nVertical response:")
        print(resp_mat[1], resp_mat[3])

    # Save results to numeric file
    if save:
        file_path = ao.directories.bpm_response
        file_fullname = (file_path + ao.default_names.bpm_archive_file + '_'
                         + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.dat')

        resp = np.stack(resp_mat)
        np.savetxt(file_fullname, resp, delimiter=' ')

        print(
            "Data saved to {}\nBPM response measurement complete\n".format(file_fullname))
        return file_fullname

    # Save results to archive object similar to MATLAB's structure  TODO

    print("BPM response measurement complete\n")


# ---------------------------------------------------------------------------------------
if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(
        prog='measure_bpm_response',
        description='Measures the BPM response matrix to correction magnet kicks')

    parser.add_argument(
        '--hcm_kick', type=float,
        help='Change in HCM correctors (Default: read from HCOR response matrix)')
    parser.add_argument(
        '--vcm_kick', type=float,
        help='Change in VCM correctors (Default: read from VCOR response matrix)')
    parser.add_argument(
        '--hcm_list', type=int, nargs='+',
        help='List of HCM correctors used in the measurement (Default: all HCMs)')
    parser.add_argument(
        '--vcm_list', type=int, nargs='+',
        help='List of VCM correctors used in the measurement (Default: all VCMs)')
    parser.add_argument(
        '--bpm_x_list', '-x', type=int, nargs='+',
        help='List of xBPMs that are performing the measurement (Default: all BPMs)')
    parser.add_argument(
        '--bpm_y_list', '-y', type=int, nargs='+',
        help='List of yBPMs that are performing the measurement (Default: all BPMs)')
    parser.add_argument(
        '--wait', '-w', type=float,
        help='Wait time between measurements in seconds (Default: 0)')
    parser.add_argument(
        '--unipolar', action='store_true',
        help='Set modulation method to unipolar '
             '(Changes the current from initial to kick, default is by +/- kick/2)')
    parser.add_argument(
        '--physics', action='store_true',
        help='Archive and display data in physics units (Default: Hardware)')
    parser.add_argument(
        '--no_display', action='store_true',
        help='Do not draw plots from measured data (Default: Draw)')
    parser.add_argument(
        '--save', action='store_true',
        help='Save measured data in .dat file (Default: Do not save)')
    parser.add_argument(
        '--archive', action='store_true',
        help='Save measured data in archive object (Default: Do not save)')

    # Parse arguments
    args = parser.parse_args()
    args = vars(args)

    # execute function
    measure_bpm_response(**args)
