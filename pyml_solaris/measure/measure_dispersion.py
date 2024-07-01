import argparse
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

from measure_response_matrix import measure_response_matrix
from ..util.parse_list import parse_list

from ..data.accelerator_objects import AcceleratorObjects
from ..data.accelerator_data import AcceleratorData


def measure_dispersion(**flags):
    """
    Measures the dispersion function based on online data. Plots results to the screen or writes them to archive file

    Parameters
    ----------
    **flags: dict, optional
        By default passed from argument parser, but can be called on its own. Available keywords:
            delta_rf: float
                Change in RF frequency in Hz (Default: 0.2% energy change)
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
    measure_chromaticity, measure_bpm_response, monitor_bpm

    Notes
    -----
    Inputs are passed from script via argument parser or with keyword arguments, all are optional
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann, Jeff Corbett and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    May 2024
    """

    # Initialising arguments
    bpm_x_list = []
    bpm_y_list = []
    wait = 0
    delta_rf = flags.get('delta_rf')

    # Initialising values from flags (bool arguments kept as flag attributes)
    if delta_rf is None:
        delta_rf = AcceleratorData.delta_rf_disp
    elif delta_rf > 1000:
        qui = input("{} Hz is a large RF change. Are you sure you want to continue? (y/n): ".format(delta_rf))
        if qui != 'y':
            print("Dispersion measurement aborted.\n")
            return

    if flags.get('wait'):
        wait = flags.get('wait')

    if flags.get('bpm_x_list'):
        bpm_x_list = flags.get('bpm_x_list')

    if flags.get('bpm_y_list'):
        bpm_y_list = flags.get('bpm_y_list')

    # rf_units must be in hardware units (to be remade when physics flag is introduced) TODO
    # rf_units = AcceleratorObjects.RF.Setpoint.hw_units

    # Measure dispersion
    dispersion = measure_response_matrix([AcceleratorObjects.BPMx, AcceleratorObjects.BPMz],
                                         [bpm_x_list, bpm_y_list], AcceleratorObjects.RF, [],
                                         delta_rf, flags.get('unipolar'), wait, flags.get("archive"))

    # Convert default units (nm/Hz) to SI (mm/Hz)
    dispersion *= 1e-6

    # Plot results
    if not flags.get('no_display') and not flags.get('archive'):
        bpm_numbers = AcceleratorObjects.BPMx.element_list
        fig, ax = plt.subplots(2)
        fig.suptitle("Dispersion function")

        ax[0].plot(bpm_numbers, dispersion[0])
        ax[0].scatter(bpm_numbers, dispersion[0], s=10)
        ax[0].set_xlabel('BPM Number')
        ax[0].set_ylabel('Horizontal [mm/Hz]')

        ax[1].plot(bpm_numbers, dispersion[1])
        ax[1].scatter(bpm_numbers, dispersion[1], s=10)
        ax[1].set_xlabel('BPM Number')
        ax[1].set_ylabel('Vertical [mm/Hz]')

        plt.subplots_adjust(hspace=0.4, left=0.2)
        ax[0].grid()
        ax[1].grid()
        plt.show()

    # TODO archive object similar to MATLAB's structure
    # Save results to archive file
    if flags.get('save'):
        file_path = AcceleratorData.Directory.disp_response
        file_fullname = (file_path + AcceleratorData.Default.disp_archive_file + '_'
                         + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.dat')

        np.savetxt(file_fullname, dispersion, delimiter=' ')

        print("Data saved to {}\nDispersion measurement complete\n".format(file_fullname))
        return file_fullname

    print('Dispersion measurement complete\n')


# -------------------------------------------------------------------------------------------------------------------
# Argument parser
parser = argparse.ArgumentParser(
    prog='measure_dispersion',
    description='Measures the dispersion function')

parser.add_argument('--delta_rf', '-rf',
                    help='Change in RF frequency in Hz (Default: 0.2% energy change)')
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
args["delta_rf"] = float(args["delta_rf"]) if args.get("delta_rf") else None

args["bpm_x_list"] = parse_list(args["bpm_x_list"])
args["bpm_y_list"] = parse_list(args["bpm_y_list"])

args["wait"] = float(args["wait"]) if args.get("wait") else None

# execute function
measure_dispersion(**args)
