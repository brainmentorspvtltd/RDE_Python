num = 17
prime = True

for i in range(2,num):
    if num % i == 0:
        #print("Not Prime")
        prime = False
        break
    else:
        #print("Prime")
        prime = True

if prime:
    print("Number is prime")
else:
    print("Number is not prime")


