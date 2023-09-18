def count_1_to_n(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + count_1_to_n(n-1)
    else:
        return count_1_to_n(n-1)