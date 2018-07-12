n=int(input())
s=input()
s=s.split()
sum=0
for i in s:
  sum=sum+int(i)
if(sum==0):
  print("0")
else:
  s.sort()
  t="".join(s)
  t=t[::-1]
print(t)
