x = 9
y = 12
z = 10

'''
if x > y and x > z:
    print("X is greater")
elif y > x and y > z:
    print("Y is greater")
else:
    print("Z is greater")
'''
result = "X" if x > y and x > z else "Y" if y > x and y > z else "Z"
print(result,"is greatest")








