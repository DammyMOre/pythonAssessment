

def wrapper(*args, **kwargs):
    def wrap(*args, **kwargs):
        print("************")
        print(*args, **kwargs)
        print("#$%^&")
    return wrap(*args, **kwargs)

@wrapper
def print_name(name):
    return name


print_name("John")


# def print_out(n, name):
#     for i in range(n):
#         print(name)
#
# print_out(5, name='John')


