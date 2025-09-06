#critical test case - payroll, leave, attandance
#normal test case - login, register, employee managment,
#low priority test case
import sys

import pytest

@pytest.mark.critical
def test_payroll():
    assert True

@pytest.mark.critical
def test_leave():
    assert True

@pytest.mark.critical
def test_attendance():
    assert True

@pytest.mark.normal
def test_login():
    assert True

@pytest.mark.normal
def test_register():
    assert True
    print("***********************************")

@pytest.mark.noncritical
def test_buzz():
    assert True
    print("***********************************")
