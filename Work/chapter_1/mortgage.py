"""
mortgage.py
"""

PRINCIPAL: float = 500000.0
RATE: float = 0.05
PAYMENT: float = 2684.11
CURRENT_PAYMENT: float = 0.0
EXTRA_PAYMENT: float = 1000.0
EXTRA_PAYMENT_START_MONTH: int = 60
EXTRA_PAYMENT_END_MONTH: int = 108
TOTAL_PAID: float = 0.0
MONTHS_PAID: int = 0

def print_payment_history(
    months_paid: int,
    current_payment: float,
    total_payment: float,
    principal: float
) -> None:
    """
    print_payment_history formats arguments, rounds each argument to two decimals
    and prints themt to the console.
    """
    print(
        months_paid,
        round(current_payment, 2),
        round(total_payment, 2),
        round(principal, 2)
    )

while PRINCIPAL > 0:
    CURRENT_PAYMENT = PAYMENT
    MONTHS_PAID = MONTHS_PAID + 1

    # Make extra payments between months 60 and 108
    if EXTRA_PAYMENT_START_MONTH <= MONTHS_PAID <= EXTRA_PAYMENT_END_MONTH:
        CURRENT_PAYMENT = PAYMENT + EXTRA_PAYMENT

    # Last payment should be principal only (no interest) and break out immediately
    if PRINCIPAL < PAYMENT:
        CURRENT_PAYMENT = PRINCIPAL
        TOTAL_PAID = TOTAL_PAID + PRINCIPAL
        PRINCIPAL = 0
        break

    TOTAL_PAID = TOTAL_PAID + CURRENT_PAYMENT
    PRINCIPAL = PRINCIPAL * (1 + RATE / 12) - CURRENT_PAYMENT
    print_payment_history(MONTHS_PAID, CURRENT_PAYMENT, TOTAL_PAID, PRINCIPAL)

print_payment_history(MONTHS_PAID, CURRENT_PAYMENT, TOTAL_PAID, PRINCIPAL)
print('Total paid', round(TOTAL_PAID, 2))
print('Months paid', MONTHS_PAID)
