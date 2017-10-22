import random
import time
import PizzaStore
from factories import *

pizza_types = ['cheese', 'pepperoni']
names = ['Noah', 'Liam', 'Mason', 'Jacob', 'William', 'Ethan',
         'James', 'Alexander', 'Michael', 'Benjamin', 'Elijah', 'Daniel',
         'Aiden', 'Logan', 'Matthew', 'Lucas', 'Jackson']

horki_factory = HorkiIngredientFactory.HorkiIngredientFactory()
horki_pizza_store = PizzaStore.PizzaStore(horki_factory)

minsk_factory = MinskIngredientFactory.MinskIngredientFactory()
minsk_pizza_store = PizzaStore.PizzaStore(minsk_factory)

while True:
    store = random.choice([horki_pizza_store, minsk_pizza_store])

    pizza = store.order_pizza(random.choice(pizza_types),
                              random.choice(names))

    print(pizza.get_full_description())

    time.sleep(random.choice(range(5)))
