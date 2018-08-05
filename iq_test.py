def is_even(num):
    return not num % 2


def even_count(num):
    return sum(map(is_even, num))


def iq_test(numbers):
    numbers = [int(x) for x in numbers.split()]
    pos = 0
    if even_count(numbers) > 1:
        pos = [i for (i, j)in enumerate(numbers, start=1) if not is_even(j)][0]
    else:
        pos = [i for (i, j)in enumerate(numbers, start=1) if is_even(j)][0]
    return pos
