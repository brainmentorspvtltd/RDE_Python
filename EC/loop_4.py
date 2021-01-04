#Nested for loops
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
1
12
123
1234
12345
'''
for i in range(5):
    for j in range(i+1):
        print(j+1, end='')
    print()

print('-' * 20)

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5 - i):
        print('*', end='')
    print()

'''
a
ab
abc
abcd
abcde
'''
#hint - chr(97)
for i in range(5):
    for j in range(i+1):
        print(chr(97+j), end='')
    print()

print('-' * 20)

'''
1
23
456
78910
'''
k = 0
for i in range(4):
    for j in range(i+1):
        k = k + 1
        print(k, end='')
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
    for j in range(5 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()









