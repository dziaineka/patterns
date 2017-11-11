class Menu:
    """Menu"""

    def __init__(self, name, *menu_items):
        self.name = name
        self.menu_items = list(menu_items)
        self.is_veg = self.menu_contain_veg()

    def menu_contain_veg(self):
        for item in self.menu_items:
            if item.is_veg:
                return True

        return False

    def get_description(self):
        print("Menu {}".format(self.name))

    def get_item(self):
        yield self

        for item in self.menu_items:
            yield from item.get_item()

