# def greet_user(user_name,age = '18'):
#     """显示简单的问候语"""
#     print(f"Hello!{user_name},{age}")
#
# greet_user(user_name = 'zhaosyuhi')
#
# def make_pizza(size, *toppings):
#     """打印顾客点的所有配料"""
#     print(f"Make a {size}-inch pizza with the following {toppings}")
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms','green peppers','extra cheese')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')