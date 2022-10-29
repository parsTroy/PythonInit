# temperature = 15
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")


# age = 12
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)


# high_income = True
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")


# successful = False
# for number in range(3):
#     print('Attempt')
#     if successful:
#         print('Successful')
#         break
# else:
#     print('Attempted 3 times and failed')


# for x in range(5):
#     for y in range(3):
#         print(f'({x}, {y})')

# print(type(5))
# print(type(range(5)))

# # Iterable
# for item in shopping_cart:
#     print(item)

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# while True:
#     command = input('>')
#     print('ECHO', command)
#     if command.lower() == 'quit':
#         break

# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         count += 1
#         print(x)

# print(f'We have {count} even numbers')

def greet(first_name, last_name):
    print(f'Hi there {first_name} {last_name}')
    print('Welcome aboard')


greet("Troy", "Parsons")
