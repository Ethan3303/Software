# class cPerson():
   
#     def __init__( self, age, name, gender, address, number, __password):
#      self.age=age
#      self.name=name
#      self.gender=gender
#      self.address=address
#      self.phoneNumber=number
#      self.myPassword=__password
   

# ethan=cPerson(21, "Ethan", "Male", "Lachlan's Gaff", +4486786786946, "LchlanHotty5")
# james=cPerson(21, "James", "Male", "Lachlan's House", +44634576788654, "LchlanScotty5")
# lachlan=cPerson(19, "Lachlan", "Male", "Lachlan's Pad", +445578758678, "LchlanThotty5")
             
# print(f"My name is {ethan.name} I am {ethan.age}. I was born a {ethan.gender} and i live at {ethan.address}. To get a hold of me please call {ethan.phoneNumber}. To log into my account pleae use {ethan.myPassword}")

# print(f"My name is {james.name} I am {james.age}. I was born a {james.gender} and i live at {james.address}. To get a hold of me please call {james.phoneNumber}. To log into my account pleae use {james.myPassword}")

# print(f"My name is {lachlan.name} I am {lachlan.age}. I was born a {lachlan.gender} and i live at {lachlan.address}. To get a hold of me please call {lachlan.phoneNumber}. To log into my account pleae use {lachlan.myPassword}")



class iPerson():

     
    def __init__( self, age, name, gender, address, number, __password):     
     
     self.age=age
     self.name=name
     self.gender=gender
     self.address=address
     self.phoneNumber=number
     self.myPassword=__password  
     
     
inperson=iPerson(int(input("what is your age ")), input("what is your name "), input("what is your gender "), input("what is your address "), int(input("what is your number ")),input("what is your password "))
 
print(f"My name is {inperson.name} I am {inperson.age}. I was born a {inperson.gender} and i live at {inperson.address}. To get a hold of me please call {inperson.phoneNumber}. To log into my account pleae use {inperson.myPassword}")


attempts=3
while True:
   
   newpass=input("to reset password please input original password")
   savedpass=(inperson.myPassword)

   if newpass==savedpass:
      print("That is your old password")
      break

   elif newpass!=savedpass:
      print("that is incorrect try again")
      attempts-=1
      

   
   if attempts<=0:
      print("you have run out of attempts")
      break


   




