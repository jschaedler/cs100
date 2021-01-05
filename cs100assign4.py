import math as m


def ship_cost(w):
    if w <= 2:
        price = 15
        return price
    elif w <= 70:
        price = (((m.ceil(w) - 2) * 5) + 15)
        return price
    elif w <= 100:
        price = (((m.ceil(w) - 2) * 5) + 30)
        return price
    else:
        return None


Weight = float(input('Enter Weight in Pounds: '))
if ship_cost(Weight) is None:
    print('Invalid weight')
else:
    print('$', ship_cost(Weight))
