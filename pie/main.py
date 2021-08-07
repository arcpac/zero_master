class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Test', 8)
player2 = PlayerCharacter.adding_things2(2,4)
player3 = PlayerCharacter.adding_things(2,3)

print(player1.shout())
print(player2)
print(player3.age)
