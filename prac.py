# how to use the map function

def multi(a):
    return (a*a)

values = (1,2,3,4)

output = map(multi, values)


print(list(output))

word = '2,2526 5,8 7 9 2'
separated = word.split(',')
print(separated)


