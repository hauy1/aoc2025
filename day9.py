import time
from collections import defaultdict, deque
t1 = time.perf_counter()

with open('day9.txt') as f:
    coords = [tuple(map(int, x.split(','))) for x in f.read().splitlines()]

# part 1, basically a one-liner
areas = sorted([[(abs(r1 - r2) + 1) * (abs(c1 - c2) + 1), (r1, c1), (r2, c2)] for i, (r1, c1) in enumerate(coords) for r2, c2 in coords[:i]], reverse=True)
print(f"Part 1: {areas[0][0]}")

# part 2, coordinate compression
row_coords = sorted({r for r, _ in coords})
col_coords = sorted({c for _, c in coords})
row_indexes = {r: row_coords.index(r)*2 + 1 for r in row_coords}
col_indexes = {c: col_coords.index(c)*2 + 1 for c in col_coords}

# making the comrpessed grid: '#' for red/green, '.'' for no color
grid = [['.'] * (len(col_coords) * 2 + 1) for _ in range(len(row_coords) * 2 + 1)]
for (r1, c1), (r2, c2) in zip(coords, coords[1:] + [coords[0]]):
    cr1, cr2 = sorted([row_indexes[r1], row_indexes[r2]])
    cc1, cc2 = sorted([col_indexes[c1], col_indexes[c2]])
    for cr in range(cr1, cr2 + 1):
        for cc in range(cc1, cc2 + 1):
            grid[cr][cc] = '#'

compressed = {}
for (r, c) in coords:
    cr, cc = row_indexes[r], col_indexes[c]
    compressed[(r, c)] = (cr, cc)


# floodfill to find the outside
def neighbors(x, y, grid=[]):
    n = []
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if i == x and y == j:
                continue
            if 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1:
                n.append((i, j))
    return n

outside = {(0, 0)}
queue = deque(outside)
while queue:
    r, c = queue.popleft()
    for nr, nc in neighbors(r, c, grid):
        if grid[nr][nc] == '.' and (nr, nc) not in outside:
            outside.add((nr, nc))
            queue.append((nr, nc))

inside = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in outside:
            grid[i][j] = '#'
            inside.add((i, j))

# checking border of rectangles
for area, *coords in areas:
    a, b = map(lambda x: compressed[x], coords)
    ar, ac = a
    br, bc = b
    c = sorted([ac, bc])
    d = sorted([ar, br])
    temp = set()
    for i in range(c[0], c[1] + 1):
        temp.add((ar, i))
        temp.add((br, i))
    for j in range(d[0], d[1] + 1):
        temp.add((j, ac))
        temp.add((j, bc))
    if not set.intersection(temp, outside):
        print(f"Part 2: {area}")
        break


t2 = time.perf_counter()
print(f"Time taken: {t2-t1} seconds")