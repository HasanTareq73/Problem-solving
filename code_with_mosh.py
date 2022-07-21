# 1. we check in a patient named john smith.
# he's 20 years old and is a new patient


name= "jhon smith"
age= 20
is_new = True


name = input(" what is your name? ")

color = input('What is your faborite color? ')

birth_year= input(" birth year: ")
print(type (birth_year))

age = 2022 - int(birth_year)

print(type(age))


print ("Hi "+ name+ ". your Age is: %d" % age )