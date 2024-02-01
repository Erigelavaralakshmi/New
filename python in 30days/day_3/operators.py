# Declare your age as integer variable
age = 23
print(age)
#Declare your height as a float variable
height = 4.8
print(height)
#Declare a variable that store a complex number
a = 1+2j
print(type(a))
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    #Enter base: 20
    #Enter height: 10
    #The area of the triangle is 100
base = float(input("Enter a base of the triangle: "))
height = float(input("Enter a height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle: ",area)
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
#Enter side a: 5
#Enter side b: 4
#Enter side c: 3
#The perimeter of the triangle is 12
a = int(input("Enter a side a: "))
b = int(input("Enter a side b: "))
c = int(input("Enter a side c: "))
perimeter = a + b + c
print(f"Perimeter of the triangle:",perimeter)
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter a length of the rectangle: "))
width = int(input("Enter a width of the rectangle: "))
area = length * width
print(f"The area of the rectangle:",area)
perimeter = 2*(length + width)
print(f"Perimeter of the rectangle:",perimeter)
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter  a radius of circle: "))
area = 3.14 * radius * radius
print(f"Area of the circle:",area)
circumference = 2 * 3.14 * radius 
print(f"Circumference of the circle:",circumference)
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a = "python"
b = "dragon"
print(len(a) == len(b))
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
a = "python"
b = "dragon"
# if 'on' in a and b:
#     print(True)
# else:
#     print(False)
print('on' in a and 'on' in b)
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not fullof jargon"
print('jargon' in sentence)
#There is no 'on' in both dragon and python
a = 'dragon'
b = 'python'
print(not 'on' in a and b )
#Find the length of the text python and convert the value to float and convert it to string
text = 'python'
print(len(text))
value = float(len(text))
print(value)
print(str(value))
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number  = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is not even")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
a = 7
b = 3
floor_divison = a // b
if floor_divison == int(2.7):
    print("Yes,it is true")
else:
    print("No,it is false")
#Check if type of '10' is equal to type of 10
print('10 is 10',10 is 10)
#Check if int('9.8') is equal to 10
print(int(9.8) == 10)
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter a rate per hour: "))
pay_of_the_person = hours * rate_per_hour
print(f"The pay of the person is:",pay_of_the_person)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
years = int(input("Enter a years you have lived: "))
seconds_lived = years * 365 * 24 * 60
print(f"Yo have lived for{seconds_lived} seconds.")
#Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# Display the table using operators
for i in range(1, 6):
    row = ""
    for j in range(5):
        # Calculate the power using the exponentiation operator **
        power = i ** j
        row += str(power) + " "
    print(row.strip())  # strip() is used to remove the trailing space in each row


