'''
for i in range(5):
    for j in range(5):
        print(i,j, end=',')
    print('-' * 10)
'''
'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()
'''
a
ab
abc
abcd
abcde
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(96 + j), end='')
    print()

'''
1
23
456
78910
'''
k = 0
for i in range(1,5):
    for j in range(1,i+1):
        k += 1
        print(k, end='')
    print()

print('-' * 20)

'''
12345
1234
123
12
1
'''
for i in range(1,6):
    for j in range(1,7-i):
        print(j, end='')
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
    for j in range(5 - i - 1):
        print(' ', end=' ')
    for k in range(2*i + 1):
        print('*', end='')
    print()













