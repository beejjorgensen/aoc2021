def explode(n, depth=0, exploder=None):
    # Leaf, check for right explosion
    if isinstance(n, int):
        result = n

        # Explode right
        if exploder is not None:
            result += exploder[1]
            exploder[1] = 0  # Prevent subsequent adds

        return result, exploder

    if depth == 4 and exploder is None:
        assert(isinstance(n[0], int) and isinstance(n[1], int))
        print(f"Explode {n}")
        exploder = n.copy()
        return 0, exploder

    left, exploder = explode(n[0], depth+1, exploder)
    right, exploder = explode(n[1], depth+1, exploder)

    # Check for previous explosion to propagate left
    if exploder is not None:
        if isinstance(n[0], int):
            # Explode left
            left += exploder[0]
            exploder[0] = 0  # Prevent subsequent adds

    return [left, right], exploder


n = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

while True:
    r, e = explode(n)

    if e is None:
        break

    print(f"old: {n}")
    print(f"new: {r}")

    n = r
