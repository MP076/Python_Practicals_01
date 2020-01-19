# 1.
# first = [1, 2, 3]
# print(first)
# O/p:
# [1, 2, 3]

# first = [1, 'abc', 3]
# print(first)
# O/p:
# [1, 'abc', 3]

# first = [1, 'abc', [30, 2.4, 'Joey']]
# print(first)
# O/p:
# [1, 'abc', [30, 2.4, 'Joey']]

# 2.
# first = [1, 'abc', [30, 2.4, 'Joey']]
# print(first[1])
# O/p:
# abc

# first = [1, 'abc', [30, 2.4, 'Joey']]
# print(first[2])
# O/p:
# [30, 2.4, 'Joey']

# first = [1, 'abc', [30, 2.4, 'Joey']]
# print(first[0:2])
# O/p:
# [1, 'abc']

# first = [1, 'abc', [30, 2.4, 'Joey']]
# print(first[1:3])
# O/p:
# ['abc', [30, 2.4, 'Joey']]

# first = [1, 'abc', [30, 2.4, 'Joey'], 4.5, 30]
# print(first[2:])
# O/p:
# [[30, 2.4, 'Joey'], 4.5, 30]

# first = [1, 'abc', [30, 2.4, 'Joey'], 4.5, 30]
# print(first[:4])
# O/p:
# [1, 'abc', [30, 2.4, 'Joey'], 4.5]

# 3.
# first = [1, 'abc', [30, 'Joey'], 4.5, 30]
# string1 = first[1]
# print(string1)
# O/p:
# abc

# 4.
# first = [1, 'abc', [30, 'Joey'], 4.5, 30]
# string1 = first[2][1]
# print(string1)
# O/p:
# Joey

first = [1, 'abc', [30, 'Joey'], 4.5, 30]
string1 = first[1][2]
print(string1)
# O/p:
# c
