

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f'{orig_func.__name__} is running with args: {args} and kawrgs: {kwargs}')
        return orig_func(*args, **kwargs)
    return wrapper


@my_logger   
def display_student_info(name, age):
    print(f'my name is {name} and {age} years old.')



display_student_info('Anna', 24)
