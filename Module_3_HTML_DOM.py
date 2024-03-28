def test(a = 1, b = "Hi", c = 22):
    print(a,b,c)
test()


def factorial(n):
    if n == 1:
        return 1
    fac_n_min_1 = factorial(n=n-1)
    return n * fac_n_min_1
print(factorial(5))
