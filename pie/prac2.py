class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'You have {self.num_arrows} arrows')

    def run(self):
        print('run really fast')

# inheritance
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)
        

# wizard1 = Wizard('Merlin', 50)


# def player_attack(character):
#     character.attack()
hb = HybridBorg('Borgy', 50, 100)
print(hb.sign_in())

# print(wizard1.email)
# print(dir(wizard1))
# print(len([1,2,3,4]))
