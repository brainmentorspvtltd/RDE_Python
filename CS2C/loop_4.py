'''
*****
*****
*****
*****
*****
'''
row = 5
col = 5
for i in range(row):
    for j in range(col):
        print('*', end='')
    print()

print('-' * 40)

'''
*
**
***
****
*****
'''
row = 5
for i in range(row):
    for j in range(i+1):
        print('*', end='')
    print()

print('-' * 40)

'''
*****
****
***
**
*
'''
row = 5
for i in range(row):
    for j in range(row-i,0,-1):
        print('*', end='')
    print()

print('-' * 40)

'''
1
12
123
1234
12345
'''
row = 5
for i in range(row):
    for j in range(i+1):
        print(j+1, end='')
    print()

'''
a
ab
abc
abcd
abcde
'''
row = 5
for i in range(row):
    for j in range(i+1):
        print(chr(97+j), end='')
    print()

'''
     *
    ***
   *****
  *******
 *********
***********
'''
for i in range(6):
    print(' ' * (6 - i) + '*' * (2*i + 1))

for i in range(6):
    for j in range(6 - i):
        print(' ' end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()














