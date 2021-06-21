def get_nth_fib(F0, F1, n):
    if n == 0:
        return F0
    return get_nth_fib(F1, F1 + F0, n - 1)


for i in range(100):
    print(get_nth_fib(0, 1, i), end=" ")
