class Institutes:
    def __init__(self, category):
        self.category = category
        
            
    def year_founded(self, year):
        self.year = year
        return f"Founded in {self.year}"
    
class Level(Institutes):
    def __init__(self, level):
        self.level = level
    
    def get_level(self):
        return f"{self.level}"
    
class Group(Level):
    def __init__(self, group, name):
        self.name = name
        self.group = group 
        
    def __str__(self):
        institute = self.year_founded("1999")
        return f"{self.name} is a {self.group} school {institute} "
    
maranda = Group("National Level", "Maranda School")
print(maranda)