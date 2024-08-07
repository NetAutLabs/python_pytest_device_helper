from awesome_code.devices import PortRange


def test_access_port_len(cat9k24_access: PortRange):
    assert len(cat9k24_access.get_ports()) == 24


def test_access_port(cat9k24_access: PortRange):
    ports = cat9k24_access.get_ports()
    assert ports[0] == "GigabitEthernet1/0/1"
    assert ports[-1] == "GigabitEthernet1/0/24"


def test_uplink_port_len(cat9k24_uplink: PortRange):
    assert len(cat9k24_uplink.get_ports()) == 8


def test_uplink_port(cat9k24_uplink: PortRange):
    ports = cat9k24_uplink.get_ports()
    assert ports[0] == "TenGigEthernet1/1/1"
    assert ports[-1] == "TenGigEthernet1/1/8"


def test_stack_access_port_len(cat9k24_stack_ports: PortRange):
    assert len(cat9k24_stack_ports.get_ports()) == 4 * 24


def test_stack_access_port(cat9k24_stack_ports: PortRange):
    ports = cat9k24_stack_ports.get_ports()
    assert ports[0] == "GigabitEthernet1/0/1"
    assert ports[-1] == "GigabitEthernet4/0/24"


def test_big_switch():
    assert (
        len(PortRange("Eth", range(1, 9), range(1, 5), range(1, 49)).get_ports())
        == 8 * 4 * 48
    )
