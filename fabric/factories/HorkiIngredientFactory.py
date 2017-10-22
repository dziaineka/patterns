import factories.PizzaIngredientFactory as BaseFactory
import ingredients


class HorkiIngredientFactory(BaseFactory):
    def get_dough(self):
        return ingredients.Dough('Horki dough')

    def get_sauce(self):
        pass

    def get_veggies(self):
        pass

    def get_cheese(self):
        pass

    def get_pepperoni(self):
        pass

    def get_clams(self):
        pass
