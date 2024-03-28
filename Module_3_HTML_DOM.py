def test(*args):
    print(*args)


test(1,'Hi',True)


def factorial(n):
    if n == 0:
        return 1
    fac_n_min_1 = factorial(n=n - 1)
    return n * fac_n_min_1


print(factorial(5))
