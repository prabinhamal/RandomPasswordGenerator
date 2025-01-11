
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


def valueInput():
    loop=True
    loop1=True
    while loop:
        try:
            UserSelectNumber=""
            UserSelectNumber=input("You want to select '🔒1234' numbers in your password,(yes/no): ")
            if UserSelectNumber.lower() == "yes":
                loop=False
                passwordAlpha["Selectnumber"]=True
            elif UserSelectNumber.lower() == "no":
                loop=False
                passwordAlpha["Selectnumber"]=False
            else:
                print("Please enter 'yes' or 'no' ")
                continue
        except ValueError:
            print("Please enter 'yes' or 'no'")
            continue
        while loop1:
            try:
        
                
                UserSelectSpecialchar=input("You want to select '🔒#$&*!@' special characters in your password (yes/no): ")
            
                if UserSelectSpecialchar.lower() == "yes":
                    loop1=False
                    passwordAlpha["SelectspecialChar"]=True
                elif UserSelectSpecialchar.lower() == "no":
                    loop1=False
                    passwordAlpha["SelectspecialChar"]=False
                else:
                    print("Please enter 'yes' or 'no' ")
                    continue
            except ValueError:
                print("Please enter 'yes' or 'no' 123")
                continue
   


# print(passwordAlpha["number"])

def RandomNumberGenerator(To,From):
    return random.randint(To, From)

def RandomLetterselect(alphabet):
    return random.choice(alphabet)
def listAlpha():
    count=1
    alphalist=""
    for i in passwordAlpha:
        if passwordAlpha[i]:
            # print(alphalist)
            count=str(count)
            alphalist=alphalist + count
        count=int(count)
        count+=1
    return alphalist

# def RandomNumber(Password_len, alpha):
#     for i in range(0, Password_len):
#         passwordRan=passwordRan + alpha(RandomNumberGenerator(0, len(alpha)))
#     return passwordRan

print("🔒🔒🔒🔒🔒🔒🔒 Random Password Generator 🔒🔒🔒🔒🔒🔒🔒")
# ### user select
valueInput()

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
    
    RandomPassword=""
    randomAlpha=listAlpha()
    for i in range(0,password_len):
        randomNumber=RandomLetterselect(randomAlpha)
        if randomNumber == "1":
            RandomPassword=RandomPassword +RandomLetterselect(letterLower) ### random letter select lower case character
        elif randomNumber == "2":
            RandomPassword=RandomPassword +RandomLetterselect(letterUpper) ### random letter select upper case character
            
        elif randomNumber == "3":
            RandomPassword=RandomPassword +RandomLetterselect(number)
        elif randomNumber == "4":
            RandomPassword=RandomPassword +RandomLetterselect(specialChar)
        else:
            continue
            
    return RandomPassword
        
    
RandomPassword1=Password_generator(Password_length) ### call Password_generator() function to generate random password

### password print

print("Your Random Password is 🔐🗝️ :   ",RandomPassword1)
