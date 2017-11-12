from gumballmachine import GumballMachine


machine = GumballMachine(5)

for i in range(6):
    machine.insert_coin()
    machine.turn_crank()
    print()

machine.refill(4)
