import math


def count_even_list(list_number):
    count = 0
    for item in list_number:
        if item % 2 == 0:
            count += 1
    return count


def count_odd_list(list_number):
    count = len(list_number) - count_even_list(list_number)
    return count


def count_prime_list(list_number):
    count = 0
    for item in list_number:
        if is_prime(item):
            count += 1
    return count


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        return sqrt_div(n)


def sqrt_div(n):
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
        return True
