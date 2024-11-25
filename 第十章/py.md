# python部分总结

- 主要记录的是python与之前学的语言的不同之处

1. #### 函数总结

   ```python
   首字母大写: name.title()
   删除右边空格（暂时）:name.rstrip()
   删除左边空格（暂时）:name.lstrip()
   删除前缀（暂时）:name.removeprefix()
   在列表末尾处添加:list.append('1')
   在任意位置进行插入元素:list.insert(0,'A')
   删除元素（永久）:del list[0]
   删除尾端元素并将其弹出(也可根据下标进行删除):last = list.pop()
   根据列表中的值删除元素:list.remove('A')
   按首字母排序（永久）:list.sort()
   按首字母排序（临时）:list.sorted()
   反向打印:list.reverse()
   列表长度:len(list)
   生成数值:range(1,5)并不包含5 range（6）是0~5
   提取字典中的一个键值对:favorite_languages.items()
   输入函数:input('请输入: ')
   索引加遍历:enumerate(list)
   ```

2. #### 在字符串中使用变量

   ```python
   last_name = shi
   first_name = zhaoyu
   full_name = f"{first_name} {last_name}"
   print(f"Hello, {full_name}")
   ```

3. #### 索引

   索引为-1时是提取列表中的最后一个元素

   ```python
   list = ['1', '2', '3']
   list[-1]的值是3
   ```

4. #### For循环

   ```python
   magicians = ['alice', 'david', 'carolina']
   for magician in magicians:
       print (f"I cant wait to see you next trick, {magician.title()}")
   ```

   - 不要忘记给需要循环的代码语句进行缩进
   - 不要忘记加后面的冒号

5. #### 使用range（）函数创建数值列表

   可以使用 list() 函数将 range() 函数的结果直接转换为列表。如果将 range() 作为 list() 的参数，输出的将会是一个数值列表

   ```python
   print(list(range(6)))
   ```

   ```python
   list = []
   for value in range(1, 11):
       l = value ** 2
       #两个星号表示乘方
       list.append(l)
   print(list)
   ```

   第二个程序是创建一个列表，其中包含前十个证书的平方

6. #### 列表推导式

   ```python
   squares = [value ** 2 for value in range(1,11)]
   print(squares)
   ```

   跟5中的range（）函数例子程序

7. #### 切片

   ```python
   players = ['charles', 'martina', 'michael', 'florence', 'eli']
   print(players[0:3])
   ```

   - players[0:3]输出的是下标为0、1、2的三个元素
   - 如果冒号左边没有数字，会从列表的第一位开始输出，同理右边
   - players[-3 : ]是打印最后三个元素的意思

   ##### 切片遍历

   ```python
   players = ['charles', 'martina', 'michael', 'florence', 'eli']
   for player in players[:3]:
       print(player.title())
   ```

   ##### 复制列表

   ```python
   my_food = ['pizza', 'falafel', 'carrot cake']
   friend_food = my_food[:]
   print(my_food)
   print(friend_food)
   ```

8. #### If语句

   ```python
   cars = ['audi', 'bmw', 'subaru', 'toyota']
   for car in cars:
       if car =='bmw':
           print(car.upper())
       else:
           print(car.lower())
   ```

   - 不要忘了冒号

9. #### 检查特定的值是否在列表中

   ```python
   requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
   print('mushrooms' in requested_toppings)
   ```

   - 用关键词  in
   - 反之如果想要确定一个元素是否不在列表中用关键词  not in

10. #### 字典

    字典是一系列键值对。每个键都与一个值关联，可以使用键来访问预支有关的值。与键有关的值可以是数、字符串、列表乃至字典。事实上，可将python中的任意对象用作字典中的值。

    ```python
    alien_0 = {'color': 'green', 'point': 5}
    print(alien_0['color'])
    print(alien_0['point'])
    ```

    ##### 添加键值对

    ```python
    alien_0 = {'color': 'green', 'point': 5}
    print(alien_0)
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)
    ```

    ##### 修改键值对中的值

    ```python
    alien_0 = {'color': 'green', 'point': 5}
    alien_0['color'] = 'yellow'
    print(alien_0['color'])
    ```

    ##### 删除键值对

    ```python
    alien_0 = {'color': 'green', 'point': 5}
    del alien_0['point']
    ```

    - del 语句，彻底删除。
    - 使用del语句时必须指定字典名和需要删除的键

    ##### 遍历键值对

    ```python
    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
    }
    
    for key, value in user_0.items():
        print(f"\nKey: {key}")
        print(f"Value: {value}")
    for key in user_0.keys():
        print(f"\nKey: {key}")
    
    ```

    - item()方法是返回一个键值对列表
    - keys()方法是返回键值对中的键（key）

    ##### 顺序遍历

    ```python
    favorite_languages = {
        'jen': 'python',
        'zhao': 'c',
        'yu': 'ruby',
        'shi': 'java',
    }
    for name in sorted(favorite_languages.keys()):
        #反过来，如果想只遍历值的话就把keys改成values就可以
        print(f"{name.title()}, thanks for taking the poll")
    ```

    - value可以用[]来存储多个元素，然后在遍历到value对应的key时使用for循环进行遍历多元素的value值

    ##### 遍历去重

    ```python
    favorite_languages = {
        'jen': 'python',
        'zhao': 'c',
        'yu': 'java',
        'shi': 'java',
    }
    for language in set(favorite_languages.values()):
        print(language.title())
    ```

    - 这里用set()函数来进行提取元素

    ##### 字典列表

    ```python
    aliens = []
    for alien in range(30):
        new_alien = {
            'color': 'green',
            'point': 5,
            'speed': 'slow',
        }
        aliens.append(new_alien)
    for alien in aliens[:20]:
        print(alien)
    ```

    - range（30）函数返回一个数字序列，告诉py需要循环多少次

11. #### 输入 input

    ```python
    message = input("请输入一段话：")
    print(message)
    
    age = input("请输入年龄：")
    age = int(age)
    print(age)
    print(age>18)
    ```

    - input（）函数可以在括号中输入提示语句，让用户知道自己需要输入什么
    - 函数在接受一个参数后可以直接向message进行赋值
    - 返回的结果一般为字符串
    - 如果需要int类型的数字，需要int（）函数进行转换

12. ##### while

    ```python
    num = 1
    while num <= 100:
        print(num)
        num += 1
    ```

    - python的底层逻辑决定了其自身不具有自增 ‘i++’ 这中操作

    - break是结束while这个大循环

    - continue是结束while中的小循环，然后返回查看是否符合条件

    - ```py
      num = 0
      while num < 10:
          num += 1
          if num % 2 == 0:
              continue
      
          print(num)
      ```

13. #### 函数定义

    ```python
    def greet_user(user_name):
        """显示简单的问候语"""
        print(f"Hello!{user_name}")
    
    greet_user('zhaoysuhi')
    ```

14. #### 禁止函数修改列表

    函数中可以对主程序中传过来的列表进行永久性修改，但可以用传递副本的方法对主程序中的列表进行修改保护

    ```python
    function_name(list_name[:])
    ```

    - 要将列表的副本传递给函数，可像上述代码一样
    - 虽然可以使用副本，但除非必做，否则还是应该将原始列表传递给函数。因为让函数使用现成的列表可以节省时间和内存创建副本，从而提高效率

15. #### 传递任意数量的实参

    ```python
    def make_pizza(size, *toppings):
        """打印顾客点的所有配料"""
        print(f"Make a {size}-inch pizza with the following toppings")
    
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms','green peppers','extra cheese')
    ```

    - 形参名*toppings中的星号是让py创建一个名位toppings的元组，该元祖包含函数收到的所有值
    - 如果要让函数接受不同类型的实参，必须在函数定义中将接受任意数量的实参的形参（*toppings）放在最后面

    ##### 接受任意数量的关键字实参

    ```python
    def build_profile(first, last, **user_info):
        """创建一个字典，其中包含我们知道的有关用户的一切"""
        user_info['first_name'] = first
        user_info['last_name'] = last
        return user_info
    
    user_profile = build_profile('albert', 'einstein',
                                 location='princeton',
                                 field='physics')
    ```

    - 形参**user_info中的两个星号是让python创建一个名为user_info的字典，该字典包含了函数收到的所有的键值对

16. #### 用as给导入的函数指定别名

    ```python
    from pizza import make_pizza as mp
    mp(16, 'pepperoni')
    mp(20, 'mushrooms', 'green peppers', 'extra cheese')
    ```

    - 不仅可以给导入的函数进行别名，如果导入的是模块也可以用as取别名

17. #### `__init__(self, ...)`方法

    ```python
    class Dog:
        """一次模拟小狗的简单尝试"""
        def __int__(self, name, age):
            """初始化属性name和age"""
            self.name = name
            self.age = age
    
        def sit(self):
            """模拟小猴收到命令时坐下"""
            print(f"{self.name} is now sitting")
    
        def roll_over(self):
            """模拟小狗收到命令时打滚"""
            print(f"{self.name} rolled over!")
    
            
    
    # 创建一个Person对象，并为该对象添加一个名字属性
    person = Person("John Doe")
    print(person.name) # 输出: John Doe
    ```

    ​	此方法是python中的一类特殊方法，也成构造函数，Java中同样有此类函数。当创建一个类的实例时，此方法会自动调用。

    ​	==它的主要作用还初始化实例中的属性==，如上述代码中的name和age两个属性，在主程序对Dog这个类进行实例时就可以直接将参数传过来进行初始化

    ​	初始化语句可以在创建对象时为对象的属性设置初始值，从而使得代码更加简洁，方便维护。

    ​	其中self参数是必须的，它代表了创建的对象本身，在方法内部可以通过self来引用对象的属性和方法。

    ##### `__init__`方法的多态特性

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            
    class Student(Person):
        def __init__(self, name, age, major):
            Person.__init__(self, name, age)
            self.major = major
    ```

    ​	此方法也支持多态的特性，即子类可以通过重写此方法来覆盖父类的方法，以实现不同的初始化行为。

    ##### super

    super是python中的内置函数，可以在继承关系中访问父类的属性。

    ```python
    class ParentClass:
        def __init__(self, value1, value2):
            self.value1 = value1
            self.value2 = value2
     
    class ChildClass(ParentClass):
        def __init__(self, value1, value2, value3):
            super().__init__(value1, value2)
            self.value3 = value3
    ```

    - 这个super跟上述的多态举例不太一样，这个在调用父类的init方法时不需要再写self

    #### init注意⚠️

    - 方法在对象创建时自动调用，无需手动调用
    - 方法可以接收任意数量的参数，但需要遵循特定的参数签名
    - 在方法中必须给对象的每个属性进行赋值，否则该对象将不完整，不能正常工作
    - 尽量避免在初始化过程中产生太多计算，会影响程序性能

18. #### 导入

    - 在进行跨文件导入时，如果导入的是一个类，即使文件中只有一个类也可以用 `from 文件名 import 类`  这样的方式进行导入
    - 也可以将整个文件进行导入，但需要在后续使用过程中进行  `文件名.类`  的方式进行使用

    - 如果导入的文件中只有方法也可以直接用 `import 文件名` 这样的方式进行简单导入