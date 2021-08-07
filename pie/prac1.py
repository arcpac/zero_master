class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        self._name = name
        self._age = age

    def run(self):
        return self
    
    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old')

player1 = PlayerCharacter('test', 10)
print(player1.speak)
