# def person(name, mobile, *address):
#     print("Name is",name)
#     print("Mobile is :",mobile)
#     print("Address is",address)
#
# person('Ram', 676767676, 'Delhi')
# person('Shyam', 9898989888, 'Pune_1', 'Pune_2')

def person(**details):
    print(details)

person(name = 'Ram', age = 20, mobile = 8787888878)
person(name = 'Ravi')
person(name = 'Shyam', mobile = 9898899899)





