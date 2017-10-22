import Pizzas.Pizza as BasePizza


class CheesePizza(BasePizza.Pizza):
    def __init__(self, ingredient_factory, name):
        super().__init__(ingredient_factory, name)
        self.description = 'Cheese Pizza'

    def prepare(self):
        print('Preparing:')
        factory = self.ingredient_factory

        dough = factory.get_dough()
        self.ingredient_list.append(dough)

        sauce = factory.get_sauce()
        self.ingredient_list.append(sauce)

        cheese = factory.get_cheese()
        self.ingredient_list.append(cheese)

        self.mix(self.ingredient_list)
        print()
