import Pizzas


class PizzaStore:
    """docstring for PizzaStore"""

    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def get_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            return Pizzas.CheesePizza.CheesePizza(self.ingredient_factory)
        elif pizza_type == 'pepperoni':
            return Pizzas.PepperoniPizza.PepperoniPizza(self.ingredient_factory)

    def order_pizza(self, pizza_type):
        pizza = self.get_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
