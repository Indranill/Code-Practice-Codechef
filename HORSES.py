# cook your dish he
tn=int(input())
for i in range(0,tn):
    L1=[]
    n=int(input())
    L=list(map(int,input().split(" ")[0:n]))
    L.sort()
    for k in range(0,len(L)-1):
        L1.append(L[k+1]-L[k])
    print(min(L1))