
def monthlyPayment(loan_amount, i, num_payments):
    i = i/1200
    return loan_amount * (i*(1+i)**num_payments)/((1+i)**num_payments - 1)

def remainingBalance(loan_amount: float, i: float, payment: float, month: int):
    i = i/1200
    return loan_amount*((1+i)**month) - payment*((1+i)**month-1)/i
