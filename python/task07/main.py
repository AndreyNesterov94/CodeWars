# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]


def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    
    result = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i - 1]:
            result.append(iterable[i])
    return result

print(unique_in_order('AAAABBBCCDAABBB'))