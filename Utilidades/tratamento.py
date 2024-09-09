def contagemInvertida(inicio, fim):
    if inicio > fim:
        return -1
    else:
        return 1
    
def valorInteiro(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[31mERRO!! Valor invalido digite novamente.\033[m')

