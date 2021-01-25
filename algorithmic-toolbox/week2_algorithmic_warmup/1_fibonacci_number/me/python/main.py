# this is the main program
import time 

def calc_fib(n):
    '''
        args: An integer
        return: Fibonacci number
        eg: Input = 10; Output = 55
    '''
    if(n <= 1):
        return n
    start = 1
    fib_number = 1 

    for i in range(n-2):
        temp = fib_number + start
        start = fib_number
        fib_number = temp 
    return fib_number
    

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
    
    
