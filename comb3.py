import itertools

def comb3(k, available, used):
    if len(used) == k:
        yield tuple(used)
    elif len(available) == 0:
        pass
    else:
        head = available.pop(0)
        used.append(head)
        for c in comb3(k, available, used):
            yield c
        used.pop(-1)
        for c in comb3(k, available, used):
            yield c
        available.insert(0, head)

s = 'abcd'
k = 2
mycombs = [c for c in comb3(k, list(s), [])]
print mycombs
itcombs = [d for d in \
    itertools.combinations(list(s), k)]
print itcombs