def atm():
    total = 10000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Success")
    else:
        # print("Login Fail")
        raise ValueError("Login Failed, Invalid PIN")

    amount = int(input("Enter amount you want to withdraw : "))
    if amount < total:
        total = total - amount
        print("Remaining balance is", total)
    else:
        raise ValueError("Insufficient Balance")

try:
    atm()
except ValueError as err:
    print(err)







