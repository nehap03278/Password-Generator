from random import *
special=["!","@","#","$","%","^","&","*","(",")","_","+","=","-",":",";","'","?","<",">",".",",","}","{","[","]","~","|","/"]
print("Enter number of letters to be included in your password")
let_len=int(input())
print("Enter number of digits to be included in your password")
num_len=int(input())
print("Enter number of special characters to be included in your password")
sp_len=int(input())
password=[]
for i in range(let_len):
    letters=randint(65,122)
    password.append(chr(letters))
for i in range(num_len):
    numbers=randint(48,57)
    password.append(chr(numbers))
for i in range(sp_len):
    sp_num=randint(0,25)
    password.append(special[sp_num])
shuffle(password)
final=""
for i in password:
    final+=i 
print(final)