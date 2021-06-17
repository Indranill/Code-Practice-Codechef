# cook your dish he
t=int(input())
for al in range(t):
    a=[]
    sym=[]
    s=input()
    for i in s:
        if i.isalpha():
            a.append(i)
        elif i==')':
            a.append(sym.pop())
        elif i=='(':
            continue
        else:
            sym.append(i)
    for i in a:
        print(i,end='')
    print()