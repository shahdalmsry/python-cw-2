my_name = input("what is your name?")
my_age = int( input("how old are you?"))

print(f'My name is {my_name} and I am {my_age} years old')


first_number = int( input("inter the first number"))
secound_number = int( input("inter the secound number"))
operation = input("inter the operation")

if operation =="+":
    print(first_number+secound_number)
elif operation =="-":
    print(first_number-secound_number)
elif operation =="*":
    print(first_number*secound_number)
elif operation =="/":
    print(first_number/secound_number)
else:
    print("none")

bus_capacity = 50

people_in_bus =int(input("How many passengers are in the bus?"))
the_number_oof_people_want_to_ride= input("How many people want to ride the bus?")
empty_seats = (bus_capacity - people_in_bus)

if empty_seats>the_number_oof_people_want_to_ride:
   print(f'thr number of empty seats{10}')
if empty_seats<=the_number_oof_people_want_to_ride:
    print("there_is_no_place")