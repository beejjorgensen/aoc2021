def explode(n):

    prev = None
    exploder = None
    exploded = False

    def set_prev(n):
        nonlocal prev

        if isinstance(n[0], int) or isinstance(n[1], int):
            prev = n

    def add_prev(v):
        nonlocal prev

        if isinstance(prev[1], int):
            prev[1] += v
        else:
            prev[0] += v

    def explode_r(n, depth=0):
        nonlocal prev, exploder, exploded
        
        if isinstance(n, int):
            return n, depth

        if exploded:
            if isinstance(n[0], int):
                n[0] += exploder[1]
                exploder[1] = 0

            if isinstance(n[1], int):
                n[1] += exploder[1]
                exploder[1] = 0

        set_prev(n)

        if depth == 3 and not exploded:
            exploder_index = None

            if isinstance(n[0], list):
                exploder_index = 0
            elif isinstance(n[1], list):
                exploder_index = 1


            if exploder_index is not None:
                exploded = True
                exploder = n[exploder_index].copy()
                add_prev(exploder[0])
                n[exploder_index] = 0

        explode_r(n[0], depth+1)
        explode_r(n[1], depth+1)

    explode_r(n)

    return exploded

n = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

print(n)
exploded = explode(n)

while exploded:
    print(n)
    exploded = explode(n)
