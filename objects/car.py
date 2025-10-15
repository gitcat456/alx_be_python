class Anime:
    def __init__(self, name, rating, country):
        self.name = name
        self.rating = rating
        self.country = country
        self.mainxter = None
        self.move = None

    # Allows printing the object directly
    def __str__(self):
        return (
            f"{self.name} from {self.country} has a rating of {self.rating}\n"
            f"The main character is {self.mainxter}\n"
            f"Killer move: {self.move}"
        )

    def set_main_character(self, mainxter):
        self.mainxter = mainxter

    def set_move(self, move):
        self.move = move

    

index1 = Anime("Dragon Ball Super", 9.5, "Japan")
index1.set_main_character("Son Goku")
index1.set_move("Spirit Bomb")

index2 = Anime("Ice Cube", 8.3, "China")
index2.set_main_character("Chiller Z")
index2.set_move("Frost Strike")

index3 = Anime("One Piece", 9.3, "Japan")
index3.set_main_character("Luffy")
index3.set_move("Gum-Gum Bazooka")

objs = [index1, index2, index3]

for obj in objs:
    print(obj)
    print("-" * 40)





        