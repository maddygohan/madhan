Num=int(input())
for i in range(2,Num//2):
    if(Num%i==0):
        print("no")
        break
else:
    print("yes")
