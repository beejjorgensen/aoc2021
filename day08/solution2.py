"""
1: 2  1x
7: 3  1x
4: 4  1x
2: 5  3x
3: 5
5: 5
6: 6  3x
0: 6
9: 6
8: 7  1x


   0
1     2

   3
4     5

   6

Number to segment map:

0: 0 1 2   4 5 6
1:     2     5    <
2: 0   2 3 4   6
3: 0   2 3   5 6
4:   1 2 3   5    <
5: 0 1   3   5 6
6: 0 1   3 4 5 6
7: 0   2     5    <
8: 0 1 2 3 4 5 6  <
9: 0 1 2 3   5 6

1:     2     5    <
4:   1 2 3   5    <
7: 0   2     5    <
8: 0 1 2 3 4 5 6  <

2: 0   2 3 4   6
3: 0   2 3   5 6
5: 0 1   3   5 6

0: 0 1 2   4 5 6
6: 0 1   3 4 5 6
9: 0 1 2 3   5 6

segment to letter map:

0: abcdefg
1: abcdefg
2: abcdefg
3: abcdefg
4: abcdefg
5: abcdefg
6: abcdefg

0: d
1: e
2: ab
3: f
4: g
5: ab
6: c



Candidate map:

ab     : 1
abef   : 4
abd    : 7
abcedfg: 8

 bcdef   : 2 3 5 < 5 (5. subset of 6)
a cd fg  : 2 3 5 < 2 (6. elimination
abcd f   : 2 3 5 < 3 (1. superset of 1)

abcde f : 0 6 9  < 9 (2. superset of 4)
b cdefg : 0 6 9  < 6 (4. elimination)
abcde g : 0 6 9  < 0 (3. superset of 1)


"""

INPUT="input.txt"
#INPUT="input1.txt"
#INPUT="input2.txt"

number_segment_map = {
    0: {0, 1, 2,    4, 5, 6},
    1: {      2,       5   },  # unique
    2: {0,    2, 3, 4,    6},
    3: {0,    2, 3,    5, 6},
    4: {   1, 2, 3,    5   },  # unique
    5: {0, 1,    3,    5, 6},
    6: {0, 1,    3, 4, 5, 6},
    7: {0,    2,       5   },  # unique
    8: {0, 1, 2, 3, 4, 5, 6},  # unique
    9: {0, 1, 2, 3,    5, 6},
}

to_digit = {}
to_key = {}

def find_by_length(i):
    lengths = { 1: 2, 7: 3, 4: 4, 2: 5, 6: 6, 8: 7 }

    assert(i in lengths)

    target_length = lengths[i]

    for k in to_digit:
        if to_digit[k] is None and len(k) == target_length:
            to_digit[k] = i
            to_key[i] = k

def find_by_subset(key_length, subset, value):
    for k in to_digit:
        if to_digit[k] is None and len(k) == key_length:
            #print(f"Testing for {subset} in {k} for value {value}")
            if set(subset).issubset(set(k)):
                #print("found")
                to_digit[k] = value
                to_key[value] = k
                break

def find_by_superset(key_length, superset, value):
    for k in to_digit:
        if to_digit[k] is None and len(k) == key_length:
            #print(f"Testing for {k} in {superset} for value {value}")
            if set(superset).issuperset(set(k)):
                #print("found")
                to_digit[k] = value
                to_key[value] = k
                break

def process(inp, out):
    count = 0

    for i in inp:
        l = len(i)
        key = "".join(sorted(i))
        to_digit[key] = None

    find_by_length(1);
    find_by_length(7);
    find_by_length(4);
    find_by_length(8);
    find_by_subset(5, to_key[1], 3)
    find_by_subset(6, to_key[4], 9)
    find_by_subset(6, to_key[1], 0)
    find_by_length(6)
    find_by_superset(5, to_key[6], 5)
    find_by_length(2)

    #print(to_key)
    #print(to_digit)

    v = 0

    for k in out:
        k = "".join(sorted(k))
        v *= 10
        v += to_digit[k]

    #print(v)
    return v


total_count = 0


with open(INPUT) as fp:
    for line in fp:

        inp, out = line.split("|")

        inp = inp.strip().split()
        out = out.strip().split()

        total_count += process(inp, out)

print(total_count)
