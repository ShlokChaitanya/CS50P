import pytest
from jar import Jar

def testInitDefault():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def testInitCustom():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

def testDeposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

def testWithdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
