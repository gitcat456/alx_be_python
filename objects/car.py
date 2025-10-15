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
    
    def main_character(self, mainxter):
        self.mainxter = mainxter
        return f"The main characters name is {self.mainxter}"
    
    def get_move(self, move):
        self.move = move
        return f"His Killer move is {self.move} "
        
    

index1 = Anime("Dragon Ball Super", 9.5, "Japan")
index2 = Anime("Ice Cube", 8.3, "China")
index3 = Anime("One Piece", 9.3, "Japan")

print(index1.get_move("Spirit Bomb!"))

objs = [index1,index2,index3]
for obj in objs:
    print(obj)

        