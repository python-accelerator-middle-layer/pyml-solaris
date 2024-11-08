import argparse

import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
from time import time, sleep

from ..data.context import AcceleratorObjects


def monitor_bpm(time_period: float = 180., delta_t: float = .5,
                bpm_x_list=None, bpm_y_list=None,
                save: bool = False, archive: bool = False):
    """
    Monitors the orbit to determine BPM noise.

    Parameters
    ----------
    time_period: float
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
    WARNING: Acquisition takes ~0.2 seconds online, so delta_t should be bigger than that
    WORK IN PROGRESS

    Adapted from MATLAB code by Gregory J. Portmann, Jeff Corbett and Laurent S. Nadolski
    Written by Mikolaj Wrobel
    2nd version
    November 2024
    """
    ao = AcceleratorObjects()

    # Preallocate arrays
    num_measurements = int(time_period // delta_t)
    time_vector = np.array(range(num_measurements)) * delta_t
    bpm_x = np.empty((num_measurements, len(ao.BPMx)))
    bpm_y = np.empty((num_measurements, len(ao.BPMz)))

    # Begin measurement
    print(f"Monitoring orbit for {time_period} seconds")

    for i in range(num_measurements):
        start_time = time()
        bpm_x[i] = ao.BPMx.monitor(offset=True)
        bpm_y[i] = ao.BPMz.monitor(offset=True)

        measurement_time = time() - start_time
        remaining_time = max(delta_t - measurement_time, 0)
        sleep(remaining_time)

    # Convert to mm
    bpm_x /= 1e6
    bpm_y /= 1e6

    # Low frequency drifting increases the deviation.
    # Using difference orbits mitigates this.
    # TODO: This solution needs to be verified
    x_std = np.std(np.diff(bpm_x, axis=1), axis=0) / 2 ** (1 / 2)
    y_std = np.std(np.diff(bpm_y, axis=1), axis=0) / 2 ** (1 / 2)

    bpm_number = np.arange(0, x_std.shape[0], 1)

    # Plot results
    if not archive:
        fig, ax = plt.subplots(2, 2)
        fig.suptitle("Orbit monitor")

        for i in range(bpm_x.shape[1]):
            ax[0, 0].plot(time_vector, bpm_x[:, i], label=f"BPMx {i}")
            ax[1, 0].plot(time_vector, bpm_y[:, i], label=f"BPMy {i}")

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
    if save:
        file_path = ao.directories.bpm_data
        file_fullname = (file_path + ao.default_names.BPM_archive_file + '_'
                         + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.dat')

        output = np.hstack((time_vector.reshape(-1, 1), bpm_x, bpm_y))

        np.savetxt(file_fullname, output, delimiter=' ')
        print("Data saved to {}\nBPM noise measurement complete\n".format(file_fullname))
        return file_fullname

    print('BPM noise measurement complete\n')


# ---------------------------------------------------------------------------------------
if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(
        prog='monitor_bpm',
        description='Monitors the orbit to determine BPM noise')

    parser.add_argument(
        '--time_period', '-t', type=float,
        help='Time period to measure the data in seconds (Default: 180)')
    parser.add_argument(
        '--delta_t', '-dt', type=float,
        help='Time between samples in seconds (Default: 0.5)')
    parser.add_argument(
        '--bpm_x_list', '-x', type=int, nargs='+',
        help='List of xBPMs that are performing the measurement (Default: all BPMs)')
    parser.add_argument(
        '--bpm_y_list', '-y', type=int, nargs='+',
        help='List of yBPMs that are performing the measurement (Default: all BPMs)')
    parser.add_argument(
        '--save', action='store_true',
        help='Save measured data in .dat file (Default: Do not save)')
    parser.add_argument(
        '--archive', action='store_true',
        help='Save measured data in archive object (Default: Do not save)')

    # Parse arguments
    args = parser.parse_args()
    args = vars(args)

    if not args["time_period"]:
        args["time_period"] = 5.

    if not args["delta_t"]:
        args["delta_t"] = .5

    # execute function
    monitor_bpm(**args)
