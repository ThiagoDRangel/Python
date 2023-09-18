def mdc(a, b):
    if b == 0:
        return a
    print(mdc(b, a % b))  # test
    return mdc(b, a % b)


mdc(5, 40)  # test
