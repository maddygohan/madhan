n=int(input(""))
s=input()
s=s.split(' ')
a=[int(i) for i in s]
a.sort()
for i in range(n):
     print(a[i],end=' ')
