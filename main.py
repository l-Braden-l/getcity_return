#Braden Leach
#january 8 2025
#Return City Function



#----1----#
def get_city():
    return input('Please enter the name of the city you live in: ') 


#----2----#
def get_age():
    return int(input('Please enter your age: '))


#----3----#
def build_output(city,age):
     return f'You live in {city} and you are {age} years old.'
    


age = get_age()
city = get_city()
message = build_output(city,age)

print(message)