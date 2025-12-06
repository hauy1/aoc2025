import time
import re

t1 = time.perf_counter()

with open('day6.txt') as f:
    problems = [x.split() for x in f.read().splitlines()]

def prod(a=[]):
    p = a[0]
    for i in range(1, len(a)):
        p *= a[i]
    return p

# part 1
count1 = 0
for i in range(len(problems[0])):
    temp = []
    for j in range(len(problems) - 1):
        temp.append(int(problems[j][i]))
    if problems[-1][i] == '+':
        count1 += sum(temp)
    else:
        count1+= prod(temp)

# part 2 (parsing)
with open('day6.txt') as f:
    data = f.read().splitlines()
    ops = re.split(r'\s(?=[+*])', data[-1])
    widths = [len(op) for op in ops]

processed = []
for item in data[:-1]:
    start_index = 0
    temp = []
    for width in widths:
        temp.append(item[start_index:start_index+width])
        start_index += width+1
    processed.append(temp)

def merge(a=[], b=[]):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

#actually solving part 2
count2 = 0
for i in range(len(processed[0])):
    temp = list(processed[0][i])
    for j in range(1, len(processed)):
        temp = merge(temp, list(processed[j][i]))
    if ops[i].strip() == '+':
        count2 += sum(list(map(int, temp)))
    else:
        count2 += prod(list(map(int, temp)))

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")
t2 = time.perf_counter()
print(f"Time taken: {t2-t1} seconds")