import itertools

# Infinite Iterators
for i in itertools.count(10, 5):
    if i > 25: break
    print(i)

cycler = itertools.cycle('AB')
print(next(cycler), next(cycler), next(cycler))

print(list(itertools.repeat(7, 3)))

# Terminating Iterators
print(list(itertools.accumulate([1, 2, 3, 4])))

print(list(itertools.chain([1, 2], [3, 4])))

print(list(itertools.compress('ABC', [1, 0, 1])))

print(list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

print(list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(6))))

print(list(itertools.islice(range(10), 2, 8, 2)))

for key, group in itertools.groupby('AAABBC'):
    print(key, list(group))

it1, it2 = itertools.tee([1, 2, 3], 2)
print(list(it1), list(it2))

print(list(itertools.zip_longest('AB', 'XYZ', fillvalue='-')))

# Combinatoric Iterators
print(list(itertools.product('AB', [1, 2])))

print(list(itertools.permutations('ABC', 2)))

print(list(itertools.combinations('ABC', 2)))

print(list(itertools.combinations_with_replacement('ABC', 2)))