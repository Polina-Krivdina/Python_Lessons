import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.positive_test
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4,  5)
    assert res == 9

def test_sum_negativ_nums():
    calculator = Calculator()
    res = calculator.sum(-6,  -10)
    assert res == -16

def test_sum_negativ_and_positive_nums():
    calculator = Calculator()
    res = calculator.sum(-6,  6)
    assert res == 0

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(3.5, 6.4)
    res = round(res, 1)
    assert res == 9.9

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(5, 0)
    assert res == 5

@pytest.mark.positive_test
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)

def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

@pytest.mark.positive_test
def test_avg_positive():
    calculator = Calculator()
    numbers = [1,2,3,4,5,6,7,8,9,5]
    res = calculator.avg(numbers)
    assert res == 5