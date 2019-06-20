# function is a block of code that can be used elsewhere
# only an argument default value is allowed in the last argument


def greet_customer(name, num_apples=7):
    print(f'hello, {name}')
    print(f'we have {num_apples} in stock')


greet_customer('Mark')
greet_customer('Brooke', 6)
greet_customer('Greg', 2)
