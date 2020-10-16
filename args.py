

### *args **kwargs

###           positional args ////   keywords args
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)



### student_info('Math', 'Comp Sci', name='Jack', age=23)
courses = ['Math', 'Comp Sci']
info = {'name': 'Jack', 'age': 23}

student_info(*courses, **info)
