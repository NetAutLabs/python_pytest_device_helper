---
tags:
  - pytest
  - beginner
  - codespaces
---

# Testing DeviceHelper with PyTest


|             |                                                                                                       |
| ----------: | :-----------------------------------------------------------------------------------------------------|
| Level       | beginner                                                                                              |
| Repo        | [https://github.com/NetAutLabs/<repo name>](https://github.com/NetAutLabs/python_pytest_device_helper)|
| Discussion  | [Discussion GitHub Repo](https://github.com/NetAutLabs/python_pytest_device_helper/discussions)       |
| Codespaces  | :material-check: [GitHub Codespaces](https://codespaces.new/NetAutLabs/python_pytest_device_helper)   |


## Lab Goal

The goal of this lab is to learn and understand the differences between three testing approaches: ["monkey patching"](https://docs.pytest.org/en/stable/how-to/monkeypatch.html), using [`pytest-mock`](https://pytest-mock.readthedocs.io/en/stable/), and creating "fake objects". You will work on a Python project with five test files, but only the three mentioned below contain TODOs that need fixing.

### Objectives:
1. **Monkey Patching**:
   
   - Explore how to dynamically modify or replace methods and attributes in your code during runtime.
   - Complete the TODOs in `tests/test_device_helper_01_monkeypatch.py`.

2. **pytest-mock**:
   
   - Learn how to use the `pytest-mock` library to create and manage mock objects.
   - Discover how mocking can help isolate the code under test and verify interactions.
   - Complete the TODOs in `tests/test_device_helper_02_mock.py`.

3. **Fake Objects**:
   
   - Implement fake objects that provide simplified, yet working, implementations of dependencies.
   - Recognize when and why to use fake objects over mocks or monkey patching.
   - Complete the TODOs in `tests/test_device_helper_03_fakedevice.py`.

### Additional Information:

- The test files are located in the `tests` directory, but only `tests/test_device_helper_01_monkeypatch.py`, `tests/test_device_helper_02_mock.py`, and `tests/test_device_helper_03_fakedevice.py` contain TODOs that require your attention.
- These tests are marked with `xfail` to indicate that they are expected to fail. After you implement the necessary changes, remove the `xfail` markers.
- To run and check the tests, use the following command:
  
  ```sh
  python3 -m pytest
  ```

- Test execution needs to be under one second.
