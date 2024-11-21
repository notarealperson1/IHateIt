class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 100
        self.weapon = "Нож"

    def take_damage(self, damage):

        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"Персонаж {self.name} погиб.")
        else:
            print(f"{self.name} получил урон: {damage}. Текущее здоровье: {self.health}.")

    def equip_weapon(self, weapon):

        self.weapon = weapon
        print(f"{self.name} сменил оружие на {self.weapon}.")

    def attack(self):

        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} атакует с оружием {self.weapon}. Энергия уменьшена на 10.")
        else:
            print("Недостаточно энергии для атаки.")

    def get_status(self):
        #
        return f"Персонаж {self.name}: Здоровье - {self.health}, Энергия - {self.energy}, Оружие - {self.weapon}"
character = Character("Герой")
print(character.get_status())
character.attack()
character.take_damage(30)
character.equip_weapon("Меч")
print(character.get_status())
character.attack()