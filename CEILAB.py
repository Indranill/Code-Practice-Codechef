50# cook your code here
from sys import stdin,stdout
l = [int(i) for i in stdin.readline().split()]
x=l[0]-l[1]
if (x%10==9):
    x-=1
else:
    x+=1
print(x)