


#### Decorator

"""
def call_me():
    msg = 'Hello everyone!!'

    def inner_call_me():
        print(msg)
    return inner_call_me()






call_me()
"""
"""
def call_me(sms):
    msg = sms

    def inner_call_me():
        print(msg)
    return inner_call_me






say_hello = call_me('Hello Guys!!!')
say_bye = call_me('Bye Guys!!!')
say_hello()
say_bye()
"""


def dec_function(my_func):
    def wrapper_func(*args, **kwargs):
        print(f'Before running {my_func.__name__} function ....')
        return my_func(*args, **kwargs)
    ##print(f'I am ouside of inner function...')
    return wrapper_func

"""
def display():
    print('the function is executed ...')



dec_display = dec_function(display)

dec_display()

"""

@dec_function
def display():
    print('the function is executed ...')



@dec_function
def display_student_info(name, age):
    print(f'my name is {name} and {age} years old.')









display()
print("+++++++++++++")
display_student_info('Anna', 23)





















