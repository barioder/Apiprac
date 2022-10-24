import bcrypt

# always has to be a byte string 
password =b"MyPasswordtouse"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

if bcrypt.checkpw(password, hashed):
    print("It is a match")
else:
    print("It didnt match fam")

# work factor implication on the hash 
print("work factor implication on the hash ")
import time

start = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
end = time.time()

f = end - start

print(f)

# work factor can be increased by passing a round argument
# Note the difference in the 2 

start = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))
end = time.time()

print(end - start)
