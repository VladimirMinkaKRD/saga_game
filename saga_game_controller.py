from random import choice, randint
from time import sleep

from saga_game_model import Warrior, Archer, Paladin, Ork, Assassin

characters_list = [Warrior, Archer, Paladin, Ork, Assassin]


class Game:
    def __init__(self):
        self.units = [choice(characters_list)() for i in range(12)]

    def get_enemy(self, unit):
        enemies = [obj for obj in self.units if obj != unit]
        enemy = choice(enemies)
        return enemy

    def is_evasion(self, enemy):
        evasion = False
        chance = enemy.evasion_chance
        if randint(0, 100) <= chance:
            evasion = True
        return evasion

    def is_critical_hit(self, unit):
        critical_hit = False
        chance = unit.weapon.critical_hit_chance
        if randint(0, 100) <= chance:
            critical_hit = True
        return critical_hit

    def get_strike(self, unit, enemy):
        if self.is_evasion(enemy):
            print(
                f'{unit.rank} {unit.name} атакует врага {enemy.rank} {enemy.name} {unit.weapon.name}, но {enemy.rank} {enemy.name} уворачивается. Урон - 0, здоровье противника {enemy.rank} {enemy.name} - {enemy.health_point if enemy.health_point >= 0 else 0}')

        elif self.is_critical_hit(unit):
            basic_damage = randint(int(unit.weapon.damage.split('-')[0]), int(unit.weapon.damage.split('-')[1])) * 2
            damage = basic_damage - int(basic_damage * (enemy.armor / 100))
            enemy.health_point = enemy.health_point - damage
            print(
                f'{unit.rank} {unit.name} атакует врага {enemy.rank} {enemy.name} {unit.weapon.name} и наносит '
                f'критический урон. Урон - {damage}, здоровье противника {enemy.rank} {enemy.name} - '
                f'{enemy.health_point if enemy.health_point >= 0 else 0}')

        else:
            basic_damage = randint(int(unit.weapon.damage.split('-')[0]), int(unit.weapon.damage.split('-')[1]))
            damage = basic_damage - int(basic_damage * (enemy.armor / 100))
            enemy.health_point = enemy.health_point - damage
            print(
                f'{unit.rank} {unit.name} атакует врага {enemy.rank} {enemy.name} {unit.weapon.name} и пробивает '
                f'броню. Урон - {damage}, здоровье противника {enemy.rank} {enemy.name} - '
                f'{enemy.health_point if enemy.health_point >= 0 else 0}')

        if enemy.health_point <= 0:
            print(f'{enemy.rank} {enemy.name} убит.')
            self.units.remove(enemy)
        print('-' * 130)
        sleep(1)

    def action(self):
        while len(self.units) != 1:
            for unit in self.units:
                enemy = self.get_enemy(unit)
                self.get_strike(unit, enemy)
        return f'{unit.rank} {unit.name} победитель! Его здоровье - {unit.health_point}'
