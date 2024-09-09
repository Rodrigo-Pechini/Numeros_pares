from time import sleep
from Utilidades import tratamento

print('ENCONTRANDO NUMEROS \033[32mPARES\033[m')
inicio = tratamento.valorInteiro('Digite o valor inicial da contagem: ')
fim = tratamento.valorInteiro('Digite o valor final da contagem: ')

paso = tratamento.contagemInvertida(inicio, fim)
if paso == -1:
    fim -= 2

for n in range(inicio, fim + 1, paso):
    if n % 2 == 0:
        print(f'\033[32m{n}\033[m', end=' ')
    else:
        print(n, end=' ')
    sleep(0.5)
print()
print('Programa finalizado')
