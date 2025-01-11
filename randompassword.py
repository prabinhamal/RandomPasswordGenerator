
# import random
# password1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+\\|{ };:/?.><~,`"

# passwordord = str()
# password_length = 10
# for i in range(0, password_length):
#     random_selection=random.randint(0, len(password1))
#     passwordord =passwordord + password1[random_selection]
# print("Your Random password :  ", passwordord)

import random
letterLower="abcdefghijklmnopqrstuvwxyz"
letterUpper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
specialChar="!@#$%^&*()-_=+\\|{ };:/?.><~,`"

passwordAlpha={
    "Selectlower": True, 
    "Selectupper": True,
    "Selectnumber": False,
    "SelectspecialChar": False,

}

# print(passwordAlpha["number"])

def RandomNumberGenerator(To,From):
    return random.randint(To, From)

def RandomLetterselect(alphabet):
    return random.choice(alphabet)

# def RandomNumber(Password_len, alpha):
#     for i in range(0, Password_len):
#         passwordRan=passwordRan + alpha(RandomNumberGenerator(0, len(alpha)))
#     return passwordRan

print("🔒🔒🔒🔒🔒🔒🔒 Random Password Generator 🔒🔒🔒🔒🔒🔒🔒")
# ### user select
try:
    UserSelectNumber=input("You want to select '🔒1234' numbers in your password,(yes/no): ")
    if UserSelectNumber.lower() == "yes":
        passwordAlpha["Selectnumber"]=True
    elif UserSelectNumber.lower() == "no":
        passwordAlpha["Selectnumber"]=False
    else:
        print("Please enter 'yes' or 'no' ")
        exit()
    UserSelectSpecialchar=input("You want to select '🔒#$&*!@' special characters in your password (yes/no): ")

    if UserSelectSpecialchar.lower() == "yes":
        passwordAlpha["SelectspecialChar"]=True
    elif UserSelectSpecialchar.lower() == "no":
        passwordAlpha["SelectspecialChar"]=False
    else:
        print("Please enter 'yes' or 'no' ")
        exit()
except ValueError:
    print("Please enter 'yes' or 'no' ")
    exit()

### password length input

try:
    Password_length=  int( input("Enter your password length, Grater then 4: "))
except ValueError:
    print("Please enter a number ")
    exit()

if Password_length<4:
    print("Enter your password length is not greater than 4")
    exit()


# ### generate password

def Password_generator(password_len):
    sumSignal=passwordAlpha["Selectlower"]+passwordAlpha["Selectupper"]+passwordAlpha["Selectnumber"]+passwordAlpha["SelectspecialChar"]
    RandomPassword=""
    for i in range(0,password_len):
        randomNumber=RandomNumberGenerator(1,sumSignal) ### random number select between 1 to user selected alphabet 

        if randomNumber == 1:
            RandomPassword=RandomPassword +RandomLetterselect(letterLower) ### random letter select lower case character
        elif randomNumber == 2:
            RandomPassword=RandomPassword +RandomLetterselect(letterUpper) ### random letter select upper case character
        elif randomNumber == 3:
            RandomPassword=RandomPassword +RandomLetterselect(number)
        elif randomNumber == 4:
            RandomPassword=RandomPassword +RandomLetterselect(specialChar)
    return RandomPassword
        
    
RandomPassword1=Password_generator(Password_length) ### call Password_generator() function to generate random password

### password print

print("Your Random Password is 🔐🗝️ :   ",RandomPassword1)

