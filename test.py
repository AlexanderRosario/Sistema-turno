# x = 50

# def one():
#   x = 10

# def two():
#   global x
#   x = 30

# def three():
#   x = 100
#   print(x)

# for func in [one, two, three]:
#   func()
#   print(x)


# def print_before_and_after(func):
#     def name(*args):
#         print('Before {}'.format(func.__name__))
#     # Call the function being decorated with *args
#         func(*args)
#         print('After {}'.format(func.__name__))
#   # Return the nested function
#     return name

# @print_before_and_after
# def multiply(a, b):
#   print(a * b)

# multiply(5, 10)

# def print_return_type(func):
#   # Define wrapper(), the decorated function
#   def wrapper(*args, **kwargs):
#     # Call the function being decorated
#     result = func(*args, **kwargs)
#     print('{}() returned type {}'.format(
#       func.__name__, type(result)
#     ))
#     return result
#   # Return the decorated function
#   return ____
  
# @print_return_type
# def foo(value):
#   return value
  
# print(foo(42))
# print(foo([1, 2, 3]))
# print(foo({'a': 42}))

# def print_before_and_after(func):
#     def wrapper(*args):
#         print('Before {}'.format(func.__name__))
#     # Call the function being decorated with *args
#         func(*args)
#         print('After {}'.format(func.__name__))
#   # Return the nested function
#     return wrapper


# def multiply(a, b):
#   print(a * b)

# new_print = print_before_and_after(multiply)
# new_print (5,2)

# book = {
#     'title': 'The Giver',
#     'author': 'Lois Lowry',
#     'rating': 4.13
# }

# book['rating'] = 4.6

# print(book['rating'])
# x = (1, 2, 3)
# s = set(x)

# print(s)

# print([i for i in range(5) if i>2])