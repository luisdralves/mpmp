def next(triangle):
    a = abs(triangle[0]-triangle[1])
    b = abs(triangle[1]-triangle[2])
    c = abs(triangle[2]-triangle[0])
    return [a, b, c]


for a in range(14):
    for b in range(14):
        for c in range(14):
            triangle = [a, b, c]                        #All possible triangles with numbers from 0 to 14
            if sum(triangle) == 14:                     #If the starting numbers sum is 14, ignore
                continue
            for n in range(16):                         #Check 16 iterations 
                triangle = next(triangle)
                if n > 8 and sum(triangle) != 14:       #If after 8 iterations the sum different than 14 at least once, ignore
                    continue
            if sum(triangle) == 14:
                print(a, b, c)                          #Print the solution