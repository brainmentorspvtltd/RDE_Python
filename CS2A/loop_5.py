'''
for i in range(5):
    for j in range(6):
        print(i,j)
    print('---------')
'''

'''
*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()


print('-' * 20)

'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()
print('-' * 20)
'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    for j in range(0,i):
        print('*', end='')
    print()

print('-' * 20)

'''
1
23
456
78910
'''
n = 1
for i in range(4):
    for j in range(i+1):
        print(n, end='')
        n = n + 1
    print()

print('-' * 20)

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5):
    for j in range(4 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()


'''
a
ab
abc
abcd
abcde
'''
for i in range(0,6):
    for j in range(0,i):
        print(chr(j + 97), end='')
    print()












