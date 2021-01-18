name = input("Enter your name : ")
pwd = input("Enter your password : ")

if name == 'ravi':
    print("Valid Id")
    if pwd == '12345':
        print("Login success")
    else:
        print("Invalid Password, Login Failed")
else:
    print("Invalid Id")
