favorite_languages = {
    'jen': 'python',
    'zhao': 'c',
    'yu': 'java',
    'shi': 'java',
}

friends = ['jen', 'zhao', 'yu', 'shi']

# for name in favorite_languages.keys():
#     print(f"Hi,{name.title()}")
#     if name in friends:
#         languages = favorite_languages[name].title()
#         print(f"\t{name.title()},your favorite language is {languages}")

# for name in sorted(favorite_languages.keys()):
# # 反过来，如果想只遍历值的话就把keys改成values就可以
#     print(f"{name.title()}, thanks for taking the poll")

for language in set(favorite_languages.values()):
    print(language.title())