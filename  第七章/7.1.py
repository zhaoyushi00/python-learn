# age = input("请输入年龄：")
# age = int(age)
# print(age)
# print(age>18)

# num = 1
# while num <= 100:
#     print(num)
#     num += 1

# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue
#
#     print(num)

# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("验证用户：" + current_user)
#     confirmed_users.append(current_user)
# for user in confirmed_users:
#     print(user)
#
# pets = ['cat','dog','dog','cat','cat','dog']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("请输入你的名字：")
    response = input("请输入你的爱好：")
    responses[name] = response
    repeat = input("是否继续（yes/no）：")
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print(f"name: {name}  like: {response}")