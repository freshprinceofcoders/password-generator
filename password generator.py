
import random
import code
password = ""
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # defing variable to letters
numbers = '0123456789'# defing variables to numbers
sym = "!£$%^&*()_+-=<>.,/?@;:"# defing symbols to variable



# print(random.choice(nums)) # this is testing to see weather this line of code works

 
lens = input("Enter lenght of password?") # This is so the user can input the number
lens = int(lens)# This shows the number has to be a int casting parsing converting

if (lens) < 6: # if it is less than 6 characters then the code will exit and you will have to restart
    print("Use common sense it has to be longer than 6 character")
    exit()


let = input("Enter how many letters you want in your password?")
let = int(let)

if (let) > (lens):
    print("Make sure count of letters is less than the of the password")
    exit()


nums = input("Enter how many numbers you want in your password?")
nums = int(nums)

if (nums) > (lens):
    print("Make sure count of numbers is less than the of the password")
    exit()


if (nums)+(let)>lens-1:
    print("please make sure it sums up to one less than lenght of password")
    exit()
   

print("\nYour passwords are here:")    


password = ''  

for l in range(let):
    password += random.choice(chars)
    
for i in range(nums):
    password += random.choice(numbers)

for c in range(lens-(let+nums)):
    password += random.choice(sym)
    
print(password)

