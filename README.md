# Encontrando numeros pares em python
## Sobre o programa:
Este é um programa simples que vai colorir os numeros pares em verde e deixar os impares sem cor.

Temos duas entradas do usuario, uma para indicar onde vai iniciar o progrma e outra onde ele vai finalizar.

A saida é todos os numeros, mas os numeros pares são coloridos com verde.

Para ver o video do código funcionando [clique aqui](https://www.linkedin.com/feed/update/urn:li:ugcPost:7238964659603570688/)

![Captura de tela 2024-09-09 112447](https://github.com/user-attachments/assets/cec32124-6829-4943-b457-eef98bf74aa5)

![Captura de tela 2024-09-09 112338](https://github.com/user-attachments/assets/a94e1985-b1c8-4fe2-82f1-012c10e82477)
***
Um programa simples, mas demonstra algumas funcionalidades interessantes em python:
## Função renge():
````
for n in range(inicio, fim, pular)
````
inicio: Onde a contagem se inicia.

fim: Onde a contagem finaliza.

pular: Onde o programa pode pular de acordo com o valor.

Uma coisa importante o range() sempre desconsidera o **ultimo** numero do fim.
Um exemplo:
````
# Código:
for n in range(0, 10)
 print(n)

#saida:
0 1 2 3 4 5 6 7 8 9
````
Nota que o inicio é 0, fim é 10 e o pulo é nada, quando não se coloca nenhum valor no pulo ele automaticamente é 1,
então o programa esta pulando de 1 em 1 e o 9 foi o ultimo numero da saida, de monstrando que se eu quise-se o numero 10 no fim eu colocaria o
numero 11.
***
Outro exemplo:
````
# Código:
for n in range(0, 10, 2)
  print(n)

# saida:
0 2 4 6 8
````
Percebe que o programa inicia no 0 termina em 10 e vai pulando de 2 em 2.
***
Ultimo exemplo:
````
# Código:
for n in range(10, 0, -1)
 print(n)

# Saida:
10 9 8 7 6 5 4 3 2 1
````
Agora temos algo novo o inicio 10, fim é 0 e o pulo é -1, oque esta contecendo é que o pulo esta voltando de 1 em 1 
fazendo uma contagem invertida.
***
## Cores em python:
É claro que existem varias formas de utilizar cores em python, mas como eu queria um visual simples apliquei um codigo simples.
* **Vermelho**: ``\033[31mSua palavra\033[m``
* **Verde**: ``\033[32mSua palavra\033[m``
* **Amarelo**: ``\033[33mSua palavra\033[m``
* **Azul**: ``\033[34mSua palavra\033[m``
* **Roxo**: ``\033[34mSua palavra\033[m``
Pecebe um padrão, no inicio temos os código ``\033[32m``, no meio um texto e no final outro código ``\033[m``, este no final indica qual o trecho do texto queremos colorir,
sem ele não teremos essa limitação.
***
## Tratamento de erros.
Quando estamos fazendo algum código e testando ele alguns erros podem aparecer e isso é normal, mas podemos utilizar esse erros ao nosso favor.

Um exemplo:
````
try:
 numero = int(input('Digite um numero: '))
except ValueError:
 print('Valor invalido.')
````
Se a gente digitar algum valor que não seja um ``int``(numero inteiro) o programa voltara um erro de valor e o programa vai finalizar, para não ocorrer isso utilizamos o ``try:`` 
para tentar realizar o código ``numero = int(input('Digite um numero: '))``, se o usuario digitar alguama palavra por engano o código vai até o except e o executa pois o erro que 
seria mostrado na tela é o mesmo estabelecido para ele, o código retornara ``Valor invalido.``.

### Sem try:

![Captura de tela 2024-09-09 141600](https://github.com/user-attachments/assets/ee58c535-c923-483d-9e2d-63be5568fbc1)
## Com try:

![Captura de tela 2024-09-09 141809](https://github.com/user-attachments/assets/80843e24-d0b9-4b72-9073-1786ceedfc94)
***
## Pontos a se melhorar:
Como todo e qualquer código tem pontos que podemos melhorar, no meu caso eu vejo os seguintes pontos:
- [x] **Tratamento de erros**: Verificar sé a entrada do usuario é um numero ou não, pois nada impede o usuario de colocar seu nome ou qualquer outra palavra.
- [x] **Validação de entrada**: Adicionadar uma verificação para garantir que o valor inicial seja menor ou igual ao valor final.




