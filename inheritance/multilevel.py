class Institutes:
    def __init__(self, category):
        self.category = category

    def year_founded(self, year):
        self.year = year
        return f"Founded in {self.year}"

class Level(Institutes):
    def __init__(self, category, level):
        super().__init__(category)  # call Institutes constructor
        self.level = level

    def get_level(self):
        return f"{self.level}"

class Group(Level):
    def __init__(self, category, level, group, name):
        super().__init__(category, level)  # call Level constructor
        self.name = name
        self.group = group

    def __str__(self):
        institute = self.year_founded("1999")
        return f"{self.name} is a {self.group} school ({self.category}, {self.level}). {institute}"


maranda = Group("High School", "Secondary", "National Level", "Maranda School")
print(maranda)
