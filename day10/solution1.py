INPUT = "input.txt"
#INPUT = "input1.txt"

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0,
}

matching = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def testline(line):
    stack = []

    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(matching[c])
        else:
            v = stack.pop()
            if v != c:
                return c

    return None


total_score = 0

with open(INPUT) as fp:
    for line in fp:
        r = testline(line.strip())
        total_score += points[r]

print(total_score)

