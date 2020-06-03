import random
import code
print()
password = ""
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
sym = "!£$%^&*()_+-=<>.,/?@;:"
mix = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!£$%^&*()_+-=<>.,/?@;:'
# print(random.choice(nums))

num = input("Enter number of passwords?")
num = int(num)

lens = input("Enter lenght of password?")
lens = int(lens)

if (lens) < 6:
    exit()



nums = input("Enter how many numbers you want in your password?")
nums = int(nums)

let = input("Enter how many numbers you want in your password?")
let = int(nums)



if (nums) > (lens):
    print("")
    exit()

if (nums)+(let)> lens-1:
    print("please make sure it sums up")
    exit()




print("\nYour passwords are here:")    


for pwd in range(num):
    password = ''
  
    

    for l in range(let):
        password += random.choice(chars)
    for i in range(nums):
          password += random.choice(numbers)

    for c in range(lens-(let+nums)):
        password += random.choice(sym)
    print(password)