import os.path
import re
print("1. Registration \n")
print ("2. Forgot Password \n")
eFilePath = 'E:\Assignment'
nameOfFile = "My Data"
completeFileName = os.path.join(eFilePath, nameOfFile+".txt")
sChoice = input("Enter your choice : ")
if (sChoice == "1"):
    file1 = open(completeFileName, "a")
    print("You have opted for Registration \n")
    emailAddress = input("Enter the Email address : \n")
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (not (re.fullmatch(emailRegex, emailAddress))):
        print("Not a Valid Email Address \n")
        exit()
    chkAddress = open(completeFileName, "r")
    readFile = chkAddress.read()
    if emailAddress in readFile:
        print("Email already exists")
        exit(0)

    userPasswd = input("Enter the New Password : \n")
    confPasswd = input("Confirm the New Password : \n")


    if (len(userPasswd)<5 or len(userPasswd)>16):
        print ("Password length should be mininum 5 characters and maximum of 16 charachers"+"\n")
        exit()

    if (userPasswd != confPasswd):
        print ("New Password and Confirm Password are not same")
        exit()

    if (not(re.search("[a-z]",userPasswd)) or not(re.search("[A-Z]",userPasswd)) or not(re.search("[!@#$%^&*_-]",userPasswd))):
        print ("Not a Valid Password. \n Password Rules: \n\n Password should have minimum of 5 characters and maximum of 16 characters. \n Password should contain one special character,digit,small case,upper case. \n ")
        exit()

    file1.writelines(emailAddress + "/" + userPasswd)
    file1.writelines("\n")
    file1.close()
if (sChoice == "2"):
    fEmailAddress = input("Enter the valid Email Address : \n")
    file1 = open(completeFileName, "r")
    readLines = file1.read()
    fileContent = readLines.split("\n")

flag = 0

for line in fileContent:
    rLine = line
    #if (not(fEmailAddress.find(rLine))):
    if (line.find(fEmailAddress)) != -1:
        (fEmailid,fPwd) = line.split("/")

        print (fPwd)
        flag = 1
        exit()

if (flag == 0):

    file1 = open(completeFileName, "a")
    print("Invalid Email Address - Please register with New Email Address \n")

    emailAddress = input("Enter the Email address : \n")
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (not (re.fullmatch(emailRegex, emailAddress))):
        print("Not a Valid Email Address \n")
        #exit()

        print(completeFileName)
        chkAddress = open(completeFileName,"r")
        readFile = chkAddress.read()
        if emailAddress in readFile:
            print ("Email already exists")
            exit(0)

        userPasswd = input("Enter the New Password : \n")
        confPasswd = input("Confirm the New Password : \n")

        if (len(userPasswd) < 5 or len(userPasswd) > 16):
            print("Password length should be mininum 5 characters and maximum of 16 charachers" + "\n")
            exit()


        if (userPasswd != confPasswd):
            print("New Password and Confirm Password are not same")
            exit()

        if (not (re.search("[a-z]", userPasswd)) or not (re.search("[A-Z]", userPasswd)) or not (
            re.search("[!@#$%^&*_-]", userPasswd))):
            print("Not a Valid Password. \n Password Rules: \n\n Password should have minimum of 5 characters and maximum of 16 characters. \n Password should contain one special character,digit,small case,upper case. \n ")
            exit()

        file1.writelines(emailAddress + "/" + userPasswd)
        file1.writelines("\n")
        file1.close()

