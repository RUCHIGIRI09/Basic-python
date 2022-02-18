def factors(value):
    prime = []
    factor = 2
    while value > 1:
        if value % factor == 0:
            prime.append(factor)
            value /= factor
        else:
            factor += 1
    return prime
        