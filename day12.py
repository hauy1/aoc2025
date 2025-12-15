import time
t1 = time.perf_counter()
with open('day12.txt') as f:
    stuff = f.read().split('\n\n')
    presents, regions = stuff[:-1], stuff[-1]
    regions = regions.splitlines()

count1 = 0
for region in regions:
    region = region.split(': ')
    grid = list(map(int, region[0].split('x')))
    area = grid[0] * grid[1]
    shape_sizes = 9 * sum(list(map(int, region[1].split())))
    print(area, shape_sizes)
    if area >= shape_sizes:
        count1 += 1

print(count1)


t2 = time.perf_counter()
print(f"Time: {t2 - t1} seconds")