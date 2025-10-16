class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"Generic Animal Sound"
    
class Dog(Animal):
    def make_sound(self):
        return f"woof woof!"
    
poppy = Animal("poppy")
print(poppy.make_sound())