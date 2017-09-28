from ducks import Duck


class RedHeadDuck(Duck.Duck):
    def __init__(self, fly_behaviour, quack_behaviour):
        super(RedHeadDuck, self).__init__(fly_behaviour, quack_behaviour)
        self._description = 'Red Head Duck'
