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


