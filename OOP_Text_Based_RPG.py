import random

class Being:
    def __init__(self,name,health, attack_dmg, armour_toughness_percentage, mage_attack,inall_health=0,inall_armor=0):
        self.name=name
        self.inall_health=inall_health
        self.health=health
        self.attack_dmg=attack_dmg
        self.armour_toughness_percentage=armour_toughness_percentage
        self.mage_attack=mage_attack
        self.inall_armor=inall_armor

    def restore(self):
        self.health = self.inall_health
        self.armour_toughness_percentage = self.inall_armor

    def sword_attack(self, target):
        target.health -= (self.attack_dmg-(self.attack_dmg * target.armour_toughness_percentage))

        print(f"{target.name} Health: {target.health}")

    def magic_attack(self, target):
        target.health -= round((self.attack_dmg-(self.attack_dmg * target.armour_toughness_percentage))/3)
        target.armour_toughness_percentage -= self.mage_attack
        if target.armour_toughness_percentage <= 0: target.armour_toughness_percentage=0

        print(f"{target.name} Health: {target.health}")
        print(f"{target.name} Armour toughness: {target.armour_toughness_percentage*100}%")

    def Upgrade(self):
        
        print("Pick your reward:-")
        print("1:+30 HP, 2:+15 attack dmg, 3:+10 percent armor upgrade, 4:+10 percent mage attack")
        upgrade_options = int(input("1 or 2 or 3 or 4: "))
        match upgrade_options:
            case 1:
                self.inall_health += 30
                #self.health += 30
                print("Health upgraded!")
            case 2:
                self.attack_dmg += 15
                print("Attack damage upgraded!")
            case 3:
                self.inall_armor += 0.1
                #self.armour_toughness_percentage += 0.1
                print("Armour toughness upgraded!")
            case 4:
                self.mage_attack += 0.1
                self.attack_dmg += 5
                print("Mage attack upgraded!")
                print("Mage attack damage upgraded (+5)!")
            case _:
                print("Upgrade skipped!")



health = [75, 80,90, 100]
high_health = [130, 150, 170, 200, 250]

attack_dmg = [20, 25, 35, 40]
high_attack_dmg = [50, 65, 75, 90, 100]

#enemyOP = Being(random.choice(high_health), random.choice(high_attack_dmg), 0.7)


def options(enemy):
    act = input("Sword attack (strong attack damage) or magic attack (weakens armor while dealing less damage)? (sword/magic): ").lower()
    match act:
        case 'sword':
            Player.sword_attack(enemy)
        case "magic":
            Player.magic_attack(enemy)
        case _:
            print("Invalid text, chance to choose skipped!")


def enemy_attack(enemy,player):
    attacks=['sword','magic']
    pick=random.choice(attacks)
    if player.armour_toughness_percentage <= 0:
        enemy.sword_attack(player)
    else:
        match pick:
            case 'sword':
                enemy.sword_attack(player)
                print("enemy hit you with a sword!")
            case 'magic':
                enemy.magic_attack(player)
                print("Enemy hit you with magic!")


Player = Being('Player', 100, 20, 0.2, 0.1, 100,0.2)

while True:
    game = input("Would you like to play?: (yes/no): ").lower()
    match game:
        case 'yes':
            Player.restore()
            enemyez = Being('Enemy', random.choice(health), random.choice(attack_dmg) , 0.3, 0.1)
            print(f"You have {Player.health} HP, {Player.attack_dmg} attack damage, {int(Player.armour_toughness_percentage*100)}% armour toughness, and {int(Player.mage_attack*100)}% mage attack power")
            print(f"An enemy of health {enemyez.health} and attack dmg {enemyez.attack_dmg} with 30% armor toughness, and 10% mage attack has appeared!!")
            while True:
                print("----------------")
                options(enemyez)
                if enemyez.health <= 0:
                    print("----------------")
                    print("Enemy Defeated!!")
                    Player.Upgrade()
                    break
                enemy_attack(enemyez,Player)
                if Player.health <= 0:
                    print("You have been Defeated!")
                    break
            del enemyez
        case'no':
            break
print("Have a nice day!")