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



slot_list = []
element = []
pitch = input("Please select a Pitch A or B: ")
team = input("Enter your team name ")
position = input("Select a position ")


element.append(pitch)
element.append(team)
element.append(position)

slot_list.append(element)
print(element)

# text wrap string with a length of 4

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
len_of_string = len(string)
print(len_of_string)
length = 4
output = []
x = 0
y = 0
while x < len_of_string:
    output.append(string[x])
    
    x += 1
    y += 1
    if y == 4:
        output.append("\n")
        y = 0
    
    

print("".join(output))       


#  text wrap with a function 

import textwrap
def wraptext(text, max_width):
    wrapped_text = textwrap.TextWrapper(width=max_width)
    return wrapped_text.wrap(text) # returns a list of the text sliced according to width value

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
width_value = 5

test_1 = wraptext(string, width_value)

print(test_1)

final_result = "\n".join(test_1)
print(final_result)

# joining elements into a string from a list(all elements need be string instances)

list = ["a", "b", "c"]

string = "".join(list)
print(string)

#  Handlig Exceptions 

value_1 = int(input('Enter the 1st number '))
value_2 = int(input('Enter the 2nd number '))

try:
    result = value_1/value_2

except ZeroDivisionError:
    print("Please make sure value_2 is not 0")

else:
    print(f'The answer is {result}')