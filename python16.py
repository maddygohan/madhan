a=int(input(""))
b=int(input(""))
for num in range(n+1,k):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
             print(num)
