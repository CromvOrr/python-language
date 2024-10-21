# 2.10
line = ('Lorem\n'
        'ipsum\n'
        'dolor\n'
        'sit\n'
        'amet,\n'
        'consectetur\n'
        'adipiscing\n'
        'elit.')
words_total = len(line.split())
print(words_total)

# 2.11
word = 'Lorem'
print('_'.join(word))

# 2.12
line = ('Lorem\n'
        'ipsum\tdolor sit\n'
        'amet,\tconsectetur adipiscing\n'
        'elit.')
words = line.split('\n')
first = ''.join([word[0] for word in words])
last = ''.join([word[-1] for word in words])
print(first)
print(last)

# 2.13
words = line.split()
length_total = sum(len(word) for word in words)
print(length_total)

# 2.14
longest = max(words, key=len)
longest_length = len(longest)
print(longest)
print(longest_length)

# 2.15
L = [2517, 38, 289, 7, 658, 3453, 5052, 4, 85, 9921]
digits = ''.join(str(digit) for digit in L)
print(digits)

# 2.16
line = 'Lorem GvR ipsum dolor sit amet, consectetur adipiscing GvR elit.'
print(line.replace('GvR', 'Guido van Rossum'))

# 2.17
words = line.split()
alphabetically = sorted(words)
by_length = sorted(words, key=len)
print(alphabetically)
print(by_length)

# 2.18
number = 102203044050660708809
number_str = str(number)
zeros = number_str.count('0')
print(zeros)

# 2.19
L = [517, 38, 289, 7, 658, 453, 810, 4, 85, 992]
blocks = ''.join(str(number).zfill(3) for number in L)
print(blocks)
