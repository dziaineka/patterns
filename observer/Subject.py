class Subject:
    """subject for observers"""

    def __init__(self, *observers):
        self.observers = list(observers)
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, *observers):
        self.observers.extend(observers)

    def remove_observer(self, *observers):
        self.observers.remove(observers)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
