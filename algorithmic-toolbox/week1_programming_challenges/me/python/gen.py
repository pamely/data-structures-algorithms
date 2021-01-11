import sys
import random

n = int(sys.argv[1])

myseed = int(sys.argv[2])

output = ' '.join([str(random.randint(1, 10000)) for i in range(n)])

print (n)

print(output)

