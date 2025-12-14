import time
import re
import z3
from collections import deque

t1 = time.perf_counter()
with open('day10.txt') as f:
    manual = f.read().splitlines()

# bfs for part 1
def search(target, button_list=[]):
    queue = deque([0])
    visited = {0}
    depth = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            for button in button_list:
                temp = node ^ button
                if temp in visited:
                    continue
                queue.append(temp)
                visited.add(temp)

                if temp == target:
                    return depth + 1
                
        depth += 1

count1 = 0
count2 = 0
for line in manual:
    diagram, *buttons, joltages = line.split()
    diagram = list(diagram)[1:-1]
    # part 1 solving
    buttons_ints = [sum(map(lambda x: 2**int(x), re.findall(r'[0-9]+', button))) for button in buttons]
    target = sum([2**i for i, light in enumerate(diagram) if light == '#'])
    count1 += search(target, buttons_ints)

    # part 2 solving
    button_list = [set(map(int, button[1:-1].split(','))) for button in buttons]
    joltages = list(map(int, re.findall(r'[0-9]+', joltages)))
    solver = z3.Optimize()
    vars = z3.Ints(f"x{i}" for i in range(len(buttons)))
    solver.add(var >= 0 for var in vars)

    equations = [0 for _ in range(len(joltages))]
    for j, joltage in enumerate(joltages):
        for b, button in enumerate(button_list):
            if j in button:
                equations[j] += vars[b]
    solver.add(equations[i] == joltages[i] for i in range(len(equations)))
    solver.minimize(sum(vars))
    solver.check()
    count2 += solver.model().eval(sum(vars)).as_long()

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")


t2 = time.perf_counter()
print(f"Time taken: {t2 - t1} seconds")