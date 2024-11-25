bicycles = ['giant', 'trek', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])
# print(bicycles[-1])
# message = f"my first bicycle was a {bicycles[-1].title()}"
# print(message)
moto = ['bmw', 'yamaha', 'ducati']
# print(moto[0])
moto[0] = 'nihao'
# print(moto[0])
moto.append('hello')
print(moto)
moto.insert(1,'world')
cycle = moto.pop() #默认弹出最后一个元素
print(moto)
print(cycle)
# del moto[1]
# print(moto)
moto.remove("ducati")
print(moto)
