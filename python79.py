import math
N,M=map(int,input().split())
mul=N*M
root = math.sqrt(mul)
if(mul==int(root + 0.5) ** 2):
    print("yes")
else:
    print("no")
