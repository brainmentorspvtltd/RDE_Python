x,y,z = 10,30,20

'''
if x > y and x > z:
    print("X is greatest")
elif y > x and y > z:
    print("Y is greatest")
elif z > x and z > y:
    print("Z is greatest")
else:
    print("Invalid data")
'''

result = 'X' if x > y and x > z else 'Y' if y > x and y > z else 'Z'
print(result,"is greatest")








