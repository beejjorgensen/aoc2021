position = depth = aim = 0

with open("input.txt") as fp:
    for line in fp:
        direction, distance = line.split()
        distance = int(distance)

        if direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        elif direction == "forward":
            position += distance
            depth += aim * distance

print(position * depth)
