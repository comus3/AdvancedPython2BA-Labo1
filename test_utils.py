import pytest
import utils
import math

def test_fact():
    assert utils.fact(5) == 120
    assert utils.fact(6) == 720


def test_roots():
    assert all(utils.roots(1,4,4) == [-2,-2])

def test_integrate():
    assert abs(utils.integrate("x*((math.e)**x)",0,1)-(((2*((math.e)**3)+1))/9))<0.001
    


