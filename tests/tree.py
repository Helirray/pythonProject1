import itertools


def remove_first_level(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    return list(itertools.chain(*children))

tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))