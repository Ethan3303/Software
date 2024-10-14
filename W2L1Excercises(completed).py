#Excercise 1:
userNumber = int(input("Enter a number, any number: "))
startNumber = userNumber
print("Now add 1...")
userNumber += 1
print(f"You now have { userNumber }... ")
print("Double it...")
userNumber *= 2
print(f"You now have { userNumber }... ")
print("Now add 4...")
userNumber += 4
print(f"You now have { userNumber }... ")
print("Now divide by 2...")
userNumber /= 2
print(f"You now have { userNumber }... ")
print("Now take away the number you first thought of...")
userNumber = userNumber - startNumber
print(f"You now have three : { userNumber }")

#In this excercise I was able to shorten the comparison by using the equals to make operators which removes the need to type the string value.

#Excercise 2:

age = int(input( "Enter your age: " ))
    
if (age >= 20 and age <= 29):
    print("You are in your twenties")

elif (age>=13 and age <=19):
    print("you are a teenager")
else:
    print("you are not in your twenties")
    
#Excercise 3:
counter = 1
while (counter <= 10):
 print( counter, end="," )
 #with the addition of end= it places the numbers horrizontally rather than vertically
 counter+=1

 print("\n")

#Excercise 4:

counter1=100
while (counter1 <= 100):
# while (counter1 >= 0):
    #does in reverse order
    print(counter1, end=",")
    counter1-=2
print("\n")
#same code made but this time it only displays even numbers

#Excercise 5:

import keyboard
from IPython.display import clear_output
print("welcome to 'Tragic The Gathering' a fantasy game that involves dragons warriors and so much more")
keyboard.read_event(suppress=True) 

    
    


CharacterType=["Warrior", "Scout"]
while True:
    option=input("Do you want to be a scout or a warrior? Please decide using the first leter of your choice! ").lower()
    if option=="w":
        print("You have chosen", CharacterType[0])
        break
    elif option=="s":
        print("Your have chosen", CharacterType[1])
        break
    else:
        print("invlald option")

    

print("\nAt the start of your adventure, you first reach a huge stone door, which wont open. A huge voice booms out: \n", 
      "\nANSWER THIS RIDDLE TO PASS SAFELY: WHAT CAN YOU CATCH BUT CANNOT THROW?\n",
      "\nYour options are as followed:\n1: A baby.\n2: A cold\n3: A Ball\n4: Carl\n")

characterHealth = 100

while True:
  try:  
    ans=int(input("Your answer is: \n"))
    
    if ans==1:
        print("wtf? no?? Try agan.\n")
        characterHealth-=50
      

    elif ans==2:
        print("You may pass\n")
        break

    elif ans==3:
        characterHealth-=50
        print("That is not the answer, try again\n")
        
    elif ans==4:
        print("I wish, but no")
        characterHealth-=50

    if characterHealth<=0:
        print("your journey has come to an end")
        break

  except ValueError:
      print("please input the number choice")
print("you continue your journey")










