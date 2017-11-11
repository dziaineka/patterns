class MenuItem:
    def __init__(self, name, is_veg, price):
        self.name = name
        self.is_veg = is_veg
        self.price = price

    def veg_string(self):
        if self.is_veg:
            return 'veg'
        else:
            return 'nonveg'

    def get_description(self):
        print('  {}({}) for {}'.format(self.name,
                                       self.veg_string(),
                                       self.price))

    def get_item(self):
        yield self
