#Первывй вариант

def myDecorator(func):
    def wrapped(a, b=1, *args, **kwargs):
        print(f'Calling testFunc({a, b, args}, {kwargs})')
        func(a, b, *args, **kwargs)
        print(f'Finished testFunc({a+b})')
    return wrapped

#Второй вариант(better)
def myDecorator(func):
    func_name = func.__name__
    
    def wrapped(*args, **kwargs):
        print(f'Calling {func_name}({args}, {kwargs})')
        func_result = func(*args, **kwargs)
        print(f'Finished {func_name}({func_result})')
    return wrapped

#Testing
@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print("argument a: ", a)
    print("argument b: ", b)
    print("argument args: ", args)
    print("argument kwargs: ", kwargs)

    return a + b

testFunc(2, 3, 4, 5, c=6, d=7)
testFunc(2, c=5, d=6)
testFunc(10)
