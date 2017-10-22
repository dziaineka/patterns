import Pizzas.Pizza as BasePizza


class PepperoniPizza(BasePizza):
    def __init__(self, ingredient_factory):
        super.__init__(ingredient_factory)

    def prepare(self):
        factory = self.ingredient_factory

        dough = factory.get_dough()
        sauce = factory.get_sauce()
        cheese = factory.get_cheese()
        pepperoni = factory.get_pepperoni()

        self.mix(dough, sauce, cheese, pepperoni)
