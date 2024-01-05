def div(a, b):
    print(a / b)


def rev(name):
    return name


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


def deco_rev(func):
    def inner(name):
        lst = list(name)
        lst.reverse()
        name = ''
        for i in lst:
            name += i
        return func(name)

    return inner


rev = deco_rev(rev)

if __name__ == '__main__':
    print(rev("varshitha"))
