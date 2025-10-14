def checker(num):
    if num % 2 == 0:
       return 'even' 
    else:
        return 'odd'
number = int(input('Enter a number: '))
print(checker(number))