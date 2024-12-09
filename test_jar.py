from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-3)
    with pytest.raises(ValueError):
        Jar(3.5)

def test_deposit():
    jar = Jar(5)
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        Jar.withdraw(2)

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert jar.__str__() == 3 * "\N{Cookie}"








