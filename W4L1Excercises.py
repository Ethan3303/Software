#Excercise 1:
def WaitForEnter():
  input("\nPress Enter to Continue...")
print("")
# Excercise 2:

def DrawHorizonLine():
 width=int(input(""))
 for line in range (width):
   line=("-")
   
   print(line, end="")
print("")

#Excercise 3:
def ReadIntFromUser():
  linewidth = int(input("What number do you want: "))
 
# ReadIntFromUser()

#Excercise 4:


# ReadIntFromUser()
# DrawHorizonLine()

# created a second one
def howLong():
  inputted=int(input("How long do you want the line "))
  for amount in range(inputted):
    amount="-"
    print(amount, end="")
print("")


  

# ReadIntFromUser()
# DrawHorizonLine()
# WaitForEnter()
# howLong()
# DrawHorizonLine()
# WaitForEnter()
# howLong()

#Excercise 5:
# while True:
#      try:
#         userNum1 = float(input("Enter first number: "))
#         userNum2 = float(input("Enter second number: "))
        

#         userchoice = input("what calculation are you wanting (-,+,/,*,%,**,***)")
        
#         def plus():
#          if userchoice == "+":
#                 userTotal = userNum1 + userNum2
#                 print(f"{userNum1} + {userNum2} = {userTotal}")
                
#         def minus():
#           if userchoice == "-":
#                 userTotal = userNum1 - userNum2
#                 print(f"{userNum1} - {userNum2} = {userTotal}")
                               
#         def divide():
#           if userchoice == "/":
#                 userTotal = userNum1 % userNum2
#                 print(f"{userNum1} / {userNum2} = {userTotal}")
                        
#         def times():
#           if userchoice == "*":
#                 userTotal = userNum1 * userNum2
#                 print(f"{userNum1} * {userNum2} = {userTotal}")

#         def modulus():
#           if userchoice =="%":
#               userTotal = userNum1 % userNum2
#               print(f"{userNum1} % {userNum2} = {userTotal}")

#         def squared():
#           if userchoice == "**":
#                 userTotal = userNum1 * userNum1
#                 print(f"{userNum1} ** {userNum1} = {userTotal}")
                

#         def cubed():
#           if userchoice == "***":
#                 userTotal = userNum1 * userNum2 * userNum1
#                 print(f"{userNum1} * {userNum1} * {userNum1}= {userTotal}")
       
#         plus()
#         minus()             
#         divide()                   
#         times()
#         modulus()
#         squared()
#         cubed()       
        
                    
#         yesNo = input("Do you want another go (y/n): ").lower() #.lower function added to make any input lower case and valid  
                                
#         while (yesNo != 'y' and yesNo != "n"):      
#                 print("invalid input")                                                                      
                                
                                        
#         if (yesNo == "n"):
#                 print("we hope you enjoyed the calculator")
#                 break
                                                                  
#      except ValueError:
#       print("has to be a number")


