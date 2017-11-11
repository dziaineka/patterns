class Waitress:

    def __init__(self, menu):
        self.menu = menu

    def show_menu(self):
        menu_list = self.menu.get_item

        for item in menu_list():
            item.get_description()

    def show_vegetarian(self):
        menu_list = self.menu.get_item

        for item in menu_list():
            if item.is_veg:
                item.get_description()
