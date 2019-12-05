from collections import defaultdict

with open('03.txt') as f:
    wires = dict(enumerate(map(
        lambda line: line.split(','),
        f.readlines())))

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

positions = defaultdict(set)
distances = {}
lengths = defaultdict(dict)

for uid, path in wires.items():
    length = 0
    position = (0, 0)
    for motion in path:
        normal_vector, magnitude = directions[motion[0]], int(motion[1:])
        for n in range(1, magnitude + 1):
            length += 1
            position = (
                position[0] + normal_vector[0],
                position[1] + normal_vector[1])
            positions[position].add(uid)
            lengths[position][uid] = length
            if len(positions[position]) > 1:
                distances[position] = sum(map(abs, position))

manhattan_ranks = list(sorted(distances.items(), key=lambda xy_d: xy_d[1]))
connection_ranks = list(sorted((lengths[xy].values() for xy in distances), key=sum))
print(f'{manhattan_ranks[0][0]} [{manhattan_ranks[0][1]}], {sum(connection_ranks[0])}')
