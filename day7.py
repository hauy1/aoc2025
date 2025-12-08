import time
t1 = time.perf_counter()

with open('day7.txt') as f:
    grid = [list(x) for x in f.read().splitlines()]

# part 1
beams = [grid[0].index("S")]
count1 = 0
for r in range(1, len(grid)):
    temp = []
    for beam in beams:
        if grid[r][beam] == '^':
            count1 += 1
            temp.append(beam - 1)
            temp.append(beam + 1)
        else:
            temp.append(beam)
    beams = list(set(temp))
print(f"Part 1: {count1}")

# part 2
beams = [grid[0].index("S")]
ways = {(0, beams[0]): 1}
for r in range(1, len(grid)):
    temp = {}
    for beam in beams:
        if grid[r][beam] == '^':
            for nb in [beam - 1, beam + 1]:
                if (r, nb) not in temp:
                    temp[(r, nb)] = ways[(r - 1, beam)]
                else:
                    temp[(r, nb)] += ways[(r - 1, beam)]
        else:
            if (r, beam) not in temp:
                temp[(r, beam)] = ways[(r - 1, beam)]
            else:
                temp[(r, beam)] += ways[(r - 1, beam)]
    ways = temp
    beams = list(set(b for _, b in ways))
print(f"Part 2: {sum(ways.values())}")


t2 = time.perf_counter()
print(f"Time: {t2-t1} seconds")