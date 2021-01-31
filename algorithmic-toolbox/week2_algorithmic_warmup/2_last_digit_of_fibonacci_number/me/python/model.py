# python3
def fib_last_digit(n):    
    if (n <= 1):
        return n %10
    return (fib_last_digit(n-1) +  fib_last_digit(n-2)) % 10


if __name__ == '__main__':
    n = int(input())
    print (fib_last_digit(n))
