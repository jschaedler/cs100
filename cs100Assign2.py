import math as m

weight = float(input('Weight of Package in Pounds'))
if weight <= 2:
    print('$15')
elif weight <= 70:
    # price per pound above 2 and initial charge
    price = (((m.ceil(weight) - 2) * 5) + 15)
    print('$', price)
elif weight <= 100:
    # price including weight charge of 15 and charge per pound above 2 and initial charge
    price = (((m.ceil(weight) - 2) * 5) + 30)
    print('$', price)
else:
    print('Weight cannot be accepted')
