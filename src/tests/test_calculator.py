"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message
def test_addition():
    assert Calculator().addition(2, 3) == 5
def test_subtraction():
    assert Calculator().subtraction(5, 3) == 2
def test_multiplication():
    assert Calculator().multiplication(4, 3) == 12
def test_division():
    assert Calculator().division(10, 2) == 5
    
