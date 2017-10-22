class Pizza:
    """Pizza"""

    def __init__(self, ingredient_factory, customer):
        self.ingredient_factory = ingredient_factory
        self.description = 'Pizza'
        self.ingredient_list = []
        self.customer = customer

    def mix(self, ingredients):
        for ingredient in ingredients:
            print('  adding {}'.format(ingredient.description))

    def prepare(self):
        print('Preparing...')

    def bake(self):
        print('Baking...')

    def cut(self):
        print('Cutting...')

    def box(self):
        print('Boxing...')

    def get_full_description(self):
        description = '{} with '.format(self.description)

        for ingredient in self.ingredient_list:
            description += '{}, '.format(ingredient.description)

        description = description.rpartition(',')[0]
        description += ' for {}'.format(self.customer)
        description += '.'

        return description
