import random
import code
password = ""
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # defing variable to letters
numbers = '0123456789'# defing variables to numbers
sym = "!£$%^&*()_+-=<>.,/?@;:"# defing symbols to variable

# print(random.choice(nums)) # this is testing to see weather this line of code works

num = input("Enter number of passwords?") # This is so the user can input the number
num = int(num) # This shows the number has to be a int 

lens = input("Enter lenght of password?")
lens = int(lens)

if (lens) < 6: # if it is less than 6 characters then the code will exit and you will have to restart
    print("Use common sense it has to be longer than 6 character")
    exit()



nums = input("Enter how many numbers you want in your password?")
nums = int(nums)

if (nums) > (lens):
    print("Make sure it sums up you twat")
    exit()

let = input("Enter how many letters you want in your password?")
let = int(nums)
if (nums) > (lens):
    print("Make sure it sums up you twat")
    exit()

if (let) > (lens):
    print("Make sure it sums up you twat")
    exit()


if (nums)+(let)> (lens)-1:
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