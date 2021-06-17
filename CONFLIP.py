# cook your dish he
t = int(input())
while t > 0:
    g = int(input())
    for i in range(g):
        i,n,q = map(int,input().split()) 
        if(i == 1):
            h = n//2
            s = n - h
        else:
            s = n//2
            h = n - s
        if(q == 1):
            print(h)
        else:
            print(s)
    t-=1