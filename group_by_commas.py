def group_by_commas(n):
    n = str(n)
    result = n[:len(n) % 3]+"," if len(n) % 3 != 0 else n[:len(n) % 3]
    rest, i = n[len(n) % 3:], 0
    while (i < len(rest)):
        result += rest[i:i+3] + ","
        i += 3
    return result[:-1]
