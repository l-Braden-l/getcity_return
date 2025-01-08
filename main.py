#Braden Leach
#january 8 2025
#Return City Function



#----1----#
def get_city():
    city = input('Please enter the name of the city you live in: ')
    return city


#----2----#
def get_age():
    age = int(input('Please enter your age: '))
    return age


#----3----#
def build_output(city,age):
    message = f'You live in {city} and you are {age} years old.'
    return message 



age = get_age()
city = get_city()
message = build_output(city,age)

print(message)