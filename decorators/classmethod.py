class Person:
    
    count = 0 #class variable to count instances
    
    def __init__(self, name):
        self.name = name
        Person.count += 1  #increment count on instance creation
        
    @classmethod
    def display_count(cls):
        return f"Total persons created: {cls.count}"
    
    
#usage
person1 = Person("Alice")
person2 = Person("Arisu")
person3 = Person("joker")

print(Person.display_count())   #output :Total persons created : 3
        
    