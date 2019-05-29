n = int(input(""))
li=list(map(int, input("").split()))
for i in range(n):
    li.sort()
print("",*li)
