import DarkRoast
import HouseBlend
import Milk
import Mocha
import Soy


condiment_str = '''Choose condiment:
  1. Milk
  2. Mocha
  3. Soy
  4. Enough'''

beverage_str = '''Choose beverage:
  1. Dark Roast
  2. House Blend'''


def check_input(option, *tolerable):
    if tolerable.count(option) != 0:
        return True
    else:
        return False

    tolerable


def get_base():
    option = 0

    while not check_input(option, 1, 2):
        print(beverage_str)
        option = int(input())
        print()

    if option == 1:
        return DarkRoast.DarkRoast()
    elif option == 2:
        return HouseBlend.HouseBlend()


def get_condiments(beverage):
    option = 0
    my_bev = beverage

    while option != 4:
        print(condiment_str)
        option = int(input())
        print()

        if check_input(option, 1, 2, 3):
            if option == 1:
                my_bev = Milk.Milk(my_bev)
            elif option == 2:
                my_bev = Mocha.Mocha(my_bev)
            elif option == 3:
                my_bev = Soy.Soy(my_bev)

    return my_bev


myBeverage = get_base()
myBeverage = get_condiments(myBeverage)

print('Description: {}'.format(myBeverage.description))
print('Total cost: {}'.format(myBeverage.cost))
