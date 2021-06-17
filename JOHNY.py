# cook your dish he
nt=int(input())

for i in range(0,nt):
    n=int(input())
    L=list(map(int,input().strip().split(" ")[0:n]))
    k=int(input())
    v=L[k-1]
    L.sort()
    pos=L.index(v)
    print(pos+1)