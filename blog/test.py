l=[]
for x in range(1000,3000):
    y=str(x)
    if int(y[0])%2==0 and int(y[1])%2==0 and int(y[2])%2==0 and int(y[3])%2==0:
        l.append(y)
        print(" ".join(l))
