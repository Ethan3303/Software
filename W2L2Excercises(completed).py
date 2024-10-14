#Excercise 1:
# For loops

for i in range(0,10):
    print(i, end=",")


for j in range(9,49):
    if j%2!=0:
        print(j, end=", ")

for h in range(9,49):
    if h%2==0:
        print(h, end=", ")

#excercise 2:

while True:
     p=input("Are you sure you want to delete the record? (Y/N)").lower()
     if p=="y":
        print("Record was deleted")
        break
        
     elif p =="n":
        print("Record was no deleted")
        break
    
     else:
         print("Sorry, you must answer 'y' or 'n'.")
       
# print("goodbye")

#excercise 3:
while True:
  try:
    year=int(input("what year were you born: "))

    if year >= 1900 and year <=2011:
        print("you are", 2011-year, "years old")
        break

    else: 
       print("that is not a valid year")

  except ValueError:
    print("That is not a number")

#Excercise 4:

while True:
     try:
        userNum1 = float(input("Enter first number: "))
        userNum2 = float(input("Enter second number: "))
        

    
        
        userchoice = input("what calculation are you wanting (-,+,%,*)")
        if userchoice == "+":
                userTotal = userNum1 + userNum2
                print(f"{userNum1} + {userNum2} = {userTotal}")
                

        elif userchoice == "-":
                userTotal = userNum1 - userNum2
                print(f"{userNum1} - {userNum2} = {userTotal}")
                               

        elif userchoice == "%":
                userTotal = userNum1 % userNum2
                print(f"{userNum1} % {userNum2} = {userTotal}")
                        

        elif userchoice == "*":
                userTotal = userNum1 * userNum2
                print(f"{userNum1} * {userNum2} = {userTotal}")
                        
                            
        else: 
                print("invalid option")
                    
        
                    
        yesNo = input("Do you want another go (y/n): ").lower() #.lower function added to make any input lower case and valid  
                                
        while (yesNo != 'y' and yesNo != "n"):      
                print("invalid input")                                                                      
                                
                                        
        if (yesNo == "n"):
                print("we hope you enjoyed the calculator")
                break
                                            
                      
               

     except ValueError:
      print("has to be a number")
#i tried to make it so there was no possible way to continue with errors but i ended up not being able to and it either ignoring it or getting stuck on a while loop and not going to be beginning
#added to make the program continue to work even if a string is inputted instead of a float 

# Excercise 6:
import calendar
from datetime import datetime
numberDays = calendar.monthrange(2011, 10)[1] 
print(numberDays)

# Excercise 7:
while True:
 try:  
    vyear = int(input("Enter a year: "))
    while (vyear >=1 and vyear <=9999):
     for month in range(1,13):
        months=calendar.monthrange(vyear, month)[1]
        print(f"Month {month}\n{months} days\n") 
     break
    else:
        print("Sorry, please enter a valid year between 1 and 9999")
 except ValueError:
     print("Sorry, enter a valid year")
     


 year = 2023
 month = 10
 day = 15 

 monthName = datetime(2023, 10, 1).strftime("%B")

 shortDayName = datetime (year, month, day).strftime("%a")

 dayName = datetime (year, month, day).strftime("%A")
 print(f"Month Name: { monthName }")
 print(f"Short Day Name: { shortDayName }")
 print(f"Full Day Name: { dayName }")

#excercise 8:
 while True:
  try:  
    vyear = int(input("Enter a year: "))
    if (vyear >=1 and vyear <=9999):
        for month in range(1,13):
            days=calendar.monthrange(vyear, month)[1]
            monthname=datetime(vyear, month, 1).strftime("%B")
            print(monthname)          
           
            for day in range(1,days+1):
                dayname=datetime(vyear, month, day).strftime("%a")
                print(f"{dayname} {day}", end=", ")    
            print()
 

    else:
        print("Sorry, please enter a valid year between 1 and 9999")
  except ValueError:
     print("Sorry, enter a valid year")

#excercise 9
  while True:
   try: 
    bday=int(input("birth day number:"))
    bmonth=int(input("birth month number:"))
    byear=int(input("birth year number:"))

    birthdayday=datetime(byear,bmonth,bday).strftime("%A")

    print(birthdayday)
   except ValueError:
       print("not a valid number")