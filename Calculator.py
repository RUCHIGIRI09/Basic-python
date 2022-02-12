from operator import truediv
from random import choice
import time     #used for Time

#initial Steps to invite Player in the Game

print("\n ******************* 🎉🎇🎉🎇  WELCOME TO CALCULATOR GAME  🎉🎇🎉🎇 **************************** ")

name=input("ENTER YOUR NAME : ")

print("HELLO 🙋‍ "+name+"  !!!!  ARE YOU READY FOR THIS GAME 😉")

print("Press 'y' for continue 👍 or press 'n' for exit 👎 : ")
on=input()

if on == "n":
    print("THANKS FOR PLAYING! WE EXPECT YOU BACK AGAIN 😊")
    exit()

time.sleep(1)   #This is used to halt the execution of the program for a few seconds.

print("THE GAME IS ABOUT TO START!\n 💃💃  LET'S PLAY   💃💃 ")

time.sleep(1)

while True:
    print(" ~~~~~~~~~~     Operations in our calculator     ~~~~~~~~~~~~ ")

    print("1.  +  : Addition ")                 #it is use for to addition of  two values
    print("2.  -  : Subtraction ")              #it is use for to subtraction of  two values
    print("3.  *  : Multiplication ")           #it is use for to multiply of  two values
    print("4.  /  : Division ")                 #it is use for division and it takes decimal values
    print("5.  // : Double Division ")          #it is use for division and it takes non-decimal values
    print("6.  %  : Modulus ")                  #it is use for division and it takes the remainder of a division
    print("7.  ** : Exponent ")                 #it is use for to takes the first operand to the power of the second operand
    print("8.  0  : Exit " )


    print("Enter your choice : ")
    choice=input()

    if choice == '8':
        break

    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the Second number : "))

    def addition(a,b):
     print(" Result 📢 : ",a + b)
    def subtraction(a,b):
        print(" Result 📢 : ", a - b)
    def multiplication(a,b):
        print(" Result 📢 : ", a * b)
    def single_division(a,b):
        print(" Result 📢 : ", a / b)
    def double_division(a,b):
        print(" Result 📢 : ", a // b)
    def modulus(a,b):
        print(" Result 📢 : ", a % b)
    def exponent(a,b):
        print(" Result 📢 : ", a ** b)

    if choice == '1' :
        c=addition(num1,num2)
        #the addition of two number

    elif choice == '2' :
        c = subtraction(num1,num2)
        #the subtraction of two number

    elif choice == '3' :
        c=multiplication(num1,num2)
        #the multiplication of two number
    elif choice == '4' :
        c = single_division(num1,num2)
        #the division of two number

    elif choice == '5' :
        c = double_division(num1,num2)
        #the division of two number

    elif choice == '6' :
        c = modulus(num1,num2)
        #the modulus of two number

    elif choice == '7' :
        c = exponent(num1,num2)
       #the exponent of two number

    else:
        print("😥😞  Enter the correct choice  😥😞 !!!")




