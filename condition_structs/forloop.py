#syntax  : for variable in iterable:    where iterable is something you can loop over
           #condition to be executed
           
for i in range(3):   #i<10
    print(f"loop:{i}")
    
#looping over a list 
languages = ["python","javascript", "java", "mySql", "Cpp"]
for language in languages:
    print(f"The user has experience in {language}")