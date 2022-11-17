class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        ...

    def defence(self):
        ...

    def special(self):
        ...


class Warrior(Character):
    ...


class Mage(Character):
    ...


class Healer(Character):
    ...