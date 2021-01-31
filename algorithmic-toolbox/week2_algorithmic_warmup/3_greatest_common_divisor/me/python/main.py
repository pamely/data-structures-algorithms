# this is the main program
import sys
import time 


def gcd(a, b):
    '''
        args: Two integers a and b, a >= b >= 0
        return: gcd
        eg: Input = 12, 5; Output = 1
    '''
    return  if b == 0 else gcd(b, a % b)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(gcd(a, b))
    
    
