# 4.2
def make_ruler(n):
    top = ""
    for i in range(n):
        top += "|...."
    top += "|"

    bottom = "0"
    for i in range(1, n + 1):
        bottom += str(i).rjust(5)

    result = top + "\n" + bottom
    return result


def make_grid(rows, cols):
    result = ""
    horz = "+---" * cols + "+"
    vert = "|"
    for _ in range(cols):
        vert += "|".rjust(4)

    for i in range(rows * 2):
        if i % 2 == 0:
            result += horz + "\n"
        else:
            result += vert + "\n"
    result += horz + "\n"

    return result


# 4.3
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 4.4
def fibonacci(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# 4.5
def odwracanie_i(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_r(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_r(L, left + 1, right - 1)


# 4.6
def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        elif isinstance(item, (int, float)):
            total += item
    return total


# 4.7
def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


print(make_ruler(12))
print(make_grid(2, 4))
print(factorial(5))
print(fibonacci(15))

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie_i(L, 2, 5)
print(L)
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie_r(L, 2, 5)
print(L)

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(sum_seq(seq))
print(flatten(seq))
