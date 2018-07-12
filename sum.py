n=int(input())
k=int(input())
l=[]
s=0
for i in range(0,n):
    l.append(int(input()))
for i in range(0,k):
    s=s+l[i]
print(s)
