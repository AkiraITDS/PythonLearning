
x = 174458

while x < 174505:
    x +=1
    c = 0
    d1 = 0
    d2 = 0
    for d in range(2, x):
        if x % d == 0:
            c += 1
            if c == 1:
                d1 = d
            if c == 2:
                d2 = d
    if c == 2:
        print(d1,d2) 
        
    
