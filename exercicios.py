# Boas praticas em python
# snake_case = para varáveis, funções e metódos
# PascalCase = para classes
# SCREAMING_SNAKE_CASE = para constantes

# 1 Imprima a frase: Python na Escola de Programação da Alura.
#print("Python na Escola de Programação da Alura")

#2 Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
#nome = input("Digite seu nome: ")
#idade = input("Digite a sua idade: ")

#print(f"Meu nome é {nome} e tenho {idade} anos")

#3 imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
#print('A','L','U','R',"A", sep='\n')

#4 - Para imprimir o valor de pi arredondado, temos algumas possíveis abordagens:
#pi = 3.14169
#print(f"O valor arredondado de pi é {pi:.2f}") #Chamando a variavel {variavel:.2f}
#print("O valor arredondado de pi é: " ,round(pi,2)) # Chamando a função round(variavel, numero de casa decimais)


#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou impar.
#numero_escolhido = int(input("Digite um número: "))
#porcentagem retorna da divisão %
#if numero_escolhido % 2 == 0:
 #   print("par")
#else:
 #   print("impar")

#2 -  Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos
# Adolecente: 13 a 18 anos
# Adulto: acima de 18 anos

#idade = int(input("Digite a sua idade: "))

#if 0 <= idade <=12:
#    print("Sua idade se classifica na categoria: Criança")
#elif 13 <= idade <= 18:
 #   print("Sua idade se classifica na categoria: Adolecente")
#else:
 #   print("Sua idade classifica na categoria: Adulta")

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos corresponder aos valores esperados determinados por você.

#usuario_correto = "arthur"
#senha_correta = "arthur123"

#usuario = input("Digite o seu nome: ")
#senha = (input("Digite uma senha: "))

#if usuario == usuario_correto and senha == senha_correta:
  #  print(f"Olá {usuario}. Login bem sucedido")
#else:
 #   print("Crendencias inválidas. Tente Novamente")

#4 Solicite ao usuário as coordenadas(x,y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeira quadrante: os valores de x e y devem ser maiores que zero
# Segunda quadrante: o valor de x é menor que zero e o valor y é maior que zero
# terceiro quadrante: os valores de x e y devem ser menores que zero
# quarto quadrante: o valor de x é maior que zero e o valor de y é menor que zero
# caso contrario: o ponto está localizado no eixo ou origem

'''
x = float(input("Digite o valor do x: ")) #float para considerar numeros negativos
y = float(input("digite o valor de y: "))

if x > 0 and y > 0:
    print("Primeiro quadrante")
elif x < 0 and y > 0:
    print("Segundo quadrante")
elif x < 0  and y < 0:
    print("Terceiro quadrante")
elif x > 0 and y < 0:
    print("Quarto quadrante")
else:
    print("O ponto está sobre um eixo ou na origem")
'''
'''
#Crie uma lista para cada informação a seguir: -Lista de números de 1 a 10; - Lista com quatro nomes; - Lista com o ano que você nasceu e o ano atual

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['roberto','carlos','santos']
lista_ano = [2007,2026]

#Utiliza um loop para percorret todos os elementos da lista

for numero in lista_numeros:
    print(numero)

for nome in lista_nomes:
    print(nome)

for ano in lista_ano:
    print(ano)
'''

'''
#Utilize um loop for para calcular a soma dos numeros impares de 1 a 10
impares  = []

for numero in range(1,11):
    if numero % 2 !=0:
        impares.append(numero)

total = sum(impares) # para somar todos os numeros 
print(total)
'''
'''
#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
colecao = []
for numero in range (1,11):
    colecao.append(numero)

colecao.sort(reverse=True) # Para inverter a ordem e deixar decrescente. sort() - Ordem crescente ; (reverse=True) - Ordem descrescente
print(colecao)
'''

'''
#Solicite ao usuário um número e, em seguida, utilie um loop for para imprimir a tabuada desse número, indo de 1 a 10.
entrada = int(input("Digite o número: "))

for n in range(1,11):
    print(f'{entrada} X {n} = {entrada*n}')
'''

'''
#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possiveis exceções.
lista_numeros = [2,4,6,8,10]
soma  = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f'Soma: {soma}')
except Exception as e:
    print(f"Ocorreu um erro: {e} ")
'''

'''
#Construa um codigo que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisao por zero, caso a lista esteja vazia
lista_valores = [15,20,25,30]
soma = 0

try:
    for numero in lista_valores:
        soma += numero
    media =  soma / len(lista_valores)
    print(f"Média da lista: {media}")
except ZeroDivisionError: #ZeroDivisionError para caso de divisao por zero.
    print("A lista está vazia, não é possivel calcular a média")
except Exception as e:
    print(f'Ocorreu um erro: {e}')
'''
'''
#Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = [{'nome': 'Murilo', 'idade': 19, 'cidade': 'São Paulo'},
          {'nome': 'Roberto', 'idade': 45, 'cidade': 'Brasilia'},
          {'nome': 'Matheus', 'idade': 25, 'cidade': 'São Paulo'}
          ]

# Utilizando o dicionário criado no item 1: 
# - Modifique o valor de um dos itens no dicionário(por exemplo, atualize idade da pessoa);
pessoa[0]['nome'] = 'Erisvaldo'
pessoa[1]['idade'] = 99
pessoa[2]['cidade'] = 'Acre'
print(pessoa) 

# - Adicione um campo de profissão para essa pessoa; 
pessoa[0]['profissao'] = 'Engenheiro'
print(pessoa)

# - Remova um item do dicionário
del pessoa[0]['profissao']
print(pessoa)
'''
'''
# Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrado = {x: x**2 for x in range(1,6)}
print(numeros_quadrado)

# Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário
pessoa = {'nome': 'amanda', 'idade': 19, 'cidade': 'São Paulo'}

if 'nome' in pessoa: 
    print("A chave 'nome' existe no funcionário")
else:
    print("A chave 'nome' não existe no dicionário")
'''

# Escreva um código que conte a frequência de cada palavra em uma frase utlizando um dicionário.
frase = "Hoje é Sexta-Feira e amanhã é sabádo"
contagem_palavras = {}
palavras = frase.split() #quebra a frase em palavras sempre que encontra um espaço

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra,0)+1 #faz a verificação se a palavra já está no dicionário, se sim adicinar mais um, senão adiciona

print(contagem_palavras)