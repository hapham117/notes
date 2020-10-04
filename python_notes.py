# Python notes

# Summary:
    # String related:
        # String formatting expressions
        # Using for loops to loop through a string
        # See if substring exists in string. Returns boolean. Find substring in string
        # string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
        # Slicing. Get a slice (substring) of a string

    # Sequence related:
        # list.insert(value): Insert item in list. Different from append. Insert takes two arguments
        # list.remove(value): Remove item from list by matching string or value. It removes the first item it encounters in the list
        # list.pop(index?): Remove item from list by index. If index is not given, pop() removes the last item
        # list.sort(key=function(), reverse=Boolean): Sorts a list from small to big
        # Replacing an item in list by index
        # Tuple
        # enumerate(sequence)
        # Loop through a list of tuples. Each tuple contains 2 strings. Get these 2 strings
        # List comprehension, python's way to create a list based on sequences or ranges
        # del. Deleting a key:value pair from a dictionary
        # Loop through a dict and get key:value pair from it
        # Set. A set is used when you want to store a bunch of elements and be certain that they're only present once
        # var = var.join(sequence): A string method that returns a string in which the elements of sequence have been joined by str separator.
        # .get('key', default_value): Get the value of a dict item. If key is empty, returns default_value.

    # Others:
        # dir. Prints all attributes and methods of an object
        # help. Prints documention about a given class/instance
        # *args and **kwargs allow you to pass an unspecified number of arguments to a function:
            # *args is used to send a non-keyworded variable length argument list to the function.
            # **kwargs allows you to pass keyworded variable length of arguments to a function.
            # You should use **kwargs if you want to handle named arguments in a function. 

    # Class and object related:
        # Creating a new instance/object of a class
        # def __init__(self): Creating a constructor:
        # def __str__(self): Returns a given string when executing print(class_instance):
        # help(class_instance). To see all the attributes and methods of a given object, use: help(class_instance):
        # Docstring. You can also add a docstring to your functions, methods and classess. This will replace the default message.
        # Class inheritence: class Apple(Fruit):12
# End of summary


def string_formatting_expressions():
    # String formatting expressions:
    number = 5.1234
    number2 = 1.9876
    test = 'Test text {number:>4.2f}, {number2:.2f}'.format(number=number, number2=number2)
    print("\n'Test text {number:>4.2f}, {number2:.2f}'.format(number=number, number2=number2):", test)
        # Test text 5.12, 1.99
    # Cheat sheet: https://i.gyazo.com/90231aae38f685b3b1a9eb8a1963d793.png
    # Documentation: https://docs.python.org/3/library/string.html#format-specification-mini-language
# string_formatting_expressions()

def loop_through_string():
    # Using for loops to loop through a string:
    string = 'Hello world!'
    print()
    for character in string:
        print('for character in string:', character)
# loop_through_string()

def check_substring_exists():
    # See if substring exists in string. Returns boolean. Find substring in string:
    string = 'Hello world!'
    print('\n"ello" in string:', 'ello' in string)
        # "ello" in string: True
# check_substring_exists()

def lstrip_rstrip_strip():
    # string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
    string = "   Yooooo    "
    new_string = string.lstrip()
    print('\nlstrip()', new_string)
        # lstrip() Yooooo  
    new_string = string.rstrip()
    print('\nrstrip()', new_string)
        # rstrip()    Yooooo
    new_string = string.strip()
    print('\nstrip()', new_string)
        #strip() Yooooo
# lstrip_rstrip_strip()

def slice_string():
    # Slicing. Get a slice (substring) of a string.
    string = "This is a string."
    get_string = string[10:]
    print('\nSlicing:', get_string)
        # Slicing: string.    
    get_string = string[:10]
    print('\nSlicing:', get_string)
        # Slicing: This is a
# slice_string()

def insert_item_to_list():
    # list.insert(value): Insert item in list. Different from append. Insert takes two arguments.
    my_list = ['apple', 'orange', 'banana']
    my_list.insert(1, 'kiwi')
    print('\ninsert():', my_list)
        # ['apple', 'kiwi', 'orange', 'banana']
# insert_item_to_list()

def remove_item_from_list():
    # list.remove(value): Remove item from list by matching string or value. It removes the first item it encounters in the list.
    my_list = ['apple', 'orange', 'kiwi', 'banana', 'kiwi']
    my_list.remove('kiwi')
    print('\nremove():', my_list)
        # ['apple', 'orange', 'banana', 'kiwi']
# remove_item_from_list()

def pop_item_from_list():
    # list.pop(index?): Remove item from list by index. If index is not given, pop() removes the last item.
    my_list = ['apple', 'orange', 'kiwi', 'banana', 'kiwi']
    my_list.pop(2)
    print('\npop():', my_list)
        # ['apple', 'orange', 'banana', 'kiwi']
# pop_item_from_list()

def sort_list():
    # list.sort(key=function(), reverse=Boolean): Sorts a sequence from small to big.
    # The way it needs to be sorted can be passed through the key parameter with a function.
    # Sort only works for lists where its contents are compatible to each other. So you can't sort a list with strings and integers in it.
    my_list = ['d', 'a', 'c', 'b']
    my_list.sort()
    print(my_list)
    my_list.sort(key=len) # len is a python built-in function. This will sort by length.
    print(my_list)
    
    # Sorting a list of tuples with the key argument:
    def takeSecond(elem): return elem[1]
    def takeFirst(elem): return elem[0]
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]
    random.sort(key=takeSecond)
    print(random)
    random.sort(key=takeFirst)
    print(random)
# sort_list()

def sorted_list():
    # list.sorted(sequence, key=function, reverse=Boolean): Creates a new sequence that's sorted. Similar to sort()
    my_list = ['d', 'a', 'c', 'b']
    new_list = sorted(my_list)
    print(new_list)
    
    # Sorting a list of tuples with the key argument:
    def takeSecond(elem): return elem[1]
    def takeFirst(elem): return elem[0]
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]
    new_random = sorted(random, key=takeSecond)
    print(new_random)
    new_random = sorted(random, key=takeFirst)
    print(new_random)
# sorted_list()

def replacing_item_in_list_by_index():
    # Replacing an item in list by index.
    my_list = ['apple', 'orange', 'banana']
    my_list[2] = 'Kiwi'
    print('\nReplacing item in list:', my_list)
# replacing_item_in_list_by_index()

def tuple_sequence():
    # Tuple
    # A tuple is a like a list, but immutable. The order of the elements inside a tuple and its values can't change.
    # A tuple starts and ends with round brackets: "('This', 'is', 'a', 'tuple')"
    # Here we assign the values of the tuple's elements to variables:
    my_tuple = ('This', 'is', 'a', 'tuple')
    word1, word2, word3, word4 = my_tuple
    print('\nTuple:', word1, word2, word3, word4)
        # Tuple: This is a tuple
# tuple_sequence()

def enumarate_function():
    # enumerate(sequence): Enumerate is a function used to convert a list or tuple into an enumerate object.
    # You use this function when you need to go through a sequence to get its values INCLUDING its index.
    # Using a for loop and extract the index and value from the tuple with enumerate():
    my_tuple = ('apples', 'bananas', 'oranges')
    for index, value in enumerate(my_tuple):
        print("index is {index} and value is {value}".format(index=index, value=value))
            # index is 0 and value is apples
            # index is 1 and value is bananas
            # index is 2 and value is oranges
    
    # Here we enumerate a tuple:
    x = ('apple', 'banana', 'cherry')
    y = list(enumerate(x))
    print('\nEnumerate:', y)
        # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# enumarate_function()

def loop_through_list_of_tuples():
    # Loop through a list of tuples. Each tuple contains 2 strings. Get these 2 strings:
    print('\nLoop through a list of tuples and get the values from each tuple:')
    list_of_tuples = [
        ('apples', 'yummy'),
        ('bananas', 'yummy'),
        ('oranges', 'blegh'),
        ('kiwis', 'yummy')
    ]
    for fruit, opinion in list_of_tuples:
        fruit = fruit[0].upper() + fruit[1:]
        print("{} are {}".format(fruit, opinion))
            # Apples are yummy
            # Bananas are yummy
            # Oranges are blegh
            # Kiwis are yummy
# loop_through_list_of_tuples()

def list_comprehension():
    # List comprehension, python's way to create a list based on sequences or ranges. Here are 3 examples:
    print('\nList comprehension')
    #Example 1:
    multiples = [ x*7 for x in range(1, 11) ]
    print('multiple:', multiples)
        # multiple: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

    # Example 2:
    languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C']
    lengths = [len(language) for language in languages]
    print('Lengths:', lengths)
        # Lengths: [6, 4, 4, 2, 4, 1]

    # Example 3, including if statements:
    z = [x for x in range(1, 101) if x % 3 == 0]
    print('z:', z)
        # z: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
# list_comprehension()

def deleting_key_value_pair_from_dict():
    # del. Deleting a key:value pair from a dictionary:
    print('\ndeleling key:value pair from dict:')
    my_dict = {'bananas': 10, 'kiwis': 5, 'oranges': 6, 'apples': 4}
    del my_dict['kiwis']
    print('my_dict:', my_dict)
        # my_dict: {'bananas': 10, 'oranges': 6, 'apples': 4}
# deleting_key_value_pair_from_dict()

def loop_through_dict_and_get_key_value():
    # Loop through a dict and get key:value pair from it:
    print('\nitems() get key:value pair from a dict:')
    my_dict = {'bananas': 10, 'kiwis': 5, 'oranges': 6, 'apples': 4}
    for key, value in my_dict.items():
        print(f'key: {key}, value: {value}')
            # key: bananas, value: 10
            # key: kiwis, value: 5
            # key: oranges, value: 6
            # key: apples, value: 4
    # Same thing but only get the keys from the dict:
    for key in my_dict.keys():
        print(f'key: {key}')
    # And only get values:
    for value in my_dict.values():
        print(f'value: {value}')
# loop_through_dict_and_get_key_value()

def a_set():
    # Set. A set is used when you want to store a bunch of elements and be certain that they're only present once.
    # It looks like a dict but without values, only keys. Example:
    my_set = {"apple", "banana", "cherry"}
    print(type(my_set))
        # <class 'set'>
# a_set()

def join_function():
    # var = var.join(sequence): A string method that returns a string in which the elements of sequence have been joined by str separator.
    print("\nvar = var.join(sequence):")
    # Example 1
    list1 = ['1','2','3','4'] 
    s = "-"
    s = s.join(list1)
    print(f"{s}\n{type(s)}")
        # 1-2-3-4
        # <class 'str'>
    
    # Example 2
    s = ""
    s = s.join(list1) 
    print(s)
        # 1234
    
    # Example 3
    data = ['Apple', 'Banana', 'Cherry', 'Orange']
    my_list = ", ".join(data)
    print(f"{my_list}\n{str(type(my_list))}")
        # Apple, Banana, Cherry, Orange
        # <class 'str'>
# join_function()

def get_value_from_dict():
    # .get('key', default_value): Get the value of a dict item. If key is empty, returns default_value.
    my_dict = {
        'apple': 1,
        'banana': 2
    }
    banana_amount = my_dict.get('banana', 0)
    print(banana_amount)
# get_value_from_dict()

def dir_function():
    # dir. Prints all attributes and methods of an object.
    print('\ndir:')
    print('dir(5):', dir(5))
        # dir(5): ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# dir_function()

def help_function():
    # help. Prints documention about a given class/instance
    print('\nhelp:')
    print('help(5):', help(5))
# help_function()

def args_and_kwargs():
    # *args and **kwargs allow you to pass an unspecified number of arguments to a function:
        # *args is used to send a non-keyworded variable length argument list to the function.
        # **kwargs allows you to pass keyworded variable length of arguments to a function.
        # You should use **kwargs if you want to handle named arguments in a function
    print('\nargs and kwargs:')
    
    def test_var_args(first_arg, *args):
        print('f_arg:', first_arg)
            # first_arg: apple
        print(f'*args, {args}, {type(args)}')
            # *args, ('banana', 'cherry'), <class 'tuple'>
        for arg in args:
            print("another arg through *args:", arg)
                # another arg through *args: python
                # another arg through *args: eggs
                # another arg through *args: test
    test_var_args('apple', 'banana', 'cherry')
    
    def print_name(**kwargs):
        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))
                # name = Ha Pham
    print_name(name="Ha Pham")
# args_and_kwargs()

def creating_object_from_class():
    # Creating a new instance/object of a class:
    print('\nCreating a new instance/object of a class:')
    class Apple:
        color = ""
        flavor = ""
    
    my_apple = Apple()
    my_apple.color = "red"
    print('my_apple.color:', my_apple.color)
        # my_apple.color: red
# creating_object_from_class()

def init_constructor():
    # def __init__(self): Creating a constructor:
    print('\nCreating a constructor with def __init__(self):')
    class Apple:
        def __init__(self, color, flavor):
            self.color = color
            self.flavor = flavor
    jonagold = Apple('red', 'sweet')
    print(f'{jonagold.color}, {jonagold.flavor}')
        # red, sweet
# init_constructor()

def str_special_method():
    # def __str__(self): Returns a given string when executing print(class_instance):
    print('\ndef __str__(self): Returns a given string when print(class_instance):')
    class Banana:
        def __init__(self, color, flavor):
            self.color = color
            self. flavor = flavor
        def __str__(self):
            return 'This fruit is {flavor} and its color is {color}'.format(flavor=self.flavor, color=self.color)
    my_banana = Banana('yellow', 'sweet')
    print(my_banana)
        # This fruit is sweet and its color is yellow
    
    # help(class_instance). To see all the attributes and methods of a given object, use: help(class_instance):
    help(my_banana)
# str_special_method()

def docstring():
    # # Docstring. You can also add a docstring to your functions, methods and classess. This will replace the default message.
    # Use """ Docstring example """ at the first line of a function/method/class to write a docstring:
    print('\nDocstring example:')
    class Cherry:
        """This is a docstring"""
        def __init__(self, color, flavor):
            """This too is a docstring"""
            self.color = color
            self. flavor = flavor
        def __str__(self):
            return 'This fruit is {flavor} and its color is {color}'.format(flavor=self.flavor, color=self.color)
    my_cherry = Cherry('red', 'sweet and sour')
    # help(my_cherry)
    # help(Cherry)
    def my_function():
        """This is a docstring for this function"""
        return
    # help(my_function)
# docstring()

def class_inheritence():
    # Class inheritence: class Apple(Fruit):
    print('\nClass inheritence:')
    class Fruit:
        """This is a fruit"""
        name = ""
        def __init__(self, color, flavor):
            self.color = color
            self.flavor = flavor
        
        def __str__(self):
            return "This is {}. The color is {} and it tastes {}".format(self.name, self.color, self.flavor)
        
    class Apple(Fruit):
        name = "an apple"

    class Grape(Fruit):
        name = "a grape"

    my_apple = Apple('red', 'sour')
    print(my_apple)
        # This is an apple. The color is red and it tastes sour
# class_inheritence()

def composition():
    print('\nComposition:')
    # Composition. You can have a situation where two different classes are related, but there is no inheritance going on.
    # This is referred to as composition -- where one class makes use of code contained in another class.
    def clothing_composition():
        class Clothing:
            stock={ 'name': [],'material' :[], 'amount':[]}
            def __init__(self,name):
                material = ""
                self.name = name
                
            def add_item(self, name, material, amount):
                Clothing.stock['name'].append(self.name)
                Clothing.stock['material'].append(self.material)
                Clothing.stock['amount'].append(amount)
                
            def Stock_by_Material(self, material):
                count=0
                n=0
                for item in Clothing.stock['material']:
                    if item == material:
                        count += Clothing.stock['amount'][n]
                        n+=1
                return count

        class Shirt(Clothing): material = "Cotton"
        class Pants(Clothing): material = "Cotton"

        polo = Shirt("Polo")
        sweatpants = Pants("Sweatpants")
        polo.add_item(polo.name, polo.material, 4)
        sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
        current_stock = polo.Stock_by_Material("Cotton")
        print('Current stock:', current_stock)
            # Current stock: 10
    clothing_composition()
    
    # Another example:
    def repository_composition():
        class Repository:
            def __init__(self): self.packages = {}
            def add_package(self, package): self.packages[package.name] = package
        
            def total_size(self):
                result = 0
                for package in self.packages.values(): result += package.size
                return result
            
        class Package:
            def __init__(self, name, size):
                self.name = name
                self.size = size
            def __str__(self):
                return "name: {}, size: {}".format(self.name, self.size)
                
        my_repo = Repository()
        my_package = Package('C++', 1024)
        my_repo.add_package(my_package)
        print(my_repo)
            # <__main__.composition.<locals>.repository_composition.<locals>.Repository object at 0x000001EABDAEB460>
        
    repository_composition()
# composition()