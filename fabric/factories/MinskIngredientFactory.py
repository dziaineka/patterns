import factories.PizzaIngredientFactory as BaseFactory
from ingredients import *


class MinskIngredientFactory(BaseFactory.PizzaIngredientFactory):
    @staticmethod
    def get_dough():
        return Dough.Dough('роскошное тесто')

    @staticmethod
    def get_sauce():
        return Sauce.Sauce('сырный соус')

    @staticmethod
    def get_veggies():
        return Veggies.Veggies('руккола')

    @staticmethod
    def get_cheese():
        return Cheese.Cheese('моцарелла')

    @staticmethod
    def get_pepperoni():
        return Pepperoni.Pepperoni('пепперони')

    @staticmethod
    def get_clams():
        return Clams.Clams('лобстер')