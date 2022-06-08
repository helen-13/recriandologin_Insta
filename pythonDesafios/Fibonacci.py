n = int(input('Entre com a quantidade de termos de Fibonacci:'))
a= 0
b= 1
c=a+b
print
cont = 3
while cont <=n:
    c=a+b
    print('{}'. format(c))
    a=b
    b=c
    cont += 1
print('')