# pyml_solaris_v2

A package built in order to perform LOCO measurements in NCSR SOLARIS. It is more or less direct port from MATLAB. It contains necessary measurement scripts (measure_dispersion, measure_bpm_response, monitor_bpm), as well as measure_loco_data which binds them together.

Version 2 is a complete overhaul, while still based on MML it heavily leverages Python's object oriented capabilities. Completely new AcceleratorObjects class allows for easy accomodation for different facilities.

Code should work on Python 3.6 and higher.
Data acquisition is pyTango-based, implementing other control systems would require some modifications.

AcceleratorObjects is accessed through context.py module, changing lattice requires writing initialisation script and placing it as source for import inside context.py.

WORK IN PROGRESS
