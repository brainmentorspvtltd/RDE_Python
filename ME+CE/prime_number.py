num = 17
prime = True
for i in range(2,num):
    if num % i == 0:
        #print("Not prime")
        prime = False
        break
    else:
        prime = True
        #print("Prime")

if prime:
    print("Number is prime")
else:
    print("Number is not prime")
