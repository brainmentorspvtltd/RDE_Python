'''
for i in range(5):
    for j in range(5):
        print(i,j)
    print("-" * 20)
'''
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
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()

print('-' * 20)

'''
*****
****
***
**
*
'''
for i in range(6,1,-1):
    for j in range(i-1):
        print('*', end='')
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

print('-' * 20)
'''
1
2 3
4 5 6
7 8 9 10
'''
k = 1
for i in range(1,5):
    for j in range(i):
        print(k, end='')
        k = k + 1
    print()

print('-' * 20)

















