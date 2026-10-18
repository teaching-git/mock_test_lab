from unittest.mock import Mock
from tax import TaxService

def add_tax(amount):
    return amount * 1.07

def test_tax_calculation():
    calculator = Mock()
    calculator.calculate.side_effect = add_tax
    service = TaxService(calculator)
    assert service.total(100) == 107
