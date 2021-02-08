# Uses python3
import sys

def get_change(m):
    '''
        Goal: This function aims to  to find the minimum number of coins needed to change the input value
              (an integer) into coins with denominations 1, 5, and 10.

        Algorithm type: Greedy algorithm

        Argument: An integer m 

        Return: An integer 

    '''
    # number of coins with denominations 1, 5, 10
    coin_count = 0

    while (m >= 0):
        if (m < 5):
            # best move if m  in [1:5]
            coin_count += m
            m = 0
            return coin_count
        elif (m >= 5 and m < 10):
            # best move if m in [5:10]
            coin_count += 1
            m -= 5
        else:
            # best move if m >= 10
            temp = (m-(m % 10))
            coin_count += temp /10
            m = m - temp 

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = int(input())
    print(get_change(m))
