"""
triangular inequality
"""

import pytest
from main import Triangulo

def test_triangular_inequality_1 ():
    
    a = Triangulo(1,1,1)
    assert a.identify_triangule() == None
    
def test_triangular_inequality_2 ():
    
    b = Triangulo(1,2,1)
    assert b.identify_triangule() == 'Isnt triangle cuz the sum of any two sides must be greater than the length of the third side' 
    
def test_triangular_inequality_3 ():
    
    c = Triangulo(10,10,20)
    assert c.identify_triangule() == 'Isnt triangle cuz the sum of any two sides must be greater than the length of the third side' 
    
def test_triangular_inequality_4 ():
    
    d = Triangulo(5, 4, 7)
    assert d.identify_triangule() == None