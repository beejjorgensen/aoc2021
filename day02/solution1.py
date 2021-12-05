position = depth = 0

with open("input.txt") as fp:
    for line in fp:
        direction, distance = line.split()

        distance = int(distance)

        if direction == "forward":
            position += distance
        elif direction == "up":
            depth -= distance
        elif direction == "down":
            depth += distance

print(position * depth)

