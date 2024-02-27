# price of a house is $1M
# If a buyer has good credit:
# -they need to put down 10%
# otherwise:
# -they need to put down 20%
# -print the down payment

house_price = 1000000
has_good_credit =False

if has_good_credit:
   down_payment =  int(house_price * 0.10)
else:
   down_payment = int(house_price * 0.20)
print(f'your downpayment is ${down_payment}')

