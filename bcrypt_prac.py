import bcrypt

# always has to be a byte string 
password =b"MyPasswordtouse"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

if bcrypt.checkpw(password, hashed):
    print("It is a match")
else:
    print("It didnt match fam")
