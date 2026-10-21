principal = 500000
interest = 0.05
payment = 2684.11
total_payment = 0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
monthly_payment = 0

while principal > 0:
    month = month + 1

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        monthly_payment = payment + extra_payment
    else:
        monthly_payment = payment

    principal = principal * (1 + interest / 12) - monthly_payment

    if principal < 0:
        monthly_payment = 0
        print("Principal:", monthly_payment)

    total_payment = round(total_payment + monthly_payment, 2)

    print(
        "Month:" + str(month),
        "Principal:" + str(round(principal, 2)),
        "Monthly payment:" + str(monthly_payment),
    )

print("Total paid:", total_payment, "Took monthes:", month)
