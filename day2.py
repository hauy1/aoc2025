with open('day2.txt') as f:
    ranges = [tuple(map(int, x.split('-'))) for x in f.read().split(',')]


total1 = 0
total2 = 0


for start, end in ranges:
    for i in range(start, end + 1):

        num = str(i)
        s = len(str(i))
        
        # part 1
        if s % 2 == 0:
            if num[:s//2]*2 == num:
                total1 += i

        # part 2
        for j in range(1, s//2 + 1):
            if s % j == 0 and num[:j]*(s//j) == num:
                total2 += i
                break

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")