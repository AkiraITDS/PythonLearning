

for x in range(312614, 312652):
    c = 0
    dnum= [0]*6
    for d in range(1, x+1):
        if x % d == 0:
            c += 1
            if c > 6:
                break
            dnum[c-1] = d
    if c == 6:
        for y in range(0,c):
            print(dnum[y], end= ' ')
        print() 
        
