#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = 'Thirty', 'Days', 'Of', 'Python'
result = ' '.join(string)
print(result)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string = 'Coding', 'For' , 'All'
result = ' '.join(string)
print(result)
# Declare a variable named company and assign it to an initial value "Coding For All".Print the variable company using print().
company = "Coding For All"
print(company)
# Print the length of the company string using len() method and print().
company = "Coding For All"
print(len(company))
# Change all the characters to uppercase letters using upper() method.
company = "coding for all"
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
company = "CODING FOR ALL"
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = "CODING FOR ALL"
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
company = "coding for all"
print(company.strip('coding'))
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
company = "coding for all"
print(company.index('coding'))
#Replace the word coding in the string 'Coding For All' to Python.
string = 'coding for all'
print(string.replace('coding','python'))
# Change Python for Everyone to Python for All using the replace method or other methods.
string = 'python for everyone'
print(string.replace('everyone','all'))
# Split the string 'Coding For All' using space as the separator (split()) .
string = 'coding for all'
print(string.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(','))
# What is the character at index 0 in the string Coding For All.
string = 'coding for all'
print(string[0])
# What is the last index of the string Coding For All.
string = 'coding for all'
print(string[-1])
# What character is at index 10 in "Coding For All" string.
string = 'coding for all'
print(string[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = 'Python For Everyone'
print(string[0],string[7],string[11])
# Create an acronym or an abbreviation for the name 'Coding For All'.
string = 'coding for all'
print(string[0],string[7],string[11])
# Use index to determine the position of the first occurrence of C in Coding For All.
string = 'coding for all'
print(string.index('c'))
# Use index to determine the position of the first occurrence of F in Coding For All.
string = 'coding for all'
print(string.index('f'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'coding for all'
print(string.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.strip('because because because'))
# Does ''Coding For All' start with a substring Coding?
string = 'coding for all'
print(string.startswith('coding'))
# Does 'Coding For All' end with a substring coding?
string = 'coding for all'
print(string.endswith('coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip())
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
string = 'thirty_days_of_python'
print(string.isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = ' # '.join(python_libraries)
print(joined_string)
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.')
print('I just wonder, \nwhat is next.')
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\t        Age\t  Country\t   City')
print('Asabeneh\t','250\t', 'finland\t','helsinki')
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of the circle with radius 10 is {area} meters square.")
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
result = a+b
result = a-b
result = a*b
result = a/b
result = a%b
result = a//b
result = a**b
print(f"{a} + {b} = {result}")
print(f"{a} - {b} = {result}")
print(f"{a} * {b} = {result}")
print(f"{a} / {b} = {result}")
print(f"{a} % {b} = {result}")
print(f"{a} // {b} = {result}")
print(f"{a} ** {b} = {result}")

