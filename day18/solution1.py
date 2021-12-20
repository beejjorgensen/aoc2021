def preorder(n, depth=0, exploder=None):
    if isinstance(n, int):
        print(f"{depth}: leaf: {n}")
        return n, exploder
    
    print(f">{depth}: {n}")

    if depth == 4 and exploder is None:
        assert(isinstance(n[0], int) and isinstance(n[1], int))
        print(f"Explode {n}")
        exploder = n
        return 0, exploder

    left, exploder = preorder(n[0], depth+1, exploder)
    right, exploder = preorder(n[1], depth+1, exploder)

    print(f"<{depth}: {n}")

    return [left, right], exploder


"""
inputs = (
    [1,2],
    [[1,2],3],
    [9,[8,7]],
    [[1,9],[8,5]],
)

for i in inputs:
    print("----------")
    preorder(i)
"""

#preorder([[[[[9,8],1],2],3],4])
r, e = preorder([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])

print(f"copy: {r}")
print(f"exploder: {e}")
