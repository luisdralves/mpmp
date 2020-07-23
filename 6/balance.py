from tqdm import tqdm

solutions = []

for i in tqdm(range(1, 100000)):
    for j in range(i, 100000):
        steps = 0
        day1 = i
        day2 = i+j
        day3 = day1+day2
        solution = [day1, day2, day3]
        while day3 < 1000000:
            steps+=1
            day1 = day2
            day2 = day3
            day3 = day1 + day2
            solution.append(day3)
            if day3 == 1000000 and steps > 15:
                solutions.append((solution, steps))


solutions.sort(key=lambda sol: sol[1])
print(solutions)