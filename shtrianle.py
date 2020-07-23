import math 

sht = []

def findDupes(sht, dup):
    dup.sort()
    doit = True
    for ori in sht:
        if ori == dup:
            doit = False
    if doit:
        sht.append(dup)

for a in range(1,200):
    for b in range(1,200):
        for c in range(1,200):
            perimeter = a + b + c
            p = perimeter / 2
            if a < p and b < p and c < p:
                area = math.sqrt(p*(p-a)*(p-b)*(p-c))
                if area == perimeter:
                    print("---")
                    print(a)
                    print(b)
                    print(c)
                    print(area)
                    print(perimeter)
                    findDupes(sht,[a,b,c])
print(sht)
                                    