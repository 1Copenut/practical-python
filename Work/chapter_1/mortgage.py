"""
mortgage.py
"""

PRINCIPAL = 500000.0
RATE = 0.05
PAYMENT = 2684.11
CURRENT_PAYMENT = 0.0
EXTRA_PAYMENT = 1000.0
EXTRA_PAYMENT_START_MONTH = 60
EXTRA_PAYMENT_END_MONTH = 108
TOTAL_PAID = 0.0
MONTHS_PAID = 0

while PRINCIPAL > 0:
    if PRINCIPAL < PAYMENT:
        CURRENT_PAYMENT = PRINCIPAL
        TOTAL_PAID = TOTAL_PAID + PRINCIPAL
        PRINCIPAL = 0
        MONTHS_PAID = MONTHS_PAID + 1
        break
    elif (
        (MONTHS_PAID >= EXTRA_PAYMENT_START_MONTH) and
        (MONTHS_PAID <= EXTRA_PAYMENT_END_MONTH)
    ):
        CURRENT_PAYMENT = PAYMENT + EXTRA_PAYMENT
    else:
        CURRENT_PAYMENT = PAYMENT

    TOTAL_PAID = TOTAL_PAID + CURRENT_PAYMENT
    PRINCIPAL = PRINCIPAL * (1 + RATE / 12) - CURRENT_PAYMENT
    MONTHS_PAID = MONTHS_PAID + 1
    print(MONTHS_PAID, round(CURRENT_PAYMENT, 2), round(TOTAL_PAID, 2), round(PRINCIPAL, 2))

print(MONTHS_PAID, round(CURRENT_PAYMENT, 2), round(TOTAL_PAID, 2), round(PRINCIPAL, 2))
print('Total paid', round(TOTAL_PAID, 2))
print('Months paid', MONTHS_PAID)
