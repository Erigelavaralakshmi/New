# 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
first_name = 'Erigela'
# Declare a last name variable and assign a value to it
last_name = 'varalakshmi'
#Declare a full name variable and assign a value to it
full_name = 'Erigela varalakshmi'
#Declare a country variable and assign a value to it
country = 'India'
#Declare a city variable and assign a value to it
city = 'Kurnool'
#Declare an age variable and assign a value to it
age = 23
#Declare a year variable and assign a value to it
year = 2000
#Declare a variable is_married and assign a value to it
is_married = False
#Declare a variable is_true and assign a value to it
is_true = 'Yes'
#Declare a variable is_light_on and assign a value to it
is_light_on = 'Yes'
#Declare multiple variable on one line
print(
    'First_name:',first_name,'\n'
    'Last_name:',last_name,'\n'
    'Full_name:',full_name,'\n'
    'Country:',country,'\n'
    'City:',city,'\n'
    'Age:',age,'\n'
    'Year:',year,'\n'
    'Married:',is_married,'\n'
    'Is_true:',is_true,'\n'
    'Is_light_on:',is_light_on
)

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print(len(first_name and last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

# The radius of a circle is 30 meters.
radius_of_a_circle = 30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * radius_of_a_circle**2
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius_of_a_circle
#Take radius as user input and calculate the area.
radius = int(input("Enter a radius of a circle:"))
area = 3.14 * radius**2
print(area)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter a first_name:")
last_name = input("Enter a last_name:")
country = input("Enter a country name:")
age = int(input("Enter a age:"))
print(first_name,last_name)
print(last_name)
print(country)
print(age)

help('keywords')
help(str)













