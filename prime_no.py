num=int(input('enter the no : '))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print('it is not prime number')
            break
    else:
        print('{} it is a prime number'.format(num))
else:
    print('it is not prime number')