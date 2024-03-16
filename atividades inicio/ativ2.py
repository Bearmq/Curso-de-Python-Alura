'''1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Luiza', 'Ana', 'Gab', 'Lua']
ano = [2001, 2024]

print(f'{numeros}')
print(f'{nomes}')
print(f'{ano}')'''
'''2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

cores = ['Vermelho', 'Azul', 'Amarelo', 'Preto', 'Rosa']

for cores in cores:
    print(f'{cores}')'''

'''3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0

for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)'''

'''4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)'''


'''5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Digite um número: '))

for i in range (1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')'''


'''6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_de_numeros = [45, 8, 9, 2, 1]
soma = 0
try:
    for numero in lista_de_numeros:
        soma += numero
        print(f"Soma dos elementos: {soma}")
except Exception as e:
     print(f"Ocorreu um erro: {e}")'''



'''7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")'''
