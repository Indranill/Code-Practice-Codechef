# cook your dish he
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    jd=list(map(int,input().split()))
    L=[]
    for i in range(1,n+1):
        if i not in jd:
            L.append(i)
    for i in range(0,len(L),2): #for admin taking the job from least index from assistant
        print(L[i],end=" ")
    print()
    for j in  range(1,len(L),2):     #for assistant taking the job from second least index from assistant
        print(L[j],end=" ")
    print()
    
    