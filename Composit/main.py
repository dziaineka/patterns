from menu import Menu
from menuItem import MenuItem
from waitress import Waitress

# Breakfast
cupcake = MenuItem('Cupcake', True, 1.5)
coffee = MenuItem('Coffee', False, 2)
tea = MenuItem('Tea', True, 1)
cereal = MenuItem('Cereal', True, 3)
sandwich = MenuItem('Sandwich', False, 2)

# Pizza store
carbonara = MenuItem('Carbonara', False, 5)
mozarella = MenuItem('Mozarella', False, 6)
cheese_pizza = MenuItem('Cheese Pizza', True, 4)

# Sauces
spicy_sauce = MenuItem('Spicy Sauce', False, 1)
cheese_sauce = MenuItem('Cheese Sauce', False, 1)

# Sushi
nigiri = MenuItem('Nigiri', False, 3)
sashimi = MenuItem('Sashimi', True, 2)
maki = MenuItem('Maki', False, 5)
uramaki = MenuItem('Uramaki', True, 4)
temaki = MenuItem('Temaki', False, 3)

# Menus creation
breakfast = Menu('Breakfast Menu', cupcake, coffee, tea, cereal, sandwich)
sauces = Menu('Sauces Menu', spicy_sauce, cheese_sauce)
pizza = Menu('Pizza Menu',
             carbonara,
             mozarella,
             cheese_pizza,
             sauces)
sushi = Menu('Sushi Menu', nigiri, sashimi, maki, uramaki, temaki)

general_menu = Menu('General Menu', breakfast, pizza, sushi)

waitress = Waitress(general_menu)

waitress.show_menu()
waitress.show_vegetarian()
