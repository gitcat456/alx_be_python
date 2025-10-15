class Anime:
    def __init__(self, name, rating, country ):
        self.name = name
        self.rating = rating
        self.country = country
        
     #allows you to print(index1)  directly without calling a function 
    def __str__(self):
        return f"{self.name} from {self.country} rating of {self.rating}"
        
    def get_info(self):
        return f"{self.name} from {self.country} rating of {self.rating}"
    

index1 = Anime("Dragon Ball Super", 9.5, "Japan")
index2 = Anime("Ice Cube", 8.3, "China")
index3 = Anime("One Piece", 9.3, "Japan")

objs = [index1,index2,index3]
for obj in objs:
    print(obj)

        