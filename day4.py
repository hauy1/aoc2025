import time
t1 = time.perf_counter()

with open('day4.txt') as f:
    grid = [list(x) for x in f.read().splitlines()]

#part 1
def neighbors(r, c, array):
    if array[r][c] == '.':
        return False
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(array) and 0 <= nc < len(array[0]):
                if array[nr][nc] == '@':
                    count += 1   
    return count < 4

count1 = 0


for r in range(len(grid)):
    for c in range(len(grid[r])):
        if neighbors(r, c, grid):
            count1 += 1

#part 2
count2 = 0

iteration = 0
update = True
while update:
    update = False
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if neighbors(r, c, grid):
                grid[r][c] = '.'
                count2 += 1
                update = True
    if not update:
        break

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")

t2 = time.perf_counter()
print(f"Time: {t2 - t1} seconds")