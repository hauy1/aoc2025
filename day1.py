import time
t1 = time.perf_counter()

with open('day1.txt') as f:
    instructions = f.read().splitlines()

# part 1
count = 0
dial = 50
for instruction in instructions:
    if instruction[0] == 'L':
        dial -= int(instruction[1:])
    else:
        dial += int(instruction[1:])
    if dial % 100 == 0:
        count += 1

print(f"Part 1: {count}")

# part 2
count = 0
dial = 50
for instruction in instructions:
    dir = instruction[0]
    units = int(instruction[1:])

    if dir == 'L':
        end = (dial - units) % 100
        if dial != 0:
            for i in range(100):
                dial -= 1
                if dial == 0:
                    units -= i + 1
                    count += 1
                    break
    
    else:
        end = (dial + units) % 100
        for i in range(100):
            dial += 1
            if dial == 100:
                units -= i + 1
                count += 1
                break
    
    count += units // 100
    dial = end

print(f"Part 2: {count}")
t2 = time.perf_counter()
print(f"Time: {t2 - t1} seconds")