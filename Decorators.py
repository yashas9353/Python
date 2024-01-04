def div(a, b):
    print(a / b)


def rev(name):
    print(name)


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


div = smart_div(div)

div(2, 4)

rev = deco_rev(rev)
rev('yashas')
