# this is the main program
import sys
import time 


def gcd(a, b):
    '''
        args: Two integers a and b, a >= b >= 0
        return: gcd
        eg: Input = 12, 5; Output = 1
    '''
    return a if b == 0 else gcd(b, a % b)

# trick lcm(a, b) * gcd(a, b) = a*b

def lcm (a,b):
    '''
        args: Two integers a and b, a >= b >= 0
        return: lcm
        eg: Input = 12, 5; Output = 60

    '''
    return  (a * b) // gcd(a, b)
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
    
    
