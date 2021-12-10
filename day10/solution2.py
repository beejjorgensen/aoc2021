INPUT = "input.txt"
#INPUT = "input1.txt"

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
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
                return None

    return list(reversed(stack))


scores = []

with open(INPUT) as fp:
    for line in fp:
        r = testline(line.strip())
        if r is not None:
            score = 0
            for c in r:
                score *= 5
                score += points[c]
            scores.append(score)

scores.sort()

print(scores[len(scores) // 2])

