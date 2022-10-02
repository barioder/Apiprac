# how to use the map function

def multi(a):
    return (a*a)

values = (1,2,3,4)

output = map(multi, values)


print(list(output))

word = '2,2526 5,8 7 9 2'
separated = word.split(',')
print(separated)


# swap case (convert uppercase to lower case in a string and vise versa)

def swap_case(word):
    return word.swapcase()

our_word = "This WORD Has To CHanGE"

result = swap_case(our_word)

print(result)


# split and join a string 

word ="This is our word"

word = word.split(" ")
print(word)
joined = "-".join(word)

print("This is joined by -", joined)

joined2 = '@'.join(word)

print('This is joined by @', joined2)

word, *balance = "words to work with".split(" ")

print(word, balance)

word, *balance = "wordonlymm".split(" ")

print(word, balance)

if len(balance) == 0:
    print("0000000")


# edit string 

def change_value(string_value, position, item):
    list_value = list(string_value)
    list_value[position] = item
    result = "".join(list_value)
    return  result

string = "ABCDSFGHI"
pos = 4
value = "E"

result = change_value(string, pos, value)

print(result)

# finding 

word = 'forwardandfowardward'
sub_string = 'ward'

print(word.find(sub_string))
print(word.find("word"))
def count(string, sub_string):
    indexs = []
    value_1 = string.find(sub_string)
    if value_1 != -1:
        indexs.append(value_1)
        sub_length = len(sub_string)
        new_start = value_1 + (sub_length)
        value_2 = string[new_start:].find(sub_string)
        if value_2 != -1:
            indexs.append(value_2)

            return len(indexs)

        return len(index)
    

    return 0

result = count(word, sub_string)
result1 = count("word", "nowardstouse")

print(result)

print(result1)




