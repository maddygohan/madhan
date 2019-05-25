n=int(input(""))
m=int(input(""))
for num in range(n,m+1):
    order=len(str(num))
    sum=0
    temp=num
    while(temp>0):
      dig=temp%10
      sum+=dig**order
      temp//=10
    if(num==sum):
     print(num)
