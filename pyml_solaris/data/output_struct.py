class OutputStruct:

    monitor_start = []
    actuator_start = []
    actuator_delta = []

    monitor_data = []
    units = []

    gev = []
    current = []
    unipolar = []
    wait = []

    timestamp = []
    data_descriptor = []
    created_by = []
    operational_mode = []

    def __init__(self, data):
        self.data = data
