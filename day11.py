import time
from functools import lru_cache
t1 = time.perf_counter()

servers = {}
with open('day11.txt') as f:
    lines = [x.split(': ') for x in f.read().splitlines()]

for line in lines:
    servers[line[0]] = line[1].split()

@lru_cache
def search(initial=str, final=str):
    if initial == final:
        return 1
    return sum(search(node, final) for node in servers.get(initial, []))

# part 1
print(f"Part 1: {search('you', 'out')}")
# part 2
print(f"Part 2: {search('svr', 'fft') * search('fft', 'dac') * search('dac', 'out')}")

t2 = time.perf_counter()
print(f"Time taken: {t2 - t1} seconds")