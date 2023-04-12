import pytest
from employee import Employee


@pytest.fixture
def employee():
    """An employee object that will be available in all test"""
    employee = Employee('Oluwanifemi', 'Obadina', 200_000)
    return employee

def test_give_default_raise(employee):
    """Test that default raise works correctly"""
    employee.give_raise()
    assert employee.annual_salary == 205_000

def test_give_custom_raise(employee):
    """Test that custom raise works correctly"""
    employee.give_raise(10_000)
    assert employee.annual_salary == 210_000

 