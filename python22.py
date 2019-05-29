li = []
n = int(input(""))
li=list(map(int, input("").split())) 
for i in range(1,n):
    li.sort()
print("",li[-1])
