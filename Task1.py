n = int(input('Введите число слагаемых: '))
S1 = 3
i = 2
z = 1
while i <= n:
    S1=S1+4*z/(i*(i+1)*(i+2))
    i+=2
    z=-z
print(f'Число пи: {S1}')