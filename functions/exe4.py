#manipulating the list data structure
my_list = [20,30,40,50,60,70]
print (my_list[::5]) #slicing
my_list.append(80) #appending
my_list.remove(30) #removing
del my_list[1]   #deleting
print(my_list)

fav_book = {
    'title': 'TINY HABITS',
    'author': 'Dr. Denzel',
    'Genre': 'Reality'
}

print(fav_book['Genre'])
