import time
t1 = time.perf_counter()

with open('day8.txt') as f:
    coords = [tuple(map(int, x.split(','))) for x in f.read().splitlines()]

distances = dict()
for i in range(len(coords)):
    for coord in coords[:i] + coords[i+1:]:
        if distances.get((coords[i], coord)) is None and distances.get((coord, coords[i])) is None:
            temp = (coord[0] - coords[i][0])**2 + (coord[1] - coords[i][1])**2 + (coord[2] - coords[i][2])**2
            distances[(coords[i], coord)] = temp

distances = {x: distances[x] for x in sorted(distances, key=distances.get)}

def lookup(coord, circuits=[]):
    for circuit in circuits:
        if coord in circuit:
            return circuits.pop(circuits.index(circuit))
    return [coord]

circuits = []
finish = False
for i, (a, b) in enumerate(distances):
    # part 1 implementation
    if i == 1000:
        part_1 = circuits.copy()
        part_1.sort(key=len, reverse=True)
        print("Part 1:", len(part_1[0]) * len(part_1[1]) * len(part_1[2]))
    for circuit in circuits:
        if a in circuit and b in circuit:
            break
        elif a in circuit:
            circuit += lookup(b, circuits)
            # part 2 implementation
            if len(circuits[0]) == len(coords):
                print("Part 2:", a[0] * b[0])
                finish = True
            break
        elif b in circuit:
            circuit += lookup(a, circuits)
            if len(circuits[0]) == len(coords):
                print("Part 2:", a[0] * b[0])
                finish = True
            break
    else:
        circuits.append([a, b])
        if finish == True:
            break



t2 = time.perf_counter()
print(f"Time taken: {t2-t1} seconds")