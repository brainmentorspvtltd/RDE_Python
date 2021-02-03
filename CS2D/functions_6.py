# def person(**details):
#     print(details)
#
# person(name = 'Ram')
# person(name = 'Shyam', age = 40)
# person(name = 'Mukesh', age = 46, address = 'Delhi')
# person(address = 'Pune')

def person(*args, **kwargs):
    print(args)
    print(kwargs)

