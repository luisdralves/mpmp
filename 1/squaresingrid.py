L=[]
for i in range(200):
    L.append("no")

for i in range(20):
    for j in range(20):
        if i >= j:
            a = i*i+j*j
            if a < 200:
                L[a] = (i,j)
#            print("[" + str(i) + ", " + str(j) + "] = " + str(a))

for i in range(200):
    print(str(i) + " = " + str(L[i]))