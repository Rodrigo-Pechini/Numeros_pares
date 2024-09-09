from time import sleep
from Utilidades import tratamento

print('ENCONTRANDO NUMEROS \033[32mPARES\033[m')

# Interação com usuario é avaliando resposta
inicio = tratamento.valorInteiro('Digite o valor inicial da contagem: ')
fim = tratamento.valorInteiro('Digite o valor final da contagem: ')

# Avaliando se a contagem vai ser invertida
paso = tratamento.contagemInvertida(inicio, fim)
if paso == -1:
    fim -= 2

# Mostrando o resultado
for n in range(inicio, fim + 1, paso):
    if n % 2 == 0:
        print(f'\033[32m{n}\033[m', end=' ')
    else:
        print(n, end=' ')
    sleep(0.5)
print()
print('Programa finalizado')
