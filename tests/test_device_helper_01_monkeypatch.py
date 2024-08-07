import pytest
from pytest import MonkeyPatch

from awesome_code.devices import DeviceType, NotConnected
from awesome_code.device_helper import DeviceHelper


"""
Using monkeypatch fixture (pytest built-in)
"""


def test_device_helper_init_hostname(cat9k24: DeviceType):
    dh = DeviceHelper("sw01", cat9k24)
    assert dh.hostname == "sw01"


@pytest.mark.xfail(reason="Use monkeypatch fix this test")
def test_device_helper_init_user_env(cat9k24: DeviceType, monkeypatch: MonkeyPatch):

    # TODO: Use mokeypatch to set the environment variable

    dh = DeviceHelper("sw01", cat9k24)
    assert dh.user == "TestingUser"


@pytest.mark.xfail(reason="Use monkeypatch fix this test")
def test_device_helper_init_password_env(cat9k24: DeviceType, monkeypatch: MonkeyPatch):

    # TODO: Use mokeypatch to set the environment variable

    dh = DeviceHelper("sw01", cat9k24)
    assert dh.password == "TestingPassword"


def test_device_helper_init_user(cat9k24: DeviceType):
    dh = DeviceHelper("sw01", cat9k24)
    assert dh.user == "vendor"


def test_device_helper_init_password(cat9k24: DeviceType):
    dh = DeviceHelper("sw01", cat9k24)
    assert dh.password == "vendor"


def test_device_helper_not_connected_error(cat9k24: DeviceType):
    dh = DeviceHelper("sw01", cat9k24)
    with pytest.raises(NotConnected):
        dh.device.cli("test")


@pytest.mark.xfail(reason="Use monkeypatch fix this test", run=False)
def test_device_helper_awesome_workflow_monkeypatch(
    cat9k24: DeviceType, monkeypatch: MonkeyPatch
):
    expected_result = {
        "show user": "Fake response for show user",
        "show a": "Fake response for show a",
        "show b": "Fake response for show b",
        "show c": "Fake response for show c",
        "do xyz": "Fake response for do xyz",
    }

    dh = DeviceHelper("sw01", cat9k24)
    do_nothing = lambda: None
    cli = lambda x: {y: f"Fake response for {y}" for y in x}

    # TODO: Use monekypatch to patch the `dh.device` object
    # Hint: You can use the `do_nothing` and `cli` lambda's.

    result = dh.awesome_workflow()

    assert result == expected_result
