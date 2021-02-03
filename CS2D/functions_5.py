def person(id, name, age, *address):
    print("ID is",id)
    print("Name is",name)
    print("Age is",age)
    print("Address is",address)

person(101,'Ram',40,'Delhi')
person(102,'Shyam',41,'Delhi','Pune')
person(102,'Shyam',41,'Delhi','Pune','Mumbai')
