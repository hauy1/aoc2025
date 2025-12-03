import time
t1 = time.perf_counter()

with open('day3.txt') as f:
    banks = [list(map(int, x)) for x in f.read().splitlines()]

total1 = 0
total2 = 0
for bank in banks:

    # part 1
    tens = max(bank[:-1])
    units = max(bank[bank.index(tens) + 1:])
    total1 += tens*10 + units

    # part 2
    joltage = 0
    index = 0
    for i in range(12, 0, -1):

        size = len(bank) 
        
        if size == i: #did not include this on my solve, added this afterwards for slight optimization
            joltage = joltage*(10**i) + int(''.join([str(x) for x in bank]))
            break

        digit = max(bank[:size-i+1])
        bank = bank[bank.index(digit)+1:]
        joltage = joltage * 10 + digit

    total2 += joltage

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")
t2 = time.perf_counter()
print(f"Time: {t2 - t1} seconds")