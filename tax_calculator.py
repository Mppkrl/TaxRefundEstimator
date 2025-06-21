class Tax_calculator:

    def __init__(self,gross_income,tax_withheld):
        self.gross_income = gross_income
        self.tax_withheld = tax_withheld


    def tax_payable(self):
        income = self.gross_income
        if income < 18200:
           return  0
        elif income <= 45000:
           return  (income - 18200) * 0.19
        elif income <= 120000:
           return  (income - 45000) *0.325 + 5092
        elif income <= 180000:
           return  (income - 120000) * 0.37 + 29467
        else:
           return  (income - 180000) * 0.45 + 51667
        
    def medicare_levy(self):
        income = self.gross_income
        if income < 30346:
         return  0
        else:
          return income * 0.02

    def get_total_tax(self):
        total_tax = self.tax_payable() + self.medicare_levy()
        return total_tax
    
    def refund_estimate(self):
        refund = self.tax_withheld - self.get_total_tax()
        return refund
           
    def summary(self):
        tax = self.tax_payable()
        levy = self.medicare_levy()
        refund = self.refund_estimate()
        return {
            "Tax": round(tax),
            "Refund": round(refund)
        }
