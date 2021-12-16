class MinHeap:
    def __init__(self, values=None, key=None):
        if values is None:
            self.data = []
        else:
            self.build(values, key)

    @classmethod
    def _get_parent(cls, i):
        return (i - 1) // 2

    @classmethod
    def _get_left(cls, i):
        return i * 2 + 1

    @classmethod
    def _get_right(cls, i):
        return (i + 1) * 2

    @classmethod
    def _ident_key(cls, e):
        return e

    def add(self, e, key=None):
        if key is None: key = MinHeap._ident_key

        # add to end
        self.data.append(e)
        i = len(self.data) - 1  # index of just-added

        # swap up
        pi = MinHeap._get_parent(i)

        while i > 0 and key(self.data[i]) < key(self.data[pi]):
            self.data[i], self.data[pi] = self.data[pi], self.data[i]
            i = pi
            pi = MinHeap._get_parent(i)

    def is_empty(self):
        return len(self.data) == 0

    def remove(self, key=None):
        if len(self.data) == 0:
            return None

        if key is None: key = MinHeap._ident_key

        # Save the min
        top = self.data[0]

        # Replace it with the end
        old_end = self.data[-1]
        self.data[0] = old_end
        self.data.pop()

        if len(self.data) > 0:
            self.heapify(0, key)

        return top

    def heapify(self, i, key=None):
        if key is None: key = MinHeap._ident_key

        li = MinHeap._get_left(i)
        ri = MinHeap._get_right(i)
        smallest = i

        if li < len(self.data) and key(self.data[li]) < key(self.data[smallest]):
            smallest = li

        if ri < len(self.data) and key(self.data[ri]) < key(self.data[smallest]):
            smallest = ri

        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.heapify(smallest, key)

    def build(self, values, key=None):
        if key is None: key = MinHeap._ident_key

        self.data = values

        self.full_heapify(key)

    def full_heapify(self, key):
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self.heapify(i, key)


if __name__ == "__main__":
    mh = MinHeap()

    for i in [5,234,1324,6,7,56,324,324,45,56,76,7,56,56,5,65,6,6]:
        mh.add(i)

    result = []
    while not mh.is_empty():
        result.append(mh.remove())

    print(result)

    fn = lambda x: -x

    mh = MinHeap([5,234,1324,6,7,56,324,324,45,56,76,7,56,56,5,65,6,6], key=fn)

    result = []
    while not mh.is_empty():
        result.append(mh.remove(key=fn))

    print(result)

