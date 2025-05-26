GoodPesel = ""          #User gives PESEL
WrongPesel = "94010705633"
dateofborn = ""
spliteddate = dateofborn.split(".")
yearofborn = spliteddate[2]


print("PESEL Validator: ")
if len(GoodPesel) < 11: #CHECKING THE LENGTH 
    print("Your Pesel hasn't got enough numbers, please check it :)")
else:
    print("CORRECT")
if GoodPesel[:2] == yearofborn[-2:]: #COMPARING FIRST 2 NUMBERS OF PESEL TO LAST 2 NUMBERS YEAROFBORN
    print("CORRECT")
else:
    print("iNCORRECT year of born")
if int(GoodPesel[-2]) % 2 == 1: #GENDER EXEMPTION IF THE -2 NUMBER IS DEIVDED BY 2 AND REST IS 1 THEN ITS MEN OTHERWISE WOMEN
     print("MEN")
else:
     print("WOMEN")
if int(spliteddate[1]) + 20 == int(GoodPesel[2:4]): #CHECKING THE MONTH WE ADD 20 TO DATE BECOUSE 2000-2099 WE HAVE TO ADD 20 ALGORITHMS THINGS 
     print(f'Correct!')
else:
    print(f'Incorrect month of born!')


