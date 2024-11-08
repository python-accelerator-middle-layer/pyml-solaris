"""
Script used to create AcceleratorObjects object, passed to other scripts using context.py
"""

from .globals import AcceleratorObjects

# General machine info
machine_address = 'tango.machine:10000/'

machine_data = dict(
    AT_model='solaris_001',
    machine='Solaris',
    machine_type='StorageRing',

    BPM_delay=0.25,
    circumference=96.,
    sections=12,
    energy=1.5,
    harmonic_number=32,
    MCF=0.0031,
    tune_delay=0.1,

    delta_rf_chro=(-0.0001, -0.00005, 0, 0.00005, 0.00015),
    delta_rf_disp=1e-4
)

directories = dict(
    disp_data='/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Dispersion/',
    bpm_response='/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/'
                 'Response/BPM/',
    bpm_data='/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/BPM/',
    loco_data='/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/LOCO/'
)

default_names = dict(
    disp_archive_file='Disp',
    bpm_archive_file='BPM',
)

AcceleratorObjects.machine_data = machine_data
AcceleratorObjects.directories = directories
AcceleratorObjects.default_names = default_names

"""
BPM Data
"""

# TANGO addresses
bpm_devices = tuple(machine_address + device for device in (
    'R1-01/DIA/R1-01-DIA-BPM1', 'R1-01/DIA/R1-01-DIA-BPM2', 'R1-01/DIA/R1-01-DIA-BPM3',
    'R1-02/DIA/R1-02-DIA-BPM1', 'R1-02/DIA/R1-02-DIA-BPM2', 'R1-02/DIA/R1-02-DIA-BPM3',
    'R1-03/DIA/R1-03-DIA-BPM1', 'R1-03/DIA/R1-03-DIA-BPM2', 'R1-03/DIA/R1-03-DIA-BPM3',
    'R1-04/DIA/R1-04-DIA-BPM1', 'R1-04/DIA/R1-04-DIA-BPM2', 'R1-04/DIA/R1-04-DIA-BPM3',
    'R1-05/DIA/R1-05-DIA-BPM1', 'R1-05/DIA/R1-05-DIA-BPM2', 'R1-05/DIA/R1-05-DIA-BPM3',
    'R1-06/DIA/R1-06-DIA-BPM1', 'R1-06/DIA/R1-06-DIA-BPM2', 'R1-06/DIA/R1-06-DIA-BPM3',
    'R1-07/DIA/R1-07-DIA-BPM1', 'R1-07/DIA/R1-07-DIA-BPM2', 'R1-07/DIA/R1-07-DIA-BPM3',
    'R1-08/DIA/R1-08-DIA-BPM1', 'R1-08/DIA/R1-08-DIA-BPM2', 'R1-08/DIA/R1-08-DIA-BPM3',
    'R1-09/DIA/R1-09-DIA-BPM1', 'R1-09/DIA/R1-09-DIA-BPM2', 'R1-09/DIA/R1-09-DIA-BPM3',
    'R1-10/DIA/R1-10-DIA-BPM1', 'R1-10/DIA/R1-10-DIA-BPM2', 'R1-10/DIA/R1-10-DIA-BPM3',
    'R1-11/DIA/R1-11-DIA-BPM1', 'R1-11/DIA/R1-11-DIA-BPM2', 'R1-11/DIA/R1-11-DIA-BPM3',
    'R1-12/DIA/R1-12-DIA-BPM1', 'R1-12/DIA/R1-12-DIA-BPM2', 'R1-12/DIA/R1-12-DIA-BPM3'
))

x_offset = (
            0.153374, 0.188851, -0.346411, -0.1617, -0.398131, 0.167579, 0.234644,
            -0.375706, -0.01495, -0.085342, 0.180363, -0.116696, 0.245268, -0.102028,
            -0.033271, 0.30686, 0.006561, 0.052198, 0.176602, -0.22888, 0.096128,
            0.464092, 0.45, -0.063526, 0.284418, 0.001044, 0.031086, 0.10072, -0.447612,
            0.124272, 0.106986, 0.520484, -0.322414, -0.012204, 0.622486, -0.043746
)

z_offset = (
            -0.12755, -0.3681, -0.15165, 0.04733, 0.02625, 0.18839, 0.2534, -0.037393,
            -0.029, 0.277314, -0.02795, 0.1549, 0.03785, 0.00945, -0.096996, -0.1163,
            -0.1356, 0.2629, -0.1686, 0.03125, 0.20235, 0.19535, 0.23915, 0.38705,
            -0.21175, -0.23905, -0.12585, 0.072115, -0.0667, -0.0389, -0.4831, -0.11258,
            0.1895, 0.13105, 0.32275, 0.2886
)

# Create families
AcceleratorObjects.add_family('BPMx', bpm_devices)
AcceleratorObjects.add_family('BPMz', bpm_devices)

# Add monitors
AcceleratorObjects.BPMx.set_default_monitor('SaX')
AcceleratorObjects.BPMz.set_default_monitor('SaY')

AcceleratorObjects.BPMx.set_units('mm')
AcceleratorObjects.BPMz.set_units('mm')

AcceleratorObjects.BPMx.set_offsets(x_offset)
AcceleratorObjects.BPMz.set_offsets(z_offset)

"""
Corrector magnets
"""

# TANGO addresses (power supplies)
hcor_devices = tuple(machine_address + device for device in (
    'R1-SGA / MAG / R1-SGACAB14-MAG-PS01', '', 'R1-SGA / MAG / R1-SGACAB14-MAG-PS13',
    'R1-SGA / MAG / R1-SGACAB14-MAG-PS02', 'R1-SGA / MAG / R1-SGACAB14-MAG-PS03', '',
    'R1-SGA / MAG / R1-SGACAB14-MAG-PS14', 'R1-SGA / MAG / R1-SGACAB14-MAG-PS04',
    'R1-SGA / MAG / R1-SGACAB14-MAG-PS05', '', 'R1-SGA / MAG / R1-SGACAB14-MAG-PS15',
    'R1-SGA / MAG / R1-SGACAB14-MAG-PS06', 'R1-SGB / MAG / R1-SGBCAB06-MAG-PS01', '',
    'R1-SGB / MAG / R1-SGBCAB06-MAG-PS13', 'R1-SGB / MAG / R1-SGBCAB06-MAG-PS02',
    'R1-SGB / MAG / R1-SGBCAB06-MAG-PS03', '', 'R1-SGB / MAG / R1-SGBCAB06-MAG-PS14',
    'R1-SGB / MAG / R1-SGBCAB06-MAG-PS04', 'R1-SGB / MAG / R1-SGBCAB06-MAG-PS05', '',
    'R1-SGB / MAG / R1-SGBCAB06-MAG-PS15', 'R1-SGB / MAG / R1-SGBCAB06-MAG-PS06',
    'R1-SGC / MAG / R1-SGCCAB12-MAG-PS01', '', 'R1-SGC / MAG / R1-SGCCAB12-MAG-PS13',
    'R1-SGC / MAG / R1-SGCCAB12-MAG-PS02', 'R1-SGC / MAG / R1-SGCCAB12-MAG-PS03', '',
    'R1-SGC / MAG / R1-SGCCAB12-MAG-PS14', 'R1-SGC / MAG / R1-SGCCAB12-MAG-PS04',
    'R1-SGC / MAG / R1-SGCCAB12-MAG-PS05', '', 'R1-SGC / MAG / R1-SGCCAB12-MAG-PS15',
    'R1-SGC / MAG / R1-SGCCAB12-MAG-PS06', 'R1-SGD / MAG / R1-SGDCAB02-MAG-PS05', '',
    'R1-SGD / MAG / R1-SGDCAB02-MAG-PS20', 'R1-SGD / MAG / R1-SGDCAB02-MAG-PS06',
    'R1-SGD / MAG / R1-SGDCAB02-MAG-PS07', '', 'R1-SGD / MAG / R1-SGDCAB02-MAG-PS21',
    'R1-SGD / MAG / R1-SGDCAB02-MAG-PS08', 'R1-SGD / MAG / R1-SGDCAB02-MAG-PS09', '',
    'R1-SGD / MAG / R1-SGDCAB02-MAG-PS22', 'R1-SGD / MAG / R1-SGDCAB02-MAG-PS10'
))

vcor_devices = tuple(machine_address + device for device in (
    "R1-SGA/MAG/R1-SGACAB14-MAG-PS07", '', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS16',
    'R1-SGA/MAG/R1-SGACAB14-MAG-PS08', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS09', '',
    'R1-SGA/MAG/R1-SGACAB14-MAG-PS17', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS10',
    'R1-SGA/MAG/R1-SGACAB14-MAG-PS11', '', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS18',
    'R1-SGA/MAG/R1-SGACAB14-MAG-PS12', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS07', '',
    'R1-SGB/MAG/R1-SGBCAB06-MAG-PS16', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS08',
    'R1-SGB/MAG/R1-SGBCAB06-MAG-PS09', '', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS17',
    'R1-SGB/MAG/R1-SGBCAB06-MAG-PS10', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS11', '',
    'R1-SGB/MAG/R1-SGBCAB06-MAG-PS18', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS12',
    'R1-SGC/MAG/R1-SGCCAB12-MAG-PS07', '', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS16',
    'R1-SGC/MAG/R1-SGCCAB12-MAG-PS08', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS09', '',
    'R1-SGC/MAG/R1-SGCCAB12-MAG-PS17', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS10',
    'R1-SGC/MAG/R1-SGCCAB12-MAG-PS11', '', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS18',
    'R1-SGC/MAG/R1-SGCCAB12-MAG-PS12', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS11', '',
    'R1-SGD/MAG/R1-SGDCAB02-MAG-PS23', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS12',
    'R1-SGD/MAG/R1-SGDCAB02-MAG-PS13', '', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS24',
    'R1-SGD/MAG/R1-SGDCAB02-MAG-PS14', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS15', '',
    'R1-SGD/MAG/R1-SGDCAB02-MAG-PS25', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS16'
))

# Create families
AcceleratorObjects.add_family('HCOR', hcor_devices)
AcceleratorObjects.add_family('VCOR', vcor_devices)

# Add monitors and setpoints
AcceleratorObjects.HCOR.set_default_monitor('Current')
AcceleratorObjects.VCOR.set_default_monitor('Current')

AcceleratorObjects.HCOR.set_default_setpoint('Current', (-11., 11.))
AcceleratorObjects.VCOR.set_default_setpoint('Current', (-11., 11.))

AcceleratorObjects.HCOR.set_units(
    'A', 'radian', (0., 0., 0., 0., 0., 0., 0.000129717, 2.99849e-06))
AcceleratorObjects.VCOR.set_units(
    'A', 'radian', (0., 0., 0., 0., 0., 0., 0.000109051, 7.77688e-06))

AcceleratorObjects.HCOR.default_delta = 3.83541150899872
AcceleratorObjects.VCOR.default_delta = 4.51843343676617

"""
RF
"""

# Create family
AcceleratorObjects.add_family(
    'RF', machine_address + 'R1-SGD/CTL/R1-SGDCAB10-RF-SIG1/')

# Add monitors and setpoints
AcceleratorObjects.RF.set_default_monitor('Frequency')
AcceleratorObjects.RF.set_default_setpoint('Frequency', (99900000., 100000000.))
AcceleratorObjects.RF.set_units('Hz', 'MHz', 1e-6)

"""
DCCT
"""

# Create family
AcceleratorObjects.add_family(
    'DCCT', machine_address + 'R1-ALL/DIA/R1-ALL-DIA-BIM1')

# Add monitor
AcceleratorObjects.DCCT.set_default_monitor('BeamCurrent')
AcceleratorObjects.DCCT.set_units('A', 'mA', 1e3)
