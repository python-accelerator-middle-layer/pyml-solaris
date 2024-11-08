import argparse

import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

from . import measure_response_matrix

from ..data.context import AcceleratorObjects


def measure_dispersion(
        delta_rf: float = None, bpm_x_list=None, bpm_y_list=None, wait: float = 0,
        unipolar: bool = False, physics: bool = False, no_display: bool = False,
        save: bool = False, archive: bool = False,
) -> str:
    """
    Measures the dispersion function based on online data. Plots results to the screen
    or writes them to an archive file

    Parameters
    ----------
    delta_rf: float
        Change in RF frequency in Hz (Default: 0.2% energy change)
    bpm_x_list: Iterable
        List of xBPMs that are performing the measurement (Default: all BPMs)
    bpm_y_list: Iterable
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
    measure_chromaticity, measure_bpm_response, monitor_bpm

    Notes
    -----
    Inputs are passed from script via argument parser or with keyword arguments,
    all are optional
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann, Jeff Corbett and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    2nd version
    November 2024
    """
    ao = AcceleratorObjects()

    # Check with user for large values
    if not delta_rf:
        delta_rf = ao.machine_data['delta_rf_disp']
    elif delta_rf > 1000:
        qui = input(
            f"{delta_rf} Hz is a large RF change. "
            f"Are you sure you want to continue? (y/n): "
            )

        if qui != 'y':
            print("Dispersion measurement aborted.\n")
            return ''

    # rf_units must be in hardware units (to be remade when physics flag is introduced)
    # TODO introduce physics flag
    # rf_units = AcceleratorObjects.RF.Setpoint.hw_units

    # Measure dispersion
    dispersion = measure_response_matrix(
        ('BPMx', 'BPMz'), 'RF', delta_rf, wait, unipolar
    )

    # Convert default units (nm/Hz) to SI (mm/Hz)
    dispersion[0] *= 1e-6
    dispersion[1] *= 1e-6

    # Plot results
    if not no_display and not archive:
        bpm_numbers = ao.BPMx.element_list
        fig, ax = plt.subplots(2)
        fig.suptitle("Dispersion function")

        ax[0].plot(bpm_numbers, dispersion[0][0])
        ax[0].scatter(bpm_numbers, dispersion[0][0], s=10)
        ax[0].set_xlabel('BPM Number')
        ax[0].set_ylabel('Horizontal [mm/Hz]')

        ax[1].plot(bpm_numbers, dispersion[1][0])
        ax[1].scatter(bpm_numbers, dispersion[1][0], s=10)
        ax[1].set_xlabel('BPM Number')
        ax[1].set_ylabel('Vertical [mm/Hz]')

        plt.subplots_adjust(hspace=0.4, left=0.2)
        ax[0].grid()
        ax[1].grid()
        plt.show()

    # TODO archive object similar to MATLAB's structure
    # Save results to archive file
    if save:
        file_path = ao.directories.disp_response
        file_fullname = (file_path + ao.default_names.disp_archive_file + '_'
                         + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.dat')

        np.savetxt(file_fullname, dispersion, delimiter=' ')

        print(f"Data saved to {file_fullname}\nDispersion measurement complete")
        return file_fullname

    print('Dispersion measurement complete\n')


# ---------------------------------------------------------------------------------------
if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(
        prog='measure_dispersion',
        description='Measures the dispersion function')

    parser.add_argument(
        '--delta_rf', '-rf', type=float,
        help='Change in RF frequency in Hz (Default: 0.2% energy change)'
    )
    parser.add_argument(
        '--bpm_x_list', '-x', type=int, nargs='+',
        help='List of xBPMs that are performing the measurement (Default: all BPMs)'
    )
    parser.add_argument(
        '--bpm_y_list', '-y', type=int, nargs='+',
        help='List of yBPMs that are performing the measurement (Default: all BPMs)'
    )
    parser.add_argument(
        '--wait', '-w', type=float,
        help='Wait time between measurements in seconds (Default: 0)'
    )
    parser.add_argument(
        '--unipolar', action='store_true',
        help='Set modulation method to unipolar '
        '(Changes the RF from master frequency to delta_rf, default is by +/- delta_rf/2)'
    )
    parser.add_argument(
        '--physics', action='store_true',
        help='Archive and display data in physics units (Default: Hardware)'
    )
    parser.add_argument(
        '--no_display', action='store_true',
        help='Do not draw plots from measured data (Default: Draw)'
    )
    parser.add_argument(
        '--save', action='store_true',
        help='Save measured data in .dat file (Default: Do not save)'
    )
    parser.add_argument(
        '--archive', action='store_true',
        help='Save measured data in archive object (Default: Do not save)'
    )

    # Parse arguments
    args = parser.parse_args()
    args = vars(args)

    # execute function
    measure_dispersion(**args)
