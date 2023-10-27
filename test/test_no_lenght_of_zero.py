"""
No side may have a length of zero
"""

import pytest
from main import Triangulo


def test_no_lenght_of_zero_1 ():
    
    a = Triangulo(1,1,0)
    assert a.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    

def test_no_lenght_of_zero_2 ():
    
    b = Triangulo(1,0,1)
    assert b.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    
def test_no_lenght_of_zero_3 ():
    
    c = Triangulo(0,1,1)
    assert c.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'

def test_no_lenght_of_zero_4 ():

    d = Triangulo(0,0,1)
    assert d.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    
def test_no_lenght_of_zero_5 ():
    
    e = Triangulo(1,0,0)
    assert e.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'

def test_no_lenght_of_zero_6 ():
    
    f = Triangulo(0,0,0)
    assert f.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'

def test_no_lenght_of_zero_7 (): 

    g = Triangulo(1,1,1)
    assert g.identify_triangule() == None    