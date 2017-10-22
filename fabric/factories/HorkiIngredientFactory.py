import factories.PizzaIngredientFactory as BaseFactory
from ingredients import *


class HorkiIngredientFactory(BaseFactory.PizzaIngredientFactory):
    @staticmethod
    def get_dough():
        return Dough.Dough('блин')

    @staticmethod
    def get_sauce():
        return Sauce.Sauce('мазик')

    @staticmethod
    def get_veggies():
        return Veggies.Veggies('помидор')

    @staticmethod
    def get_cheese():
        return Cheese.Cheese('горецкий сыр')

    @staticmethod
    def get_pepperoni():
        return Pepperoni.Pepperoni('сосиски')

    @staticmethod
    def get_clams():
        return Clams.Clams('крабовые палочки')
