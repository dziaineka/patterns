class Pizza:
    """Pizza"""

    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print('prepearing')

    def bake(self):
        print('baking')

    def cut(self):
        print('cutting')

    def box(self):
        print('boxing')
