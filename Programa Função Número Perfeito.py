#Programa para descobrir se um número inteiro e positivo é um número perfeito

def perfeito(n):
    res = 0
    for i in range (1, n):
        if n%i==0:
            res+=i
    return (res)
num = int(input(f'Informe um número inteiro e positivo: '))
while num <1:
    num = int(input(f'Informe um número inteiro e positivo: '))
if (perfeito(num) == num):
    print (f'O número {num} é um número perfeito!')
else:
    print (f'O número {num} não é um número perfeito.')
