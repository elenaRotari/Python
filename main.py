#DAY1

#1 Exercise day 1 
#print(" Hello World!!")
#input("Hi there, how are you?")


#2 Exercise day 1 
#print("hello " + input("How is your name?"))
#print("") → comment with #

#3 Exercize - day1
#length of  string 
#string =input("whats your name ? ")
#print(len(string))
#shortly
#print(len(input("What is your name? ")))


#4 Exercise day1 

""""a= input("a: ")
b= input("b: ")
# we create a new variable c equap to a input
c=a
# we declare that there a is equal b 
a=b

b=c





print("a: " + a)
print("b: " + b)"""

# Final Exercise day1 #

"""print("Welcome to the Band Name Generator")
city= input("What's name of the city you grew up in? ")
print(city)
pet = input("What's your pet's name? ")
print(pet)
print('Your band name could be '+ city +" " +  pet )"""



#DAY2

#Primitive Data Types 
#print("Hello"[len("Hello")-1])
# Float, Boolean, String. Integer

#Exercise 1 day2
"""
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))
# type_of= print(type(two_digit_number))"""



#Math Operations in Python

# 3 + 5
 #6 - 4
 #3 * 8
 #6 / 3 → result by dividing is always an float type 
 #2 ** 3 → Math.pow() JS
#PEMDAS ()→ **→ */→ +-


#Exercise 2 day 2
# Calcutale BMI 

"""height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


print(int(int(weight) / (float(height) * float(height))))"""

#Number Manipulation 

#print(round(7 / 3, 2)) #the same like in JS with toFixed(), with second param we decide how many int after comma

# FString 
"""score =8
print(f"your score is {score}") # like backtics in JS """

# Exercise 3 day2 


"""age = input("What is your current age? ")

mounth= (90 - int(age)) * 12
weeks= (90 - int(age)) * 52
days= (90 - int(age)) * 365

print(f"You have {days} days, {weeks} weeks, and {mounth} months left")"""


# Final Exercise day2 
 # Tip Calculator 

"""print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
final_amount = round(( bill + (bill * (tip / 100))) / people, 2)
print(f"Each person should pay: ${final_amount}")"""



