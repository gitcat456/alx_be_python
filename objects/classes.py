class Student:
    def __init__(self, reg_no, name, course):
        self.reg_no = reg_no
        self.name = name
        self.course = course
        
    def get_student_info(self):
        print(f"{self.reg_no}, {self.name}, {self.course}")
    
#objects

stud_1 = Student(9234, "Goku Blue", "Criminology")
print (stud_1.get_student_info())

stud_2 = Student(4930, "Solo Leveller", "Mass Destruction")
print(stud_2.get_student_info())


# Define a class (blueprint)
class User:
    def __init__(self, username, user_id):
        self.username = username
        self._id = user_id

# Create an object (instance of the class)
user = User("okoth Denzel", "68ac32459y")

# Access object attributes with DOT notation
print(user.username)  # Output: okoth Denzel
print(user._id)       # Output: 68ac32459y