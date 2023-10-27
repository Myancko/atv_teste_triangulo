"""
Each side must be shorter than the sum of all sides divided by 2;
"""

import pytest
from main import Triangulo

def test_shorter_than_the_sum_of_all_1 ():
    
    a = Triangulo (1,1,1)
    assert a.identify_triangule() == None  
  
def test_shorter_than_the_sum_of_all_2 ():
    
    b = Triangulo (-5, 2, 1000)
    assert b.identify_triangule() == 'Isnt triangle cuz Each side must be shorter than the sum of all sides divided by 2'
    
def test_shorter_than_the_sum_of_all_3 ():
    
    c = Triangulo (1, 1, 1000)
    assert c.identify_triangule() == 'Isnt triangle cuz Each side must be shorter than the sum of all sides divided by 2'
    
def test_shorter_than_the_sum_of_all_4 ():
    
    d = Triangulo (50, 10, 30)
    assert d.identify_triangule() == 'Isnt triangle cuz Each side must be shorter than the sum of all sides divided by 2' 
    
def test_shorter_than_the_sum_of_all_5 ():
    
    e = Triangulo (40, 50, 40)
    assert e.identify_triangule() == None 