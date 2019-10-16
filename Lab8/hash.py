import re
import hashlib
password = input("Please enter a password. ")
flag = 0
while True:   
    if (len(password)<8): 
        flag = -1
        print("Must be longer than 8 characters.")
        break
    elif re.search("Bill", password, re.IGNORECASE):
        flag = -1
        print("Password cannot contain your name.")
        break
    elif re.search("sean", password, re.IGNORECASE):
        flag = -1
        print("Password cannot contain my name.")
        break
    elif re.search("Kelly", password, re.IGNORECASE):
        flag = -1
        print("Password cannot contain my name.")
        break
    elif re.search("Wichert", password, re.IGNORECASE):
        flag = -1
        print("Password cannot contain your name.")
        break
    elif re.search("pass", password, re.IGNORECASE):
        flag = -1
        print("Password cannot contain the word 'pass'.")
        break
    elif re.search("word", password, re.IGNORECASE):
        flag = -1
        print("Password cannot contain the word 'word'.")
        break
    elif re.search("password", password, re.IGNORECASE):
        flag = -1
        print("Password cannot contain the word 'password'.")
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        print("Password must contain at least one capital letter.")
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        print("Password must contain at least one number.")
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        print("Password must contain at least one symbol")
        break
    else: 
        flag = 0
        print("Valid Password")
        newPassword = password
        db_pass = newPassword
        h = hashlib.md5(db_pass.encode())
        print(h.hexdigest())
        break
  
if flag ==-1: 
    print("Not a Valid Password")
