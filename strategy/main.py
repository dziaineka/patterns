from ducks import MallardDuck, RedHeadDuck
from fly_behaviours import FlyNoWay, FlyWithWings
from quack_behaviours import Quack, Squeak

my_mallard2 = MallardDuck.MallardDuck(
    FlyWithWings.FlyingWithWings,
    Quack.Quack
)

my_mallard2.action()

my_red_head2 = RedHeadDuck.RedHeadDuck(
    FlyNoWay.FlyNoWay,
    Squeak.Squeak
)

my_red_head2.action()
