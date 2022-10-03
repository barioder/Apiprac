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



word = "EEEEWhat is the   way to HAVE WORK DONEEEEEEEE"

word_2 = word.rstrip('E')
word_3 = word.lstrip("E")
word_4 = word.strip("E")
print(word_2)
print(word_3)
print(word_4)

n = 3
try_list = []
while n != -1:
    try_list.append("i")
    n -= 1

print(try_list)


# def count2(string, substring):

#     string_len = len(string)
    
#     if string.find(substring) != -1:
#         for i in range(0, string_len):
#             start = i
#             string

# counting the number of sub strings in a string
def count2(string, sub_string):

    n = 0
    while sub_string in string:
        new = string.find(sub_string) + len(sub_string)
        string = string[new:]
        n += 1

    return n
    # for i in range(0, string_len):
    #     start = i
    #     result = string[i:].find(sub_string)
    #     if result != -1:
    #         n += 1

word = 'forwardandfowardwardkihhhward'
sub_string = 'ward'
result = count2(word, sub_string)

print(result)

if sub_string in word:
    print('yahhh')