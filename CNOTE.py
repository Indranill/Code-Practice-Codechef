# cook your dish here
t=int(input())
while t>0:
    x,y,k,n=map(int,input().strip().split())
    fl=0
    while n>0:
        pi,ci=map(int,input().strip().split())
        if (ci<=k and pi+y>=x):
            fl=1
        else:
            fl=0
        n-=1
    if fl==1:
        print("Lucky Chef")
    else:
        print("Unlucky Chef")
    t-=1