"""
- No side may have a length of zero
"""

import pytest
from main import Triangulo


def test_no_lenght_of_zero ():
    
    a = Triangulo(1,1,0)
    b = Triangulo(1,0,1)
    c = Triangulo(0,1,1)
    d = Triangulo(0,0,1)
    e = Triangulo(1,0,0)
    f = Triangulo(0,0,0)
    g = Triangulo(1,1,1)
    
    assert a.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    assert b.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    assert c.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    assert d.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    assert e.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    assert f.identify_triangule() == 'Isnt triangle cuz No side may have a length of zero'
    assert g.identify_triangule() == None

    