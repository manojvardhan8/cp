def solve(l):
    basis=[]
    for num in l:
        for b in basis:
            num=min(num,num^b)
        if num!=0:
            basis.append(num)
    return (1 << len(basis))
