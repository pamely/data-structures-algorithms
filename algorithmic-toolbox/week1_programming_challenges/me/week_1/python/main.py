# this is the main program

def find_rmv_elmt(x):
    'Find the maximum of x and remove element from it'
    x_max = max(x)
    x_max_index = x.index(x_max)
    del x[x_max_index]
    return x_max 


def max_pairwise_product(numbers):
    product = 1
    for i in range(2):
        product *= find_rmv_elmt(numbers)
    return product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
