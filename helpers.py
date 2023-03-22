
def monthlyPayment(loan_amount, i, num_payments):
    """
    Calculates the monthly loan payment given the total loan amount, interest rate, and the loan term (number of payments)
    
    :param loan_amount: The starting loan amount.
    :param i: The annualized interest rate.
    :param num_payments: The loan term (number of payments)
    :return: The monthly payment for the given loan information.
    """
    i = i/1200
    return loan_amount * (i*(1+i)**num_payments)/((1+i)**num_payments - 1)

def remainingBalance(loan_amount: float, i: float, payment: float, month: int):
    """
    Calculates the remaining loan balance given total loan amount, interest rate, monthly payment, and current term month.
    
    :param loan_amount: The starting loan amount.
    :param i: The annualized interest rate.
    :param payment: The monthly payment of the loan.
    :param month: The current term month.
    :return: The remaining balance for the given term month.
    """
    i = i/1200
    return loan_amount*((1+i)**month) - payment*((1+i)**month-1)/i

def formatCurrency(amount: float):
    """
    Formats a float into currency format
    
    :param amount: A float representing the amount.
    :return: The amount in currency format ($100.00).
    """
    return "${:.2f}".format(round(amount, 2))

def formatPercent(rate: float):
    """
    Formats a float into a percent with 3 decimal places.
    
    :param rate: the rate as a percent (3.0 for 3%).
    :return: The rate in percent format (3.000%).
    """
    return "{:.3f}%".format(round(rate, 3))