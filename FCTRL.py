# cook your dish he
tc=0
tc=int(input())
while tc:
    n=int(input())
    c=1
    b=0
    while n/c>0:
        c*=5
        b+=(n//c)
    print(b)
    tc-=1
