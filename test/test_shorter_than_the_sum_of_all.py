"""
Each side must be shorter than the sum of all sides divided by 2;
"""

import pytest
from main import Triangulo

def test_shorter_than_the_sum_of_all ():
    
    a = Triangulo (1,1,1)
    b = Triangulo (-5, 2, 1000)
    c = Triangulo (1, 1, 1000)
    d = Triangulo (50, 10, 30)
    e = Triangulo (40, 50, 40)
    
    assert a.identify_triangule() == None
    assert b.identify_triangule() == 'Isnt triangle cuz Each side must be shorter than the sum of all sides divided by 2'
    assert c.identify_triangule() == 'Isnt triangle cuz Each side must be shorter than the sum of all sides divided by 2'
    assert d.identify_triangule() == 'Isnt triangle cuz Each side must be shorter than the sum of all sides divided by 2' 
    assert e.identify_triangule() == None
  