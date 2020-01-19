# 1.
# fruits = ['apple', 'orange']
# fruits.append('mango')
# print(fruits)
# O/p:
# ['apple', 'orange', 'mango']

# fruits = ['apple', 'orange']
# fruits.append('mango')
# fruits.append(567)
# print(fruits)
# O/p:
# ['apple', 'orange', 'mango', 567]

# 2.
# fruits = ['apple', 'orange']
# fruits.extend('mango')
# fruits.append(567)
# print(fruits)
# O/p:
# ['apple', 'orange', 'm', 'a', 'n', 'g', 'o', 567]

# 3.
# fruits = ['apple', 'orange']
# fruits.insert(1, 'banana')
# print(fruits)
# O/p:
# ['apple', 'banana', 'orange']

fruits = ['apple', 'orange']
fruits.insert(0, 'banana')
print(fruits)
# O/p:
# ['banana', 'apple', 'orange']
