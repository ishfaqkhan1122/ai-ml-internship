#Class is a blue print 
class Student:
    pass

#Object is an instance of a class.
class Student:
    pass

s1 = Student() #object
s2 = Student() 

print(type(s1))

#Constructor
class Student:
    def __init__(self):           #Constructor init 
        print("Constructor Called")

s1 = Student()  #object 

#Types
#1.Default Constructor
class student:
    def __init__(self):
        self.name="ishfaq khan"
        self.age=20
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=student()
s1.show()


#2.Parameterized Constructor
class student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
    def show(self):
        print(f"the name of student is {self.name} and the age of student is {self.age} and the roll number of the student is {self.roll} ")
s1=student("ishfaq wazir",30,2332)   
s2=student("Hassan",20,4434)
s1.show()
s2.show()


#simple project of Constructor
class car:
    def __init__(self,Brand,Model,Price):
        self.Brand=Brand
        self.Model=Model
        self.Price=Price
    def show_details(self):
        print("Brand:",self.Brand)
        print("Model:",self.Model)
        print("Price:",self.Price)
car1=car(Brand=input("Car Brand:"),Model=input("Car Model:"),Price=int(input("Car Price:")))
car1.show_details()      


#---------Encapsulation-------
class Student:
    def __init__(self):
        self.__marks = 90   # Private variable

    def show_marks(self):
        print(self.__marks)
s = Student()
s.show_marks()
# print(s.__marks)   # Error 


# 1.Public Variable
class Student:
    def __init__(self):
        self.name = "Ali"   # Public Variable
s = Student()
print(s.name)


#2.Protected Variable
class Student:
    def __init__(self):
        self._age = 20   # Protected Variable
s = Student()
print(s._age)


#3.Private Variable
class Student:
    def __init__(self):
        self.__marks = 90   # Private Variable

    def show_marks(self):
        print(self.__marks)
s = Student()
s.show_marks()
# print(s.__marks)   # Error



#Assignment: Bank Account System using Encapsulation
class BankAccount:
    def __init__(self,owner,__balance):
            self.owner=owner
            self.__balance=__balance
    def show__balance(self):
        print("Balance:",self.__balance)
        
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(amount," Rs Deposit Ho Gaye")
        else:
            print("Amount nhi hay")
    
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(amount," Rs withdraw Ho Gaye")
        else:
            print("ap ki account main balance kam hay")

account=BankAccount("ishfaq khan",50000)
account.show__balance()
account.deposit(6000)
account.show__balance()
account.withdraw(26000)
account.show__balance()


#---------Inheritance----------
class vehical:
    def start(self):
        print("Vehical is starting!")

class car(vehical):
    def drive(self):
        print("vehical is runnig!")
c1=car()
c1.start()
c1.drive()