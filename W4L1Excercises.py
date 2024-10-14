#Excercise 1:
def WaitForEnter():
  input("\nPress Enter to Continue...")
print("")
#Excercise 2:

def DrawHorizonLine():

 for line in range (80):
   line=("-")
   print(line, end="")
print("")

#Excercise 3:
def ReadIntFromUser():
  num1 = int(input("What number do you want: "))
  print("You chose",num1)

#Excercise 4:


ReadIntFromUser()
DrawHorizonLine()


# def howLong():
#   inputted=int(input("How long do you want the line "))
#   for amount in range(inputted):
#     amount="-"
#     print(amount, end="")
# print("")


  

# ReadIntFromUser()
# DrawHorizonLine()
# WaitForEnter()
# howLong()
# # DrawHorizonLine()
# WaitForEnter()
# howLong()


