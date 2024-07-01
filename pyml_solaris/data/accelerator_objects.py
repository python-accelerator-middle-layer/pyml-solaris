class AcceleratorObjects:
    """
    AcceleratorObjects imitates MATLAB structure which is normally passed using getappdata("AcceleratorObjects").
    This solution is very much temporary, as data cannot be easily modified or configured.
    """
    class BPMx:
        family_name = 'BPMx'
        family_type = 'BPM'
        member_of = ('PlotFamily', 'HBPM', 'BPM', 'Diagnostics', 'Archivable')
        element_list = tuple(range(1, 1+36))
        status = (1,) * 36

        device_name = (
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
        )
        common_names = (
            '01BPMx01', '01BPMx02', '01BPMx03', '02BPMx01', '02BPMx02', '02BPMx03', '03BPMx01', '03BPMx02', '03BPMx03',
            '04BPMx01', '04BPMx02', '04BPMx03', '05BPMx01', '05BPMx02', '05BPMx03', '06BPMx01', '06BPMx02', '06BPMx03',
            '07BPMx01', '07BPMx02', '07BPMx03', '08BPMx01', '08BPMx02', '08BPMx03', '09BPMx01', '09BPMx02', '09BPMx03',
            '10BPMx01', '10BPMx02', '10BPMx03', '11BPMx01', '11BPMx02', '11BPMx03', '12BPMx01', '12BPMx02', '12BPMx03'
        )
        device_list = (
            (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (5, 1),
            (5, 2), (5, 3), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2),
            (9, 3), (10, 1), (10, 2), (10, 3), (11, 1), (11, 2), (11, 3), (12, 1), (12, 2), (12, 3)
        )
        offset = [
            0.153374, 0.188851, -0.346411, -0.1617, -0.398131, 0.167579, 0.234644, -0.375706, -0.01495, -0.085342,
            0.180363, -0.116696, 0.245268, -0.102028, -0.033271, 0.30686, 0.006561, 0.052198, 0.176602, -0.22888,
            0.096128, 0.464092, 0.45, -0.063526, 0.284418, 0.001044, 0.031086, 0.10072, -0.447612, 0.124272, 0.106986,
            0.520484, -0.322414, -0.012204, 0.622486, -0.043746
        ]

        class Monitor:
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'mm'
            physics_units = 'mm'
            tango_names = (
                'R1-01 / DIA / R1-01-DIA-BPM1 / SaX', 'R1-01 / DIA / R1-01-DIA-BPM2 / SaX',
                'R1-01 / DIA / R1-01-DIA-BPM3 / SaX', 'R1-02 / DIA / R1-02-DIA-BPM1 / SaX',
                'R1-02 / DIA / R1-02-DIA-BPM2 / SaX', 'R1-02 / DIA / R1-02-DIA-BPM3 / SaX',
                'R1-03 / DIA / R1-03-DIA-BPM1 / SaX', 'R1-03 / DIA / R1-03-DIA-BPM2 / SaX',
                'R1-03 / DIA / R1-03-DIA-BPM3 / SaX', 'R1-04 / DIA / R1-04-DIA-BPM1 / SaX',
                'R1-04 / DIA / R1-04-DIA-BPM2 / SaX', 'R1-04 / DIA / R1-04-DIA-BPM3 / SaX',
                'R1-05 / DIA / R1-05-DIA-BPM1 / SaX', 'R1-05 / DIA / R1-05-DIA-BPM2 / SaX',
                'R1-05 / DIA / R1-05-DIA-BPM3 / SaX', 'R1-06 / DIA / R1-06-DIA-BPM1 / SaX',
                'R1-06 / DIA / R1-06-DIA-BPM2 / SaX', 'R1-06 / DIA / R1-06-DIA-BPM3 / SaX',
                'R1-07 / DIA / R1-07-DIA-BPM1 / SaX', 'R1-07 / DIA / R1-07-DIA-BPM2 / SaX',
                'R1-07 / DIA / R1-07-DIA-BPM3 / SaX', 'R1-08 / DIA / R1-08-DIA-BPM1 / SaX',
                'R1-08 / DIA / R1-08-DIA-BPM2 / SaX', 'R1-08 / DIA / R1-08-DIA-BPM3 / SaX',
                'R1-09 / DIA / R1-09-DIA-BPM1 / SaX', 'R1-09 / DIA / R1-09-DIA-BPM2 / SaX',
                'R1-09 / DIA / R1-09-DIA-BPM3 / SaX', 'R1-10 / DIA / R1-10-DIA-BPM1 / SaX',
                'R1-10 / DIA / R1-10-DIA-BPM2 / SaX', 'R1-10 / DIA / R1-10-DIA-BPM3 / SaX',
                'R1-11 / DIA / R1-11-DIA-BPM1 / SaX', 'R1-11 / DIA / R1-11-DIA-BPM2 / SaX',
                'R1-11 / DIA / R1-11-DIA-BPM3 / SaX', 'R1-12 / DIA / R1-12-DIA-BPM1 / SaX',
                'R1-12 / DIA / R1-12-DIA-BPM2 / SaX', 'R1-12 / DIA / R1-12-DIA-BPM3 / SaX'
            )
            hw_2_physics_params = (1.,) * 36
            physics_2_hw_params = (1.,) * 36

    class BPMz:
        family_name = 'BPMz'
        family_type = 'BPM'
        member_of = ('PlotFamily', 'VBPM', 'BPM', 'Diagnostics')
        element_list = tuple(range(1, 1 + 36))
        status = [1,] * 36

        device_name = (
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
        )
        common_names = (
            '01BPMz01', '01BPMz02', '01BPMz03', '02BPMz01', '02BPMz02', '02BPMz03', '03BPMz01', '03BPMz02', '03BPMz03',
            '04BPMz01', '04BPMz02', '04BPMz03', '05BPMz01', '05BPMz02', '05BPMz03', '06BPMz01', '06BPMz02', '06BPMz03',
            '07BPMz01', '07BPMz02', '07BPMz03', '08BPMz01', '08BPMz02', '08BPMz03', '09BPMz01', '09BPMz02', '09BPMz03',
            '10BPMz01', '10BPMz02', '10BPMz03', '11BPMz01', '11BPMz02', '11BPMz03', '12BPMz01', '12BPMz02', '12BPMz03'
        )
        device_list = (
            (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (5, 1),
            (5, 2), (5, 3), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2),
            (9, 3), (10, 1), (10, 2), (10, 3), (11, 1), (11, 2), (11, 3), (12, 1), (12, 2), (12, 3)
        )
        offset = [
            -0.12755, -0.3681, -0.15165, 0.04733, 0.02625, 0.18839, 0.2534, -0.037393, -0.029, 0.277314, -0.02795,
            0.1549, 0.03785, 0.00945, -0.096996, -0.1163, -0.1356, 0.2629, -0.1686, 0.03125, 0.20235, 0.19535, 0.23915,
            0.38705, -0.21175, -0.23905, -0.12585, 0.072115, -0.0667, -0.0389, -0.4831, -0.11258, 0.1895, 0.13105,
            0.32275, 0.2886
        ]

        class Monitor:
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'mm'
            physics_units = 'mm'
            tango_names = (
                'R1-01 / DIA / R1-01-DIA-BPM1 / SaY', 'R1-01 / DIA / R1-01-DIA-BPM2 / SaY',
                'R1-01 / DIA / R1-01-DIA-BPM3 / SaY', 'R1-02 / DIA / R1-02-DIA-BPM1 / SaY',
                'R1-02 / DIA / R1-02-DIA-BPM2 / SaY', 'R1-02 / DIA / R1-02-DIA-BPM3 / SaY',
                'R1-03 / DIA / R1-03-DIA-BPM1 / SaY', 'R1-03 / DIA / R1-03-DIA-BPM2 / SaY',
                'R1-03 / DIA / R1-03-DIA-BPM3 / SaY', 'R1-04 / DIA / R1-04-DIA-BPM1 / SaY',
                'R1-04 / DIA / R1-04-DIA-BPM2 / SaY', 'R1-04 / DIA / R1-04-DIA-BPM3 / SaY',
                'R1-05 / DIA / R1-05-DIA-BPM1 / SaY', 'R1-05 / DIA / R1-05-DIA-BPM2 / SaY',
                'R1-05 / DIA / R1-05-DIA-BPM3 / SaY', 'R1-06 / DIA / R1-06-DIA-BPM1 / SaY',
                'R1-06 / DIA / R1-06-DIA-BPM2 / SaY', 'R1-06 / DIA / R1-06-DIA-BPM3 / SaY',
                'R1-07 / DIA / R1-07-DIA-BPM1 / SaY', 'R1-07 / DIA / R1-07-DIA-BPM2 / SaY',
                'R1-07 / DIA / R1-07-DIA-BPM3 / SaY', 'R1-08 / DIA / R1-08-DIA-BPM1 / SaY',
                'R1-08 / DIA / R1-08-DIA-BPM2 / SaY', 'R1-08 / DIA / R1-08-DIA-BPM3 / SaY',
                'R1-09 / DIA / R1-09-DIA-BPM1 / SaY', 'R1-09 / DIA / R1-09-DIA-BPM2 / SaY',
                'R1-09 / DIA / R1-09-DIA-BPM3 / SaY', 'R1-10 / DIA / R1-10-DIA-BPM1 / SaY',
                'R1-10 / DIA / R1-10-DIA-BPM2 / SaY', 'R1-10 / DIA / R1-10-DIA-BPM3 / SaY',
                'R1-11 / DIA / R1-11-DIA-BPM1 / SaY', 'R1-11 / DIA / R1-11-DIA-BPM2 / SaY',
                'R1-11 / DIA / R1-11-DIA-BPM3 / SaY', 'R1-12 / DIA / R1-12-DIA-BPM1 / SaY',
                'R1-12 / DIA / R1-12-DIA-BPM2 / SaY', 'R1-12 / DIA / R1-12-DIA-BPM3 / SaY'
            )
            hw_2_physics_params = (1.,) * 36
            physics_2_hw_params = (1.,) * 36

    class HCOR:
        family_name = 'HCOR'
        family_type = 'COR'
        member_of = ('HCOR', 'COR', 'HCM', 'Magnet')
        element_list = tuple(range(1, 1 + 48))

        status = [
            1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
            1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1
        ]
        device_name = (
            'R1-01 / MAG / R1-01-MAG-SCOCOX1', 'R1-01 / MAG / R1-01-MAG-SCICOX1', 'R1-01 / MAG / R1-01-MAG-SCICOX2',
            'R1-01 / MAG / R1-01-MAG-SCOCOX2', 'R1-02 / MAG / R1-02-MAG-SCOCOX1', 'R1-02 / MAG / R1-02-MAG-SCICOX1',
            'R1-02 / MAG / R1-02-MAG-SCICOX2', 'R1-02 / MAG / R1-02-MAG-SCOCOX2', 'R1-03 / MAG / R1-03-MAG-SCOCOX1',
            'R1-03 / MAG / R1-03-MAG-SCICOX1', 'R1-03 / MAG / R1-03-MAG-SCICOX2', 'R1-03 / MAG / R1-03-MAG-SCOCOX2',
            'R1-04 / MAG / R1-04-MAG-SCOCOX1', 'R1-04 / MAG / R1-04-MAG-SCICOX1', 'R1-04 / MAG / R1-04-MAG-SCICOX2',
            'R1-04 / MAG / R1-04-MAG-SCOCOX2', 'R1-05 / MAG / R1-05-MAG-SCOCOX1', 'R1-05 / MAG / R1-05-MAG-SCICOX1',
            'R1-05 / MAG / R1-05-MAG-SCICOX2', 'R1-05 / MAG / R1-05-MAG-SCOCOX2', 'R1-06 / MAG / R1-06-MAG-SCOCOX1',
            'R1-06 / MAG / R1-06-MAG-SCICOX1', 'R1-06 / MAG / R1-06-MAG-SCICOX2', 'R1-06 / MAG / R1-06-MAG-SCOCOX2',
            'R1-07 / MAG / R1-07-MAG-SCOCOX1', 'R1-07 / MAG / R1-07-MAG-SCICOX1', 'R1-07 / MAG / R1-07-MAG-SCICOX2',
            'R1-07 / MAG / R1-07-MAG-SCOCOX2', 'R1-08 / MAG / R1-08-MAG-SCOCOX1', 'R1-08 / MAG / R1-08-MAG-SCICOX1',
            'R1-08 / MAG / R1-08-MAG-SCICOX2', 'R1-08 / MAG / R1-08-MAG-SCOCOX2', 'R1-09 / MAG / R1-09-MAG-SCOCOX1',
            'R1-09 / MAG / R1-09-MAG-SCICOX1', 'R1-09 / MAG / R1-09-MAG-SCICOX2', 'R1-09 / MAG / R1-09-MAG-SCOCOX2',
            'R1-10 / MAG / R1-10-MAG-SCOCOX1', 'R1-10 / MAG / R1-10-MAG-SCICOX1', 'R1-10 / MAG / R1-10-MAG-SCICOX2',
            'R1-10 / MAG / R1-10-MAG-SCOCOX2', 'R1-11 / MAG / R1-11-MAG-SCOCOX1', 'R1-11 / MAG / R1-11-MAG-SCICOX1',
            'R1-11 / MAG / R1-11-MAG-SCICOX2', 'R1-11 / MAG / R1-11-MAG-SCOCOX2', 'R1-12 / MAG / R1-12-MAG-SCOCOX1',
            'R1-12 / MAG / R1-12-MAG-SCICOX1', 'R1-12 / MAG / R1-12-MAG-SCICOX2', 'R1-12 / MAG / R1-12-MAG-SCOCOX2'
        )
        circuit_name = (
            'R1-01 / MAG / R1-01-MAG-CRSCOCOX1', 'R1-01 / MAG / R1-01-MAG-CRSCICOX1',
            'R1-01 / MAG / R1-01-MAG-CRSCICOX2', 'R1-01 / MAG / R1-01-MAG-CRSCOCOX2',
            'R1-02 / MAG / R1-02-MAG-CRSCOCOX1', 'R1-02 / MAG / R1-02-MAG-CRSCICOX1',
            'R1-02 / MAG / R1-02-MAG-CRSCICOX2', 'R1-02 / MAG / R1-02-MAG-CRSCOCOX2',
            'R1-03 / MAG / R1-03-MAG-CRSCOCOX1', 'R1-03 / MAG / R1-03-MAG-CRSCICOX1',
            'R1-03 / MAG / R1-03-MAG-CRSCICOX2', 'R1-03 / MAG / R1-03-MAG-CRSCOCOX2',
            'R1-04 / MAG / R1-04-MAG-CRSCOCOX1', 'R1-04 / MAG / R1-04-MAG-CRSCICOX1',
            'R1-04 / MAG / R1-04-MAG-CRSCICOX2', 'R1-04 / MAG / R1-04-MAG-CRSCOCOX2',
            'R1-05 / MAG / R1-05-MAG-CRSCOCOX1', 'R1-05 / MAG / R1-05-MAG-CRSCICOX1',
            'R1-05 / MAG / R1-05-MAG-CRSCICOX2', 'R1-05 / MAG / R1-05-MAG-CRSCOCOX2',
            'R1-06 / MAG / R1-06-MAG-CRSCOCOX1', 'R1-06 / MAG / R1-06-MAG-CRSCICOX1',
            'R1-06 / MAG / R1-06-MAG-CRSCICOX2', 'R1-06 / MAG / R1-06-MAG-CRSCOCOX2',
            'R1-07 / MAG / R1-07-MAG-CRSCOCOX1', 'R1-07 / MAG / R1-07-MAG-CRSCICOX1',
            'R1-07 / MAG / R1-07-MAG-CRSCICOX2', 'R1-07 / MAG / R1-07-MAG-CRSCOCOX2',
            'R1-08 / MAG / R1-08-MAG-CRSCOCOX1', 'R1-08 / MAG / R1-08-MAG-CRSCICOX1',
            'R1-08 / MAG / R1-08-MAG-CRSCICOX2', 'R1-08 / MAG / R1-08-MAG-CRSCOCOX2',
            'R1-09 / MAG / R1-09-MAG-CRSCOCOX1', 'R1-09 / MAG / R1-09-MAG-CRSCICOX1',
            'R1-09 / MAG / R1-09-MAG-CRSCICOX2', 'R1-09 / MAG / R1-09-MAG-CRSCOCOX2',
            'R1-10 / MAG / R1-10-MAG-CRSCOCOX1', 'R1-10 / MAG / R1-10-MAG-CRSCICOX1',
            'R1-10 / MAG / R1-10-MAG-CRSCICOX2', 'R1-10 / MAG / R1-10-MAG-CRSCOCOX2',
            'R1-11 / MAG / R1-11-MAG-CRSCOCOX1', 'R1-11 / MAG / R1-11-MAG-CRSCICOX1',
            'R1-11 / MAG / R1-11-MAG-CRSCICOX2', 'R1-11 / MAG / R1-11-MAG-CRSCOCOX2',
            'R1-12 / MAG / R1-12-MAG-CRSCOCOX1', 'R1-12 / MAG / R1-12-MAG-CRSCICOX1',
            'R1-12 / MAG / R1-12-MAG-CRSCICOX2', 'R1-12 / MAG / R1-12-MAG-CRSCOCOX2'
        )
        power_supply_name = (
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
        )
        device_list = (
            (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1),
            (4, 2), (4, 3), (4, 4), (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4), (7, 1), (7, 2),
            (7, 3), (7, 4), (8, 1), (8, 2), (8, 3), (8, 4), (9, 1), (9, 2), (9, 3), (9, 4), (10, 1), (10, 2), (10, 3),
            (10, 4), (11, 1), (11, 2), (11, 3), (11, 4), (12, 1), (12, 2), (12, 3), (12, 4)
        )
        common_names = (
            '01HCM01', '01HCM02', '01HCM03', '01HCM04', '02HCM01', '02HCM02', '02HCM03', '02HCM04', '03HCM01',
            '03HCM02', '03HCM03', '03HCM04', '04HCM01', '04HCM02', '04HCM03', '04HCM04', '05HCM01', '05HCM02',
            '05HCM03', '05HCM04', '06HCM01', '06HCM02', '06HCM03', '06HCM04', '07HCM01', '07HCM02', '07HCM03',
            '07HCM04', '08HCM01', '08HCM02', '08HCM03', '08HCM04', '09HCM01', '09HCM02', '09HCM03', '09HCM04',
            '10HCM01', '10HCM02', '10HCM03', '10HCM04', '11HCM01', '11HCM02', '11HCM03', '11HCM04', '12HCM01',
            '12HCM02', '12HCM03', '12HCM04'
        )

        class Monitor:
            member_of = 'Plotfamily'
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'A'
            physics_units = 'radian'
            tango_names = (
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS01/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS13/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS02/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS03/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS14/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS04/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS05/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS15/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS06/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS01/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS13/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS02/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS03/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS14/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS04/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS05/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS15/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS06/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS01/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS13/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS02/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS03/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS14/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS04/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS05/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS15/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS06/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS05/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS20/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS06/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS07/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS21/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS08/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS09/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS22/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS10/Current'
            )
            hw_2_physics_params = ((0., 0., 0., 0., 0., 0., 0.000129717, 2.99849e-06),) * 48
            physics_2_hw_params = ((0., 0., 0., 0., 0., 0., 0.000129717, 2.99849e-06),) * 48

        class Setpoint:
            member_of = ('MachineConfig', 'Plotfamily')
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'A'
            physics_units = 'radian'
            tango_names = (
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS01/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS13/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS02/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS03/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS14/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS04/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS05/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS15/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS06/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS01/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS13/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS02/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS03/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS14/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS04/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS05/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS15/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS06/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS01/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS13/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS02/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS03/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS14/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS04/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS05/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS15/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS06/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS05/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS20/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS06/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS07/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS21/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS08/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS09/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS22/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS10/Current'
            )
            range = [[-11., 11.],] * 48
            tolerance = [1e-4,] * 48
            delta_resp_mat = [3.83541150899872,] * 48
            hw_2_physics_params = ((0., 0., 0., 0., 0., 0., 0.000129717, 2.99849e-06),) * 48
            physics_2_hw_params = ((0., 0., 0., 0., 0., 0., 0.000129717, 2.99849e-06),) * 48

    class VCOR:
        family_name = 'VCOR'
        family_type = 'COR'
        member_of = ('COR', 'VCOR', 'VCM', 'Magnet')
        element_list = tuple(range(1, 1 + 48))

        status = [
            1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
            1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1
        ]
        device_name = (
            'R1-01 / MAG / R1-01-MAG-SCOCOY1', 'R1-01 / MAG / R1-01-MAG-SCICOY1', 'R1-01 / MAG / R1-01-MAG-SCICOY2',
            'R1-01 / MAG / R1-01-MAG-SCOCOY2', 'R1-02 / MAG / R1-02-MAG-SCOCOY1', 'R1-02 / MAG / R1-02-MAG-SCICOY1',
            'R1-02 / MAG / R1-02-MAG-SCICOY2', 'R1-02 / MAG / R1-02-MAG-SCOCOY2', 'R1-03 / MAG / R1-03-MAG-SCOCOY1',
            'R1-03 / MAG / R1-03-MAG-SCICOY1', 'R1-03 / MAG / R1-03-MAG-SCICOY2', 'R1-03 / MAG / R1-03-MAG-SCOCOY2',
            'R1-04 / MAG / R1-04-MAG-SCOCOY1', 'R1-04 / MAG / R1-04-MAG-SCICOY1', 'R1-04 / MAG / R1-04-MAG-SCICOY2',
            'R1-04 / MAG / R1-04-MAG-SCOCOY2', 'R1-05 / MAG / R1-05-MAG-SCOCOY1', 'R1-05 / MAG / R1-05-MAG-SCICOY1',
            'R1-05 / MAG / R1-05-MAG-SCICOY2', 'R1-05 / MAG / R1-05-MAG-SCOCOY2', 'R1-06 / MAG / R1-06-MAG-SCOCOY1',
            'R1-06 / MAG / R1-06-MAG-SCICOY1', 'R1-06 / MAG / R1-06-MAG-SCICOY2', 'R1-06 / MAG / R1-06-MAG-SCOCOY2',
            'R1-07 / MAG / R1-07-MAG-SCOCOY1', 'R1-07 / MAG / R1-07-MAG-SCICOY1', 'R1-07 / MAG / R1-07-MAG-SCICOY2',
            'R1-07 / MAG / R1-07-MAG-SCOCOY2', 'R1-08 / MAG / R1-08-MAG-SCOCOY1', 'R1-08 / MAG / R1-08-MAG-SCICOY1',
            'R1-08 / MAG / R1-08-MAG-SCICOY2', 'R1-08 / MAG / R1-08-MAG-SCOCOY2', 'R1-09 / MAG / R1-09-MAG-SCOCOY1',
            'R1-09 / MAG / R1-09-MAG-SCICOY1', 'R1-09 / MAG / R1-09-MAG-SCICOY2', 'R1-09 / MAG / R1-09-MAG-SCOCOY2',
            'R1-10 / MAG / R1-10-MAG-SCOCOY1', 'R1-10 / MAG / R1-10-MAG-SCICOY1', 'R1-10 / MAG / R1-10-MAG-SCICOY2',
            'R1-10 / MAG / R1-10-MAG-SCOCOY2', 'R1-11 / MAG / R1-11-MAG-SCOCOY1', 'R1-11 / MAG / R1-11-MAG-SCICOY1',
            'R1-11 / MAG / R1-11-MAG-SCICOY2', 'R1-11 / MAG / R1-11-MAG-SCOCOY2', 'R1-12 / MAG / R1-12-MAG-SCOCOY1',
            'R1-12 / MAG / R1-12-MAG-SCICOY1', 'R1-12 / MAG / R1-12-MAG-SCICOY2', 'R1-12 / MAG / R1-12-MAG-SCOCOY2'
        )
        circuit_name = (
            'R1-01 / MAG / R1-01-MAG-CRSCOCOY1', 'R1-01 / MAG / R1-01-MAG-CRSCICOY1',
            'R1-01 / MAG / R1-01-MAG-CRSCICOY2', 'R1-01 / MAG / R1-01-MAG-CRSCOCOY2',
            'R1-02 / MAG / R1-02-MAG-CRSCOCOY1', 'R1-02 / MAG / R1-02-MAG-CRSCICOY1',
            'R1-02 / MAG / R1-02-MAG-CRSCICOY2', 'R1-02 / MAG / R1-02-MAG-CRSCOCOY2',
            'R1-03 / MAG / R1-03-MAG-CRSCOCOY1', 'R1-03 / MAG / R1-03-MAG-CRSCICOY1',
            'R1-03 / MAG / R1-03-MAG-CRSCICOY2', 'R1-03 / MAG / R1-03-MAG-CRSCOCOY2',
            'R1-04 / MAG / R1-04-MAG-CRSCOCOY1', 'R1-04 / MAG / R1-04-MAG-CRSCICOY1',
            'R1-04 / MAG / R1-04-MAG-CRSCICOY2', 'R1-04 / MAG / R1-04-MAG-CRSCOCOY2',
            'R1-05 / MAG / R1-05-MAG-CRSCOCOY1', 'R1-05 / MAG / R1-05-MAG-CRSCICOY1',
            'R1-05 / MAG / R1-05-MAG-CRSCICOY2', 'R1-05 / MAG / R1-05-MAG-CRSCOCOY2',
            'R1-06 / MAG / R1-06-MAG-CRSCOCOY1', 'R1-06 / MAG / R1-06-MAG-CRSCICOY1',
            'R1-06 / MAG / R1-06-MAG-CRSCICOY2', 'R1-06 / MAG / R1-06-MAG-CRSCOCOY2',
            'R1-07 / MAG / R1-07-MAG-CRSCOCOY1', 'R1-07 / MAG / R1-07-MAG-CRSCICOY1',
            'R1-07 / MAG / R1-07-MAG-CRSCICOY2', 'R1-07 / MAG / R1-07-MAG-CRSCOCOY2',
            'R1-08 / MAG / R1-08-MAG-CRSCOCOY1', 'R1-08 / MAG / R1-08-MAG-CRSCICOY1',
            'R1-08 / MAG / R1-08-MAG-CRSCICOY2', 'R1-08 / MAG / R1-08-MAG-CRSCOCOY2',
            'R1-09 / MAG / R1-09-MAG-CRSCOCOY1', 'R1-09 / MAG / R1-09-MAG-CRSCICOY1',
            'R1-09 / MAG / R1-09-MAG-CRSCICOY2', 'R1-09 / MAG / R1-09-MAG-CRSCOCOY2',
            'R1-10 / MAG / R1-10-MAG-CRSCOCOY1', 'R1-10 / MAG / R1-10-MAG-CRSCICOY1',
            'R1-10 / MAG / R1-10-MAG-CRSCICOY2', 'R1-10 / MAG / R1-10-MAG-CRSCOCOY2',
            'R1-11 / MAG / R1-11-MAG-CRSCOCOY1', 'R1-11 / MAG / R1-11-MAG-CRSCICOY1',
            'R1-11 / MAG / R1-11-MAG-CRSCICOY2', 'R1-11 / MAG / R1-11-MAG-CRSCOCOY2',
            'R1-12 / MAG / R1-12-MAG-CRSCOCOY1', 'R1-12 / MAG / R1-12-MAG-CRSCICOY1',
            'R1-12 / MAG / R1-12-MAG-CRSCICOY2', 'R1-12 / MAG / R1-12-MAG-CRSCOCOY2'
        )
        power_supply_name = (
            'R1-SGA/MAG/R1-SGACAB14-MAG-PS07', '', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS16', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS08',
            'R1-SGA/MAG/R1-SGACAB14-MAG-PS09', '', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS17', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS10',
            'R1-SGA/MAG/R1-SGACAB14-MAG-PS11', '', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS18', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS12',
            'R1-SGB/MAG/R1-SGBCAB06-MAG-PS07', '', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS16', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS08',
            'R1-SGB/MAG/R1-SGBCAB06-MAG-PS09', '', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS17', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS10',
            'R1-SGB/MAG/R1-SGBCAB06-MAG-PS11', '', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS18', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS12',
            'R1-SGC/MAG/R1-SGCCAB12-MAG-PS07', '', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS16', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS08',
            'R1-SGC/MAG/R1-SGCCAB12-MAG-PS09', '', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS17', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS10',
            'R1-SGC/MAG/R1-SGCCAB12-MAG-PS11', '', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS18', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS12',
            'R1-SGD/MAG/R1-SGDCAB02-MAG-PS11', '', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS23', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS12',
            'R1-SGD/MAG/R1-SGDCAB02-MAG-PS13', '', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS24', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS14',
            'R1-SGD/MAG/R1-SGDCAB02-MAG-PS15', '', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS25', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS16'
        )
        device_list = (
            (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1),
            (4, 2), (4, 3), (4, 4), (5, 1), (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4), (7, 1), (7, 2),
            (7, 3), (7, 4), (8, 1), (8, 2), (8, 3), (8, 4), (9, 1), (9, 2), (9, 3), (9, 4), (10, 1), (10, 2), (10, 3),
            (10, 4), (11, 1), (11, 2), (11, 3), (11, 4), (12, 1), (12, 2), (12, 3), (12, 4)
        )
        common_names = (
            '01VCM01', '01VCM02', '01VCM03', '01VCM04', '02VCM01', '02VCM02', '02VCM03', '02VCM04', '03VCM01',
            '03VCM02', '03VCM03', '03VCM04', '04VCM01', '04VCM02', '04VCM03', '04VCM04', '05VCM01', '05VCM02',
            '05VCM03', '05VCM04', '06VCM01', '06VCM02', '06VCM03', '06VCM04', '07VCM01', '07VCM02', '07VCM03',
            '07VCM04', '08VCM01', '08VCM02', '08VCM03', '08VCM04', '09VCM01', '09VCM02', '09VCM03', '09VCM04',
            '10VCM01', '10VCM02', '10VCM03', '10VCM04', '11VCM01', '11VCM02', '11VCM03', '11VCM04', '12VCM01',
            '12VCM02', '12VCM03', '12VCM04'
        )

        class Monitor:
            member_of = 'Plotfamily'
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'A'
            physics_units = 'radian'

            tango_names = (
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS07/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS16/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS08/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS09/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS17/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS10/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS11/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS18/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS12/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS07/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS16/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS08/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS09/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS17/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS10/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS11/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS18/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS12/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS07/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS16/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS08/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS09/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS17/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS10/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS11/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS18/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS12/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS11/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS23/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS12/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS13/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS24/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS14/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS15/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS25/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS16/Current'
            )
            hw_2_physics_params = ((0., 0., 0., 0., 0., 0., 0.000109051, 7.77688e-06),) * 48
            physics_2_hw_params = ((0., 0., 0., 0., 0., 0., 0.000109051, 7.77688e-06),) * 48

        class Setpoint:
            member_of = ('MachineConfig', 'Plotfamily')
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'A'
            physics_units = 'radian'

            tango_names = (
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS07/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS16/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS08/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS09/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS17/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS10/Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS11/Current', '                               /Current',
                'R1-SGA/MAG/R1-SGACAB14-MAG-PS18/Current', 'R1-SGA/MAG/R1-SGACAB14-MAG-PS12/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS07/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS16/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS08/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS09/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS17/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS10/Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS11/Current', '                               /Current',
                'R1-SGB/MAG/R1-SGBCAB06-MAG-PS18/Current', 'R1-SGB/MAG/R1-SGBCAB06-MAG-PS12/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS07/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS16/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS08/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS09/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS17/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS10/Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS11/Current', '                               /Current',
                'R1-SGC/MAG/R1-SGCCAB12-MAG-PS18/Current', 'R1-SGC/MAG/R1-SGCCAB12-MAG-PS12/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS11/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS23/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS12/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS13/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS24/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS14/Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS15/Current', '                               /Current',
                'R1-SGD/MAG/R1-SGDCAB02-MAG-PS25/Current', 'R1-SGD/MAG/R1-SGDCAB02-MAG-PS16/Current'
            )
            range = [[-11., 11.], ] * 48
            tolerance = [1e-5, ] * 48
            delta_resp_mat = [4.51843343676617, ] * 48
            hw_2_physics_params = ((0., 0., 0., 0., 0., 0., 0.000109051, 7.77688e-06),) * 48
            physics_2_hw_params = ((0., 0., 0., 0., 0., 0., 0.000109051, 7.77688e-06),) * 48

    class DCCT:
        family_name = 'DCCT'
        member_of = 'DCCT'
        element_list = 1
        status = 1
        device_list = (1, 1)
        device_name = 'R1-ALL/DIA/R1-ALL-DIA-BIM1'
        common_names = 'DCCT'

        class Monitor:
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'A'
            physics_units = 'mA'
            tango_names = 'R1-ALL/DIA/R1-ALL-DIA-BIM1/BeamCurrent'

            hw_2_physics_params = 1000.
            physics_2_hw_params = 1e-3

    class RF:
        family_name = 'RF'
        member_of = ('RF', 'RFSystem')
        element_list = 1
        status = 1
        device_list = (1, 1)
        device_name = 'R1-SGD/CTL/R1-SGDCAB10-RF-SIG1/'
        common_names = 'RF'
        position = 88.

        class Monitor:
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'Hz'
            physics_units = 'MHz'
            tango_names = 'R1-SGD/CTL/R1-SGDCAB10-RF-SIG1/Frequency'

            hw_2_physics_params = 1e-6
            physics_2_hw_params = 1e6
            range = [99900000., 100000000.]

        class Setpoint:
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'Hz'
            physics_units = 'MHz'
            tango_names = 'R1-SGD/CTL/R1-SGDCAB10-RF-SIG1/Frequency'

            hw_2_physics_params = 1e-6
            physics_2_hw_params = 1e6
            range = [99900000., 100000000.]

        class Desired:
            mode = 'Online'
            units = 'Hardware'
            hw_units = 'Hz'
            physics_units = 'MHz'
            tango_names = 'R1-SGD/CTL/R1-SGDCAB10-RF-SIG1/Frequency'

            hw_2_physics_params = 1e-6
            physics_2_hw_params = 1e6
            range = [99900000., 100000000.]
