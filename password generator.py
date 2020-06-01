import random
import code
print()
password = ""
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"£$%^&*()_+-=<>.,/?@;:'


num = input("Enter number of passwords?")
num = int(num)

lens = input("Enter lenght of password?")
lens = int(lens)

if (lens) < 6:
    exit()

print("\nYour passwords are here:")    

for pwd in range(num):
    password = ''
    for c in range(lens):
        password += random.choice(chars)
    print(password)
