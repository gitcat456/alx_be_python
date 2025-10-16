class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()  # No type check — just assumes 'thing' can quack

d = Duck()
p = Person()

make_it_quack(d)  # Output: Quack!
make_it_quack(p)  # Output: I'm pretending to be a duck!
