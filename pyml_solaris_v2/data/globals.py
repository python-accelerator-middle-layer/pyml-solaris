"""
Module for defining accelerators elements
"""

import sys

import numpy as np

from typing import Sequence, Tuple, Optional, Union

from tango import DeviceProxy, DevFailed


ParamTypes = Optional[Union[float, Sequence[float]]]


class Device:
    """Extension class to DeviceProxy"""

    def __init__(self, family_name: str, proxy: DeviceProxy,
                 element_id: int, device_id: Tuple[int, int],):
        """

        :param family_name: Name of the element group
        :param proxy: DeviceProxy object of a device
        :param element_id: single number ID of a device
        :param device_id: paired number ID of a device
        """
        self.family_name = family_name
        self.proxy = proxy
        self.device_id = device_id
        self.element_id = element_id

        self._offset = 0.
        self._default_monitor = ''
        self._default_setpoint = ''
        self._setpoint_range = (0, 0)

    def __repr__(self):
        return f'{self.family_name} {type(self).__name__}{self.device_id}'

    def monitor(self, *, offset=False) -> float:
        """Returns value of monitor attribute"""
        if not self._default_monitor:
            raise AttributeError("Monitor attribute is not set")

        value = self.proxy.read_attribute(self._default_monitor).value

        if offset:
            value -= self._offset

        return value

    def setpoint(self, value: float):
        """Sets value of setpoint attribute"""
        if not self._default_setpoint:
            raise AttributeError("Setpoint attribute is not set")

        if self._setpoint_range[0] < value < self._setpoint_range[1]:
            self.proxy.write_attribute(self._default_setpoint, value)
        else:
            raise ValueError(
                f"Given value exceeds permitted range {self._setpoint_range}")

    def read_attribute_value(self, attribute: str):
        """Returns value of given attribute"""
        return self.proxy.read_attribute(attribute).value


class Family:
    """Base class for defining all device families"""

    def __init__(self, family_name: str, device_names: Union[str, Sequence[str]]):
        """
        :param family_name: Name of the element group
        :param device_names: TANGO addresses of elements
        """

        self.family_name = family_name
        self.device_names = (device_names,) if isinstance(device_names, str) \
            else device_names

        # Build a tuple of Device objects
        sections = AcceleratorObjects.machine_data["sections"]
        self.devices = self._build_device_objects(sections)
        self.elements_in_section = -(-len(self) // sections)    # Rounded up

        # Initialise unit parameters
        self.hw_units = ''
        self.physics_units = ''
        self.hw2physics_param = 1

    def __repr__(self) -> str:
        repr_str = f'{self.family_name} {type(self).__name__} of {len(self)} device'
        if len(self) != 1:
            repr_str += 's'
        return repr_str

    def __len__(self) -> int:
        return len(self.devices)

    def __iter__(self):
        return iter(self.devices)

    def __getitem__(self, index: int) -> Union[Device, Tuple[Device, ...]]:
        return self.devices[index]

    def __call__(self, section, device) -> Device:
        index = (section - 1) * self.elements_in_section + device - 1
        return self.devices[index]

    @property
    def element_list(self):
        return tuple(device.element_id for device in self)

    @property
    def device_list(self):
        return tuple(device.device_id for device in self)

    def set_default_monitor(self, attribute: str):
        """Sets attribute that will be referenced by monitor() calls by default"""
        for device in self:
            device._default_monitor = attribute

    def set_default_setpoint(self, attribute: str, setpoint_range: Tuple[float, float]):
        """Sets attribute that will be referenced by setpoint() calls by default"""
        for device in self:
            device._default_setpoint = attribute
            device._setpoint_range = setpoint_range

    def monitor(self, *, offset=False) -> np.ndarray:
        """Returns value of monitor attribute from all devices"""
        values = tuple(device.monitor(offset=offset) for device in self)
        return np.array(values)

    def setpoint(self, values: Union[float, Sequence[float]]):
        """Sets value of setpoint attribute on all devices"""
        try:
            # Check if input is iterable
            iter(values)

            # Verify length
            if len(values) != len(self):
                raise ValueError(f"Expected a sequence of length {len(self)} or a float, "
                                 f"but got a sequence of length {len(values)}.")

            # Write attributes
            for device, value in zip(self, values):
                device.setpoint(value)

        except TypeError:   # This suggests only a float was given
            for device in self:
                device.setpoint(values)

    # TODO? method for generating common names

    def set_offsets(self, offsets: Sequence[float]):
        if len(offsets) != len(self):
            raise ValueError(f"Expected a sequence of length {len(self)}, "
                             f"but got a sequence of length {len(offsets)}.")

        for device, offset in zip(self, offsets):
            device._offset = offset

    def set_units(self, hw_units: Optional[str] = '', phys_units: Optional[str] = '',
                  converter_param: ParamTypes = 1):
        """
        Sets or resets units.
        If only one argument is provided, it is assumed hardware and physics units
        are the same.
        Calling method with no arguments removes units
        """
        self.hw_units = hw_units
        self.physics_units = phys_units if phys_units else hw_units
        self.hw2physics_param = converter_param

    def _build_device_objects(self, sections: int) -> Tuple[Device, ...]:
        """
        Builds a tuple of Device objects
        """

        # Create DeviceProxy objects
        device_proxies = self._proxy_devices()

        # Build element lists
        if len(device_proxies) == 1:
            device_list = ((1, 1),)
            element_list = (0,)
        else:
            device_list = tuple(
                (sec, elem) for sec in range(1, 1 + sections)
                for elem in range(1, 1 + len(device_proxies) // sections)
            )
            element_list = tuple(range(0, len(device_proxies)))

        # Build list of Device objects
        devices = []
        for proxy, elem, dev in zip(device_proxies, element_list, device_list):
            devices.append(Device(self.family_name, proxy, elem, dev))

        return tuple(devices)

    def _proxy_devices(self) -> Tuple[DeviceProxy, ...]:
        """
        Creates DeviceProxy object for each given correct device address.
        Could be moved outside for easier control system switching
        """
        devices = []
        for dev in self.device_names:
            try:
                devices.append(DeviceProxy(dev))
            except DevFailed:
                pass

        return tuple(devices)


class AcceleratorObjects:
    """Dataclass for storing general information about machine"""

    machine_data = None
    directories = None
    default_names = None
    _families = {}

    def __len__(self):
        return len(self._families)

    def __repr__(self):
        return f'AcceleratorObjects instance containing {len(self)} Families'

    def __getattr__(self, name):        # TODO: verify if it's necessary on python 3.6
        """"""
        if name in self._families:
            return self._families[name]
        raise AttributeError(f"{type(self).__name__} has no Family named '{name}'")

    @classmethod
    def add_family(cls, name, addresses):
        """"""
        if hasattr(cls, name):
            raise ValueError(f"Family name '{name}' conflicts with an existing attribute")

        cls._families[name] = Family(name, addresses)
        setattr(cls, name, cls._families[name])
