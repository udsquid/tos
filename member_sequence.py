from itertools import *

members = [1003, 829, 979, 672, 959, 1159]
samples = []
for p in permutations(members[1:-1]):
    # print members[:1] + list(p) + members[-1:]
    res = members[:1] + list(p) + members[-1:]
    samples.append(res)
for s in samples:
    print s
