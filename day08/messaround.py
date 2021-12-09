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
           

for k0, s0 in number_segment_map.items():
    print(f"{k0} is a subset of:")
    for k1, s1 in number_segment_map.items():
        if k0 == k1: continue
        if s0.issubset(s1):
            print(f"    {k1}")

print()

for k0, s0 in number_segment_map.items():
    print(f"{k0} is a superset of:")
    for k1, s1 in number_segment_map.items():
        if k0 == k1: continue
        if s0.issuperset(s1):
            print(f"    {k1}")



"""
abcdefg 8

abcdef  0 6 9
bcdefg
abcdeg

bcdef 2 3 5
acdfg
abcdf

abef  4

abd 7

ab  1

"""
