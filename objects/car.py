class Anime:
    def __init__(self, name, rating, country ):
        self.name = name
        self.rating = rating
        self.country = country
        
    def get_info(self):
        return f"{self.name} from {self.country} rating of {self.rating}"
    

index1 = Anime("Dragon Ball Super", 9.5, "Japan")
print(index1)
        