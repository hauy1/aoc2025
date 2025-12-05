import time
t1 = time.perf_counter()

with open('day5.txt') as f:
    [fresh_ranges, ingredients] = [x.splitlines() for x in f.read().split('\n\n')]

ingredients = list(map(int, ingredients))

intervals = []
for fresh in fresh_ranges:
    intervals.append(list(map(int, fresh.split('-'))))

intervals.sort()

# part 1
count1 = 0
for ingredient in ingredients:
    for low, high in intervals:
        if low <= ingredient <= high:
            count1 += 1
            break

print(f"Part 1: {count1}")

# part 2
count2 = 0
processed = []
cl, ch = intervals[0]

for interval in intervals[1:]:
    a, b = interval
    if a > ch + 1:
        processed.append([cl, ch])
        cl, ch = a, b
        continue
    else:
        if b > ch:
            ch = b
processed.append([cl, ch])
for a, b in processed:
    count2 += b - a  + 1

print(f"Part 2: {count2}")

t2 = time.perf_counter()
print(f"Time: {t2 - t1} seconds")