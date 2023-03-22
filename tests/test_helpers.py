from helpers import monthlyPayment, remainingBalance, formatCurrency, formatPercent

def test_monthlyPayment():
    loan_amount = 100000
    interest_rate = 3
    num_payments = 360
    assert round(monthlyPayment(loan_amount, interest_rate, num_payments), 2) == 421.6

def test_remainingBalance():
    loan_amount = 100000
    interest_rate = 3
    num_payments = 360
    monthly_payment = monthlyPayment(loan_amount, interest_rate, num_payments)
    assert round(remainingBalance(loan_amount, interest_rate, monthly_payment, 1), 2) == 99828.4

def test_formatCurrency():
    loan_amount = 100000
    interest_rate = 3
    num_payments = 360
    monthly_payment = monthlyPayment(loan_amount, interest_rate, num_payments)
    assert formatCurrency(monthly_payment) == "$421.60"
    assert formatCurrency(remainingBalance(loan_amount, interest_rate, monthly_payment, 1)) == "$99828.40"

def test_formatPercent():
    percent = 3.0
    assert formatPercent(percent) == "3.000%"