# string validation 

word = "aBc123"
word2 = "aBc123#"

# check if all are alpanumeric(a-z, A-Z and 0-9)
result = word.isalnum()
result2 = word2.isalnum()
print(result)
print(result2)

print('-------alphabetical------')

word = "ABcef"
word2 = "aBc123#"
#  check if all characters are alphabetical (a-z, A-Z)
result = word.isalpha()
result2 = word2.isalpha()

print(result)
print(result2)

print('------digits-------')
# check if all characters they are digits (0-9)
word = "123453"
word2 = "aBc123#"

result = word.isdigit()
result2 = word2.isdigit()

print(result)
print(result2)

print('------lowerCase-------')
# Check if all characters are lower case 
word = "abcd1253"
word2 = "aBc123#"

result = word.islower()
result2 = word2.islower()

print(result)
print(result2)

print('------any func-------')
#  any() function returns true if an iterable has any item ("False" is not an item)

list1 = [123, 4588, 1551, 55]
list2 = []
print(any(list1), "Has data")
print(any(list2), "Has no data")

# False is not an item
value = [False, False, False]

print(any(value))

value2 = [False, False, True]

print(any(value2))

word = "Arsenal"
list = [i.islower() for i in word ]

print(list)


print(any([i.isupper() for i in word]))
print(any([i.isdigit() for i in word]))
print(any([i.isalnum() for i in word]))


# Text Alignment 
print("---------Text Alignment-----------")

text = "Text to Align" 
width = 100

# Aligned left

result = text.ljust(100, "-")

print(result)

# Aligned right 

result = text.rjust(width, '-')
print(result)

#  center Aligned

result = text.center(width)
print(result)

import random

def pick(x):
    y = random.randint(0, 10)
    if x == y:
        return "You Got the win"
    else:
        return f"{y} it was Please try again"

input_value = int(input("Guess a value between 0 and 10 the computer gets and win: "))

result = pick(input_value)

print(result)

print("jjjjj")