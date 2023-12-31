class BalloonTooFull(Exception):
    pass

class Balloon:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pump(self):
        self.amount += 3
        if self.amount > self.capacity:
            raise BalloonTooFull("Pop!")

    def release(self):
        self.amount -= 2
        self.amount = max(0, self.amount)

class SwordBalloon(Balloon):
    def __init__(self):
        super().__init__(capacity=5)

class DogBalloon(Balloon):
    def __init__(self):
        super().__init__(capacity=7)

class TriforceBalloon(Balloon):
    def __init__(self):
        super().__init__(capacity=11)
