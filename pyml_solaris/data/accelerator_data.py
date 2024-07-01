class AcceleratorData:
    """
    AcceleratorData imitates MATLAB structure which is normally passed using getappdata("AcceleratorData").
    This solution is very much temporary, as data cannot be easily modified or configured.
    """

    AT_model = 'solaris_001'
    machine = 'Solaris'
    machine_type = 'StorageRing'
    machine_address = 'tango://tango.machine:10000/'
    operational_mode = '1.5 GeV, 11.22 3.15 '
    special_tag = ''
    sub_machine = 'StorageRing'

    BPM_delay = 0.25
    circumference = 96.
    energy = 1.5
    error_warning_level = 0
    harmonic_number = 32
    MCF = 0.0031
    mode_number = 2
    tune_delay = 0.1

    delta_rf_chro = [-0.0001, -0.00005, 0, 0.00005, 0.00015]
    delta_rf_disp = 1e-4

    class Chromaticity:
        golden = [1, 1]

    class Default:
        BPM_archive_file = 'BPM'
        tune_archive_file = 'Tune'
        chro_archive_file = 'Chro'
        disp_archive_file = 'Disp'
        CNF_archive_file = 'CNF'
        BPM_resp_file = 'BPMRespMat'
        tune_resp_file = 'TuneRespMat'
        chro_resp_file = 'ChroRespMat'
        disp_resp_file = 'DispRespMat'
        skew_resp_file = 'SkewRespMat'
        QUAD_archive_file = 'QuadBeta'
        PINHOLE_archive_file = 'Pinhole'
        skew_archive_file = 'SkewQuad'
        BBAA_archive_file = 'BBA_DKmode'

    class Directory:
        data_root = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/'
        ops_data = '/home/Operator/scripts/mml/machine/Solaris/StorageRingOpsData/solaris_001/'
        config_data = '/home/Operator/scripts/mml/machine/Solaris/StorageRing/MachineConfig/'
        BPM_data = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/BPM/'
        tune_data = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Tune/'
        chro_data = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Chromaticity/'
        disp_data = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Dispersion/'
        BPM_response = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Response/BPM/'
        tune_response = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Response/Tune/'
        chro_response = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Response/Chrom/'
        disp_response = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Response/Disp/'
        skew_response = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Response/Skew/'
        lattice = '/home/Operator/scripts/mml/machine/Solaris/StorageRing/Lattices/'
        orbit = '/home/Operator/scripts/mml/machine/Solaris/StorageRing/orbit/'
        beam_user = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/BPM/BeamUser/'
        bump_data = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Bumps/'
        archiving = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/ArchivingData/'
        quad = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/QUAD/'
        synchro = '/home/Operator/scripts/mml/machine/Solaris/common/synchro/'
        LOCO_data = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/LOCO/'
        standalone = '/home/Operator/scripts/standalone_applications/'
        FOFB_data = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/FOFB'
        coupling = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/SkewQuad/solution_QT'
        BPM_transport = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Transport/BPM/'
        steerette = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Transport/Steerette/'
        BPM_postmortem = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Postmortem/BPMPostmortem/'
        RF_postmortem = '/home/Operator/scripts/mml/measdata/Solaris/StorageRingData/Postmortem/RFPostmortem/'
