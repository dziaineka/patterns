from ducks import MallardDuck, RedHeadDuck
from fly_behaviours import FlyNoWay, FlyWithWings
from quack_behaviours import Quack, Squeak

my_mallard = MallardDuck.MallardDuck(
    lambda: print('Mallard flying'),
    lambda: print('Mallard quacking')
)

my_mallard.action()

my_mallard2 = MallardDuck.MallardDuck(
    FlyWithWings.FlyingWithWings.fly,
    Quack.Quack.quack
)

my_mallard2.action()

my_red_head = RedHeadDuck.RedHeadDuck(
    lambda: print('Red Head flying'),
    lambda: print('Red Head quacking')
)

my_red_head.action()

my_red_head2 = RedHeadDuck.RedHeadDuck(
    FlyNoWay.FlyNoWay.fly,
    Squeak.Squeak.squeak
)

my_red_head2.action()
