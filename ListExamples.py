fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
apple = fruits.count('apple')
print(apple)
mandarina = fruits.count('tangerine')
print(mandarina)
bananaIndex = fruits.index('banana')
print(bananaIndex)
bananaindex4 = fruits.index('banana', 4)  # Find next banana starting a position 4
print(bananaindex4)
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())