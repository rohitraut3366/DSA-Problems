def power_set(array, index=None):
    if index is None:
        index = len(array) - 1
    if index < 0:
        return [[]]
    element = array[index]
    subsets = power_set(array, index - 1)
    for i in range(len(subsets)):
        current_sub_set = subsets[i]
        subsets.append(current_sub_set + [element])
    return subsets


print(power_set(['A', 'B', 'C']))
