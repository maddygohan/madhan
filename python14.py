n=int(input(""))
k=int(input(""))
if(n>100000 and k>100000):
    print("enter values in between 100000")
else:
    for i in range(n+1,k):
        if(i%2!=0):
            print(i)
