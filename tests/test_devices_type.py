from awesome_code.devices import DeviceType


def test_access_port_len(cat9k24: DeviceType):
    assert len(cat9k24.total_access_ports()) == 24


def test_access_port(cat9k24: DeviceType):
    ports = cat9k24.total_access_ports()
    assert ports[0] == "GigabitEthernet1/0/1"
    assert ports[-1] == "GigabitEthernet1/0/24"


def test_uplink_port_len(cat9k24: DeviceType):
    assert len(cat9k24.total_uplink_ports()) == 8


def test_uplink_port(cat9k24: DeviceType):
    ports = cat9k24.total_uplink_ports()
    assert ports[0] == "TenGigEthernet1/1/1"
    assert ports[-1] == "TenGigEthernet1/1/8"


def test_stack_access_port_len(cat9k48_stack: DeviceType):
    assert len(cat9k48_stack.total_access_ports()) == 240


def test_stack_access_port(cat9k48_stack: DeviceType):
    ports = cat9k48_stack.total_access_ports()
    assert ports[0] == "GigabitEthernet1/0/1"
    assert ports[-1] == "GigabitEthernet4/1/12"


def test_stack_uplink_port_len(cat9k48_stack: DeviceType):
    assert len(cat9k48_stack.total_uplink_ports()) == 40


def test_stack_uplink_port(cat9k48_stack: DeviceType):
    ports = cat9k48_stack.total_uplink_ports()
    assert ports[0] == "TenGigEthernet1/1/1"
    assert ports[-1] == "FortyGigabitEthernet4/1/2"
