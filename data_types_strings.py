#String Data Types
name = 'Nikos'
surname = 'Reppas'
#String Type
print(type(name)) #<class 'str'>
print(type(surname)) #<class 'str'>
#String Length
print(len(name)) #5
print(len(surname)) #6
#String Indexing
print(name[0]) #N
print(surname[0]) #R
print(name[-1]) #s
print(surname[-1]) #s
#String Slicing
print(name[1:3]) #ik
print(surname[1:4]) #epp
print(name[:3]) #Nik
print(surname[3:]) #pas
print(name[-3:]) #kos
print(surname[:-3]) #Rep
#String Concatenation
full_name = name + ' ' + surname
print(full_name) #Nikos Reppas
#String Formatting
age = 30
print(f'{name} {surname} is {age} years old') #Nikos Reppas is 30 years old
#String Methods 
print(name.upper()) #NIKOS
print(surname.lower()) #reppas
print(name.title()) #Nikos
print(surname.capitalize()) #Reppas
print(name.replace('N', 'M')) #Mikos    
print(surname.split('p')) #['Re', 'pas']
print(name.find('o')) #3
print(surname.index('p')) #2
print(name.count('o')) #1      
print(surname.count('p')) #2
#String Check
print(name.isalpha()) #True
print(surname.isalpha()) #True
print(name.isdigit()) #False
print(surname.isdigit()) #False
print(name.isalnum()) #True
print(surname.isalnum()) #True
print(name.islower()) #False
print(surname.islower()) #False
print(name.isupper()) #False
print(surname.isupper()) #False
print(name.isspace()) #False
print(surname.isspace()) #False
print(name.startswith('N')) #True
print(surname.endswith('s')) #True
print(name.startswith('n')) #False
print(surname.endswith('p')) #False
#String Escape Characters
print('Hello\nWorld') #Hello
#World
print('Hello\tWorld') #Hello    World
print('Hello\\World') #Hello\World
print('Hello\'World') #Hello'World
print("Hello\"World") #Hello"World
print('Hello\bWorld') #HelloWorld
print('Hello\fWorld') #Hello
#World
print('Hello\rWorld') #World
print('Hello\vWorld') #Hello
print('Hello\0World') #HelloWorld
print('Hello\N{LATIN SMALL LETTER A}') #Hello
print('Hello\U0001F600') #Hello 😀
#Check type
print(type(name) == str) #<class 'str'>
# String assignment with constructor
mike = str('Developer')
print(mike) #Developer