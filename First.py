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


print(fact_rec(4))
