from ducks import Duck


class MallardDuck(Duck.Duck):
    def __init__(self, fly_behaviour, quack_behaviour):
        super(MallardDuck, self).__init__(fly_behaviour, quack_behaviour)
        self._description = 'Mallard Duck'
