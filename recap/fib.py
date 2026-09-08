sequence = 1,1,2,3,5,8,13,21

def fib(n):
    if n <= 1:
        return n 
    else:
        return fib(n-1) + fib(n-2)
    
fib(7)

for i in range(15):
    print (fib(i))