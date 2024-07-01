# pyml_solaris
A package built in order to perform LOCO measurements in NCSR SOLARIS. It is more or less direct port from MATLAB.
It contains necessary measurement scripts (measure_dispersion, measure_bpm_response, monitor_bpm), as well as 
measure_loco_data which binds them together

### WORK IN PROGRESS
At this point in time (01.07.2024) package is not fully tested online. It is also not configurable for other machines,
unless data is rewritten by hand, so current solution of passing AcceleratorData object will have to be heavily modified