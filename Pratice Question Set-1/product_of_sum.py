def product_of_sum(arr, n, level):
    if n == 0:
        return 0
    elif isinstance(arr[0], list):
        return (level + 1) * (
            product_of_sum(arr[0], len(arr[0]), level + 1)) + product_of_sum(arr[1:], len(arr[1:]), level)
    elif n == 1:
        return arr[0]
    else:
        return arr[0] + product_of_sum(arr[1:], n - 1, level)


print(product_of_sum([1, [2, [3]], [4, [3, [4]], 4]], 3, 1))
