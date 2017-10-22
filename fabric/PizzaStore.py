from Pizzas import *


class PizzaStore:
    """docstring for PizzaStore"""

    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def get_pizza(self, pizza_type, name):
        if pizza_type == 'cheese':
            return CheesePizza.CheesePizza(self.ingredient_factory, name)
        elif pizza_type == 'pepperoni':
            return PepperoniPizza.PepperoniPizza(self.ingredient_factory, name)

    def order_pizza(self, pizza_type, name):
        pizza = self.get_pizza(pizza_type, name)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print()

        return pizza
