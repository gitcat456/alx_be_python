class Flyer:
    def fly(self):
        return f"Flying"
    
class Swimmer:
    def swim(self):
        return f"Swmiming"
    
class Human(Flyer, Swimmer):
    pass

superman = Human()
print(superman.fly())
print(superman.swim())