# def person(name, mno, *address):
#     print("Name is",name)
#     print("Mobile no is",mno)
#     print("Address is",address)
#
# person('Ravi', 9878989754, 'Delhi')
# person('Amit', 9898765441, 'Delhi', 'Gzb')

# **kwargs - keyword arguments
def person(**details):
    print(details)

person(name='Ram', mno=989886677, address='Delhi')
person(name='Shyam')
person(name='Ram', mno=989886612, address='Delhi', company='TCS')
