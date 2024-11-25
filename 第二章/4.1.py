# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print (f"I cant wait to see you next trick, {magician.title()}.\n")
# for value in range(1, 5):
#     print(value)

# print(list(range(6)))

# list = []
# for value in range(1, 11):
#     l = value ** 2
#     list.append(l)
# print(list)
#
# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for player in players[:3]:
#     print(player.title())

# my_food = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_food[:]
# print(my_food)
# print(friend_food)

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car =='bmw':
#         print(car.upper())
#     else:
#         print(car.lower())

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# print('mushrooms' in requested_toppings)

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
    print("Finished making your pizza.")
else:
        print("Are you sure?")

