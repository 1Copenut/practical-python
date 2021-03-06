# mortgage.py

principal = 500000.0
starting_principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payments_made = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if (payments_made >= extra_payment_start_month) & (payments_made <= extra_payment_end_month):
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    payments_made = payments_made + 1
    # print(payments_made, round(total_paid, 2), round(principal, 2))
    print(f'{payments_made:3n} {total_paid:10.2f} {principal:10.2f}')

print(f'Principal borrowed: ${starting_principal:.2f}')
print(f'Total paid: ${total_paid:.2f}')
print(f'Months to pay off: {payments_made:n}')
