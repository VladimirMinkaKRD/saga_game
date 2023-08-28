import random


class Sword:
    name = 'мечем'
    damage = '7-9'
    critical_hit_chance = 25


class Axe:
    name = 'секирой'
    damage = '15-18'
    critical_hit_chance = 12


class Pike:
    name = 'копьем'
    damage = '11-15'
    critical_hit_chance = 18


class Bow:
    name = 'луком'
    damage = '2-20'
    critical_hit_chance = 20


class Crossbow:
    name = 'арбалетом'
    damage = '8-25'
    critical_hit_chance = 17


class Unit:
    names = ['John', 'Michael', 'Vlad', 'Tom', 'Ted', 'Walter', 'Nick', 'David', 'Alfred', 'Andrew', 'Brian', 'Carl',
             'Kyle', 'Oliver', 'Alice', 'Amanda', 'Gloria', 'Jenny', 'Julia', 'Eva', 'Karen', 'Layla']
    health_point = 100


class Warrior(Unit):
    rank = 'Воин'
    evasion_chance = 20
    armor = 30
    weapon = Sword()

    def __init__(self):
        self.name = random.choice(self.names)


class Archer(Unit):
    rank = 'Лучник'
    evasion_chance = 15
    armor = 10
    weapon = random.choice([Bow, Crossbow])()

    def __init__(self):
        self.name = random.choice(self.names)


class Paladin(Unit):
    rank = 'Паладин'
    evasion_chance = 25
    armor = 20
    weapon = Sword()

    def __init__(self):
        self.name = random.choice(self.names)


class Ork(Unit):
    rank = 'Орк'
    evasion_chance = 10
    armor = 35
    weapon = Axe()

    def __init__(self):
        self.name = random.choice(self.names)


class Assassin(Unit):
    rank = 'Убийца'
    evasion_chance = 25
    armor = 10
    weapon = Pike()

    def __init__(self):
        self.name = random.choice(self.names)
