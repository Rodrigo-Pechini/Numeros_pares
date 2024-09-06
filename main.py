print('ENCONTRANDO NUMEROS PARES')

inicio = int(input('Digite o inicio da contagem: '))
fim = int(input('Digite o fim da contagem: '))

for n in range(inicio, fim + 1):
    if n % 2 == 0:
        print(f'\033[32m{n}\033[m', end=' ')
    else:
        print(n, end=' ')
print('Programa finalizado')
