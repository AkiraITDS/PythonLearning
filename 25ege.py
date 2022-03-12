x = 700000
n = 0 
m = 0
while n<5:
    x +=1
    dmin = x
    dmax = 0
    for d in range(2, x):
        if x % d == 0:
            if d < dmin:
                dmin = d
            elif d > dmax:
                dmax = d
    if dmax > 0:
        m = dmax + dmin
    if m % 10 == 8:
        n +=1
        print(x,m)