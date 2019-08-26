def make_uppercase(func):

    def wrapper_func(args):
        upper_case = args.upper()
        return func(upper_case)

    return wrapper_func

def split_name(func):

    def wrapper_func(args):
        split_letter = args.split(" ")
        return func(split_letter)

    return wrapper_func

@make_uppercase
@split_name
def say_hi(name):
    print("Final Output")
    return name

result = say_hi("Jijin Sebastian")
print(result)