# this is the main program
import time
import sys 

def fib_last_digit(n):
    '''
        args: An integer
        return: Fibonacci number
        eg: Input = 10; Output = 55
    '''
    if(n <= 1):
        return 
    start = 1
    fib_number = 1 

    for i in range(n-2):
        start, fib_number = fib_number, start + fib_number
    return fib_number % 10
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_last_digit(n))
    
    
