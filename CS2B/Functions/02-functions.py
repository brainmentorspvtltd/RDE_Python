def student(name,year,college='RDEC'):
    print("Hello",name)
    print("Your year is",year)
    print("College is",college)

# Positional args
# student("Ram",2,"RDEC")
# student("Shyam",3,"IMS")
# student("Anuj",2,"RDEC")

# Keyword args
# student(name='Ram', year=2, college='RDEC')
# student(name='Ram', college='RDEC', year=2)

student('Ram',3,'IMS')
student('Ram',3)



