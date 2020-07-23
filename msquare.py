def printsquare(a, b, c, d, e, f, g, h, i):
    a = pow(a,2)
    b = pow(b,2)
    c = pow(c,2)
    d = pow(d,2)
    e = pow(e,2)
    f = pow(f,2)
    g = pow(g,2)
    h = pow(h,2)
    i = pow(i,2)
    print(str(a) + "  " + str(b) + "  " + str(c) + "  " + str(a+b+c))
    print(str(d) + "  " + str(e) + "  " + str(f) + "  " + str(d+e+f))
    print(str(g) + "  " + str(h) + "  " + str(i) + "  " + str(g+h+i))
    print(str(a+d+g))
    print("   " + str(b+e+h))
    print("      " + str(c+f+i))

for a in range(20):
    for b in range(20):
        for c in range(20):
            for d in range(20):
                for e in range(20):
                    for f in range(20):
                        for g in range(20):
                            for h in range(20):
                                for i in range(20):
                                    sum = pow(a,2)+pow(b,2)+pow(c,2)
                                    total = 8
                                    if pow(d,2)+pow(e,2)+pow(f,2) == sum:
                                        total-=1
                                    if pow(g,2)+pow(h,2)+pow(i,2) == sum:
                                        total-=1
                                    if pow(a,2)+pow(d,2)+pow(g,2) == sum:
                                        total-=1
                                    if total > 7:
                                        break
                                    if pow(b,2)+pow(e,2)+pow(h,2) == sum:
                                        total-=1
                                    if total > 7:
                                        break
                                    if pow(c,2)+pow(f,2)+pow(i,2) == sum:
                                        total-=1
                                    if total > 7:
                                        break
                                    if pow(a,2)+pow(e,2)+pow(i,2) == sum:
                                        total-=1
                                    if total > 7:
                                        break
                                    if pow(g,2)+pow(e,2)+pow(c,2) == sum:
                                        total-=1
                                    if total < 2:
                                        printsquare(a, b, c, d, e, f, g, h, i)
                                    