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

                #prev[prev_idx] += exploder[0]
                return
        
        explode_r(n[0], n, 0, depth+1)
        explode_r(n[1], n, 1, depth+1)

    explode_r(n)

    return exploded

n = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
#n = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

print(n)
exploded = explode(n)

while exploded:
    print(n)
    exploded = explode(n)
