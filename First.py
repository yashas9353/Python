from functools import reduce


def fib(n):
    if n <= 0:
        print("Invalid input")
    else:
        a = 0
        b = 1
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)

            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)


def fact(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res


def fact_rec(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_rec(n - 1)


def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)


# Filter

lst = [1, 2, 3, 4, 5, 6]

res = list(filter(lambda n: n % 2 == 0, lst))

print(res)

# map

res1 = list(map(lambda n: n * n, res))

print(res1)

# reduce (it is not a built-in fuction we neede to import it from functools package)

sum1 = reduce(lambda a, b: a + b, res)

print(sum1)
