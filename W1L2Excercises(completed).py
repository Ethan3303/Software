#LAB 2 EXCERCISES
#Excercise 1:
itemPrice = float(input("Enter the item price: "))
itemTax = itemPrice*0.2
#the item tax will now calcualte 20% of the value of the item price to gve an accurate 20% additional tax
totalPrice = itemPrice + itemTax
print("Tax on the item is", itemTax)
print("Total item price is", totalPrice)
#The total price was named wrong on the print function so it had nothing to call back on
itemAmount = int(input("How many items did you get?: "))
#final display will calculate the tax added item and multiply it by the initiger inputted
finalDisplay=totalPrice * itemAmount
print("your balance comes to ", finalDisplay)

#Excercise 2:
year = int(input("Enter the year you were born: "))
if year % 4 == 0:
 print("You were born in a leap year")
#OPTIONAL: made it so an inputted year will say if theyre older or younger
if year == 2003:
 print("You were born the same year as me")
elif year < 2003:
 print("you are older than me")
elif year > 2003:
 print("You are younger than me")

else:
 print("you were not born on a leap year")

#Excercise 3: 
half = float(1/2) 
print(f"One half (1/2) = {half}")

print(type(half))
# fixed so a float will be displayed instead of an integer which rounded it down to zero and also printed "half" datatype

#Excercise 4:
#celcius is now a float input so you can accurately input the tempreture to get a better result when  
celcius = float(input("What temperature in celcius is it today "))
Fahrenheit = celcius*(9/5)+32
#It'll display the letters for different tempreture types when printed
print(f"{celcius}C {Fahrenheit}F")

#Excercise 5:
option=int(input("Input 1 for £ input 2 for $ "))
pound1=1
dollar1=2
if option==pound1:
    Pound=float(input("How many £ do you have "))
    exchangeRate=float(input("What is the current exchange rate "))
    Dollar=Pound*exchangeRate
    print("you can convert this to $", Dollar)

elif option==dollar1:
    Dollar=float(input("How many $ do you have "))
    exchangeRate=float(input("What is the current exchange rate "))
    Pound=Dollar*exchangeRate
    print("you can convert this to £", Pound)

else:
    print("that is an invalid option")

#Excerxise 6:
print("please input 5 numbers")
num1=int(input("1: "))
num2=int(input("2: "))
num3=int(input("3: "))
num4=int(input("4: "))
num5=int(input("5: "))

highest=max(num1,num2,num3,num4,num5)

print("the highest number inputted is ", highest)

#Excercise 7:

#i couldnt figure this one out, though it was fun trying 

#Extension Activity:

#example of variables:
exampleFloat=5.2
exampleInt=6
exampleString="hello"

# #Example of Opperators

# #arithmatic operators
x1=exampleFloat*exampleInt
y1=exampleFloat+exampleInt
z1=exampleFloat%exampleInt

print(x1, y1, z1)

# #Assignment operators
exampleFloat += 3

exampleInt *= 12
print(exampleInt, exampleFloat)

# #Conditions, comparison and logical operators:

if exampleFloat > exampleInt:
    print("the float is greater than the int")

elif exampleFloat < exampleInt:
    print("the int is greater than the float")

elif exampleFloat == exampleInt:
    print("these options are the same")

else: 
    print("somethings gone wrong")

if exampleFloat and exampleFloat >= 10:
    print("theyre higher than 10")

else:
    print("they are less than 10")

#input example
input1 = input("please type anytything to show the example working ")

print("what you wrote was:", input1)