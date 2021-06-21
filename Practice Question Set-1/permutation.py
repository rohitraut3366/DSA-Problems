string = "ABC"


def get_permutations(array):
    perms = []
    permutation_helper(0, array, perms)
    return perms


def permutation_helper(i, array, perms):
    if i == len(array) - 1:
        perms.append((array[:]))
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutation_helper(i + 1, array, perms)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print(get_permutations(list(range(100))))
