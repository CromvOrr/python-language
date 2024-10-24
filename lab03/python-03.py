# 3.1
# a) Kod nie jest poprawny ze względu na złe zastosowanie średników
#    oraz niepotrzebne nawiasy wokół warunku if
# b) Kod kod niepoprawny, ponieważ brakuje odpowiedniego
#    wcięcia po dwukropku w pętli for i po warunku if
# c) Pomijając spację pomiędzy print a nawiasem, kod jest poprawny

# 3.2
# a) Metoda sort() sortuje listę w miejscu, po przypisaniu
#    L = L.sort(), L będzie miała wartość None
# b) Po lewej stronie przypisania mamy dwie zmienne, a po prawej trzy wartości
# c) Nie można zmieniać poszczególnych wartości w Tuples
# d) Brak indeksu 3 w liście, powinniśmy użyć append()
# e) Próba użycia append() na stringu
# f) Błąd, pow() potrzebuje co najmniej dwóch argumentów

# 3.3
def _3():
    tmp = ""
    for i in range(31):
        if i % 3 != 0:
            tmp = tmp + str(i) + " "
    print(tmp)


# 3.4
def _4():
    while True:
        try:
            x = input("Insert a number: ")
            if x.lower() == 'stop':
                return 0
            x = float(x)
            print(f"{x}\t\t{x ** 3}")
        except ValueError:
            print("Invalid input, try again.")


# 3.5
def _5(length=12):
    top = ""
    for i in range(length):
        top += "|...."
    top += "|"

    bottom = "0"
    for i in range(1, length + 1):
        bottom += str(i).rjust(5)

    result = top + "\n" + bottom
    return result


# 3.6
def _6(width=4, height=2):
    result = ""
    horz = "+---" * width + "+"
    vert = "|"
    for _ in range(width):
        vert += "|".rjust(4)

    for i in range(height * 2):
        if i % 2 == 0:
            result += horz + "\n"
        else:
            result += vert + "\n"
    result += horz + "\n"

    return result


# 3.8
def _8(a="aabbccdd", b="ccddeeff"):
    a = list(a)
    b = list(b)
    if " " in a:
        a.remove(" ")
    if " " in b:
        b.remove(" ")
    common_el = list(set(a) & set(b))
    all_el = list(set(a) | set(b))

    return common_el, all_el


# 3.9
def _9(seq):
    sums = [sum(seq) for seq in seq]
    return sums


# 3.10
def _10(roman="MMXXIV"):
    roman2int_map = dict([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000)
    ])
    total = 0
    previous = 0

    for char in reversed(roman):
        value = roman2int_map[char]
        if value < previous:
            total -= value
        else:
            total += value
        previous = value

    return total


_3()
# _4()
print(_5())
print(_6())
print(_8())
sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print(_9(sequence))
print(_10())
