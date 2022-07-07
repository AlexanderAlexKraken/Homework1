from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 8.2 + 1.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 1.8 + 0.4


a = Coat(55)
b = Suit(1.82)
print(a)
print(a.expense)
print(b.expense)