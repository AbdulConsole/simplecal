#!/usr/bin/python3

print("=======================Simple Calulator=======================")
print("What this Calculator does is just to add two numbers together")
print("              Just A test Cal By AbdulConsole           ")
print("==============================================================")
print("")
print("")
print("What Operation do you want to perform")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("5 = About")

k = str(input("--> "))

if k == '1':
    print("OK, You selected Addition")
    a = int(input("Please enter your first number: "))
    b = int(input("Please enter your second number: "))
    answer = str(a + b)
    print("answer is: "+answer)
elif k == '2':
    print("OK, You selected Subtraction")
    a = int(input("Please enter your first number: "))
    b = int(input("Please enter your second number: "))
    answer = str(a - b)
    print("answer is: "+answer)    
elif k == '3':
    print("OK, You selected Multiplication")
    a = int(input("Please enter your first number: "))
    b = int(input("Please enter your second number: "))
    answer = str(a * b)
    print("answer is: "+answer)
elif k == '4':
    print("OK, You selected Division")
    a = int(input("Please enter your first number: "))
    b = int(input("Please enter your second number: "))
    answer = str(a / b)
    print("answer is: "+answer)
elif k == '5':
    print("This script is written with love for learning at ConsoleHUB")
    print("for: HackerNurain; Bash-Hacker; Hacker_Ridollar; Hacker_Ismail")
    print("written 8-29-2018 12:03AM")
else:
    print("Invalid Entry")
