class TaxService:
    def __init__(self, calculator):
        self.calculator = calculator

    def total(self, amount):
        return self.calculator.calculate(amount)
