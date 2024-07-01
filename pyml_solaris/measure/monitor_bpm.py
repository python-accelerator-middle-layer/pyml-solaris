import argparse
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

from ..util.parse_list import parse_list
from ..data.get_var import get_var

from ..data.accelerator_data import AcceleratorData
from ..data.accelerator_objects import AcceleratorObjects


def monitor_bpm(**flags):
    """
    Monitors the orbit to determine BPM noise.

    Parameters
    ----------
    **flags: dict, optional
        By default passed from argument parser, but can be called on its own. Available keywords:
            t: float
                Time period to measure the data in seconds (Default: 180)
            delta_t: float
                Time between samples in seconds (Default: 0.5)
            bpm_x_list: list or int or str
                List of xBPMs that are performing the measurement (Default: all BPMs)
            bpm_y_list: list or int or str
                List of yBPMs that are performing the measurement (Default: all BPMs)
            save: bool
                Save measured data in .dat file (Default: Do not save)
            archive: bool
                Save measured data in archive file (Default: Do not save)


    See also
    --------
    measure_dispersion, measure_chromaticity, measure_bpm_response

    Notes
    -----
    Inputs are passed from script via argument parser or with keyword arguments, all are optional
    WARNING: Function is too slow to work reliably, data acquisition needs to be modified
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann, Jeff Corbett and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    May 2024
    """

    # Initialising arguments
    bpm_x_list = []
    bpm_y_list = []
    t = 5
    delta_t = .5

    # Initialising values from flags (bool arguments kept as flag attributes)
    if flags.get('bpm_x_list'):
        bpm_x_list = flags.get('bpm_x_list')

    if flags.get('bpm_y_list'):
        bpm_y_list = flags.get('bpm_y_list')

    if flags.get('time'):
        t = flags.get('time')

    if flags.get('delta_t'):
        delta_t = flags.get('delta_t')

    bpm_x = []
    bpm_y = []
    time_list = [0]

    # TODO: this solution is too slow (~2 seconds with sleep())
    # Begin measurement
    print("Monitoring orbit for {} seconds".format(t))
    t0 = time.time()
    t1 = -1
    while t1 < t:
        bpm_x.append(get_var(AcceleratorObjects.BPMx, bpm_x_list))
        bpm_y.append(get_var(AcceleratorObjects.BPMz, bpm_y_list))

        time.sleep(delta_t)
        t1 = time.time() - t0

        print(f"time = {t1}")  # test output
        time_list.append(t1)

    # Refactor into numpy arrays and convert to mm
    bpm_x = np.array(bpm_x)/1e6
    bpm_y = np.array(bpm_y)/1e6

    # Adjust data by including offsets
    offset_x = np.array(AcceleratorObjects.BPMx.offset)
    offset_y = np.array(AcceleratorObjects.BPMz.offset)

    bpm_x -= offset_x
    bpm_y -= offset_y

    # Low frequency drifting increases the deviation. Using difference orbits mitigates this.
    # TODO: This solution needs to be verified
    x_std = np.std(np.diff(bpm_x, axis=1), axis=0) / 2**(1/2)   # math.sqrt(2) equivalent
    y_std = np.std(np.diff(bpm_y, axis=1), axis=0) / 2**(1/2)

    bpm_number = np.arange(0, x_std.shape[0], 1)

    # Plot results
    if not flags.get('no_display'):
        fig, ax = plt.subplots(2, 2)
        fig.suptitle("Orbit monitor")

        for i in range(bpm_x.shape[1]):
            ax[0, 0].plot(time_list, bpm_x[:, i], label=f"BPMx {i+1}")
            ax[1, 0].plot(time_list, bpm_y[:, i], label=f"BPMy {i+1}")

        ax[0, 1].plot(bpm_number, x_std)
        ax[1, 1].plot(bpm_number, y_std)

        ax[0, 0].set_xlabel('Time [s]')
        ax[0, 0].set_ylabel('Horizontal positions [mm]')
        ax[0, 0].tick_params(labelsize=8)

        ax[1, 0].set_xlabel('Time [s]')
        ax[1, 0].set_ylabel('Vertical positions [mm]')
        ax[1, 0].tick_params(labelsize=8)

        ax[0, 1].set_xlabel('BPM Number [-]')
        ax[0, 1].set_ylabel('Horizontal deviation [mm]')
        ax[0, 1].tick_params(labelsize=8)

        ax[1, 1].set_xlabel('BPM Number [-]')
        ax[1, 1].set_ylabel('Vertical deviation [mm]')
        ax[1, 1].tick_params(labelsize=8)

        plt.subplots_adjust(hspace=0.4, wspace=0.4)
        ax[0, 0].grid()
        ax[1, 0].grid()
        ax[0, 1].grid()
        ax[1, 1].grid()
        plt.show()

    # TODO: archive object similar to MATLAB's structure
    # Save results to archive file TODO: expand with deviations
    if flags.get('saves'):
        file_path = AcceleratorData.Directory.BPM_data
        file_fullname = (file_path + AcceleratorData.Default.BPM_archive_file + '_'
                         + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.dat')

        output = np.hstack((time_list.reshape(-1, 1), bpm_x, bpm_y))

        np.savetxt(file_fullname, output, delimiter=' ')
        print("Data saved to {}\nBPM noise measurement complete\n".format(file_fullname))
        return file_fullname

    print('BPM noise measurement complete\n')


# -------------------------------------------------------------------------------------------------------------------
# Argument parser
parser = argparse.ArgumentParser(
    prog='monitor_bpm',
    description='Monitors the orbit to determine BPM noise')

parser.add_argument('--time', '-t',
                    help='Time period to measure the data in seconds (Default: 180)')
parser.add_argument('--delta_t', '-dt',
                    help='Time between samples in seconds (Default: 0.5)')
parser.add_argument('--bpm_x_list', '-x',
                    help='List of xBPMs that are performing the measurement (Default: all BPMs)')
parser.add_argument('--bpm_y_list', '-y',
                    help='List of yBPMs that are performing the measurement (Default: all BPMs)')
parser.add_argument('--save', action='store_true',
                    help='Save measured data in .dat file (Default: Do not save)')
parser.add_argument('--archive', action='store_true',
                    help='Save measured data in archive object (Default: Do not save)')

# Parse arguments
args = parser.parse_args()
args = vars(args)

args["time"] = float(args["time"]) if args.get("time") else None
args["delta_t"] = float(args["delta_t"]) if args.get("delta_t") else None

args["bpm_x_list"] = parse_list(args["bpm_x_list"])
args["bpm_y_list"] = parse_list(args["bpm_y_list"])

# execute function
monitor_bpm(**args)
