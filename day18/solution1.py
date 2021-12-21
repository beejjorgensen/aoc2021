import sys

filename = sys.argv[1]

data = []

def parse_line(line):
    i = 0
    sym = None

    def accept(s):
        nonlocal i, sym

        if not isinstance(s, list):
            s = list(s)

        if line[i] in s:
            sym = line[i]
            i += 1
            return True

        return False

    def expect(s):
        if accept(s):
            return True
        print(f"Unexpected symbol: {line[i]}")
        return False

    def expression():
        if accept('0123456789'):
            return int(sym)
        else:
            return pair()

    def pair():
        expect('[')
        left = expression()
        expect(',')
        right = expression()
        expect(']')

        return [left, right]

    return pair()

with open(filename) as fp:
    for line in fp:
        r = parse_line(line)
        data.append(r)

def add_pair(a, b):
    if a is None:
        return b

    return [a, b]

def split(n):
    splitted = False

    def split_r(n, parent=None, my_index=None):
        nonlocal splitted

        if splitted:
            return

        if isinstance(n, int):
            if n > 9:
                parent[my_index] = [n // 2, (n + 1) // 2]
                splitted = True

            return

        split_r(n[0], n, 0)
        split_r(n[1], n, 1)

    split_r(n)

    return splitted

def explode(n):

    prev = None
    prev_idx = None
    exploder = None
    exploded = False
    done = False

    def explode_r(n, parent=None, my_index=None, depth=0):
        nonlocal prev, prev_idx, exploder, exploded, done

        if done:
            return

        if parent is not None and isinstance(parent[my_index], int):
            prev = parent 
            prev_idx = my_index 

        if isinstance(n, int):
            if exploded:
                parent[my_index] += exploder[1]
                done = True

            return

        if depth == 4 and not exploded:
            if isinstance(n, list):
                exploded = True
                exploder = n.copy()

                parent[my_index] = 0

                #print(f"Exploding {n}")
                #print(f"{prev} {prev_idx}")
                if prev is not None:
                    prev[prev_idx] += exploder[0]

                return

        explode_r(n[0], n, 0, depth+1)
        explode_r(n[1], n, 1, depth+1)

    explode_r(n)

    return exploded

def magnitude(n):
    if isinstance(n, int):
        return n

    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

n = None

for d in data:

    n = add_pair(n, d)

    done = False

    #print(n)

    while not done:

        exploded = explode(n)

        while exploded:
            #print(f"Exploded: {n}")
            exploded = explode(n)

        splitted = False

        if split(n):
            #print(f"Split: {n}")
            splitted = True

        done = not exploded and not splitted

#print(n)
print(magnitude(n))

