#syntax  : for variable in iterable:    where iterable is something you can loop over
           #condition to be executed
           
for i in range(3):   #i<10
    print(f"loop:{i}")
    
#looping through a list 
languages = ["python","javascript", "java", "mySql", "Cpp"]
for language in languages:
    print(f"The user has experience in {language}")
    
#loop through a string
name ="Engineer Denzel"
for letter in name:
    print (f"{letter}")
    
#loop through a dictionary
user = {
    "username": "okoth Denzel",
    "_id": "68ac32459y"
}
for key in user:
    print(key, "->", user[key]) #acess with brackets
    
#option2 using .items():
for key, value in user.items():
    print(key, "->", value)
    
#nested for loops
for i in range(3):
     for j in range(2):
         print(f"i={i}, j={j}")
         

count = 0
while count<5:
    print(count)
    count += 1