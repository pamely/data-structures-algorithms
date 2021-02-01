# this is the main program
import sys
import time 

# function to find pisano number
def pisano_number(p):
    '''
        args: An integer
        return: pisano number
        eg: Input = 3 ; Output = 8
    '''
    a = 0
    b = 1
    for i in range(p * p ):
        c = (a+b) % p
        a = b
        b = c
        if (a == 0 and b == 1):
            return (i+1) 

# function to find Fibonacci number
def fibonacci(n):
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
    return fib_number 

# function to find 𝐹𝑛 modulo 𝑚, where 𝑛 may be really huge
def fibonacci_huge (n, m):
    '''
        args: Two integers n and m; 1 ≤ 𝑛 ≤ 10^14 and 2 ≤ 𝑚 ≤ 10^3
        return: Fibonacci(n) modulo b
        eg: Input = 239, 1000; Output = 161

    '''
    real_fibo_term = n % (pisano_number(m)) #  pisano_number(3) = 8
    
    return fibonacci(real_fibo_term) % m 
if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
 
    print(fibonacci_huge (n, m))
    
    
