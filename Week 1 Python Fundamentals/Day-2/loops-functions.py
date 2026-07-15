#----<<<<<<<Loops>>>>>>>----
#--<<For loop>>--
#Without Loop
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")


#With Loop
for i in range(5):
    print("Welcome!")
    
#Even numbers  
for i in range(1,20,-1):
    if i%2==0:
        print(i)
        
#Odd numbers  
for i in range(1,20,-1):
    if i%2!=0:
        print(i)
        
#Multiplication
number=int(input("please enter the number= "))
for i in range(1,10):
    print(number,"x",i,"=",number*i)
    #print(f"{number} x {i} ={number*i}")  2nd method

#range(Start, Stop, Step)
for i in range(0,11,2):
    print(i)

#for Loop on List
fruits=["Apple","Banana","Orange"]

for fruit in fruits:
    print(fruit)



#<<>>------While Loop------<<>>>
#count =int(input("Please enter the count= "))
count=1
while count <= 5:
    print(count)
    count += 1




