import os
os.system("cls||clear")

lista_numero = []
lista_negativa = []
lista_positiva = []
lista_maior = []
lista_menor = []

for i in range(3):
    numero =float(input(f"Digite o {i+1}° numero: "))
    lista_numero.append(numero)
    
    def positivo_negativo(numero):
        if numero > 0:
            lista_negativa.append(numero)
        else:
            lista_positiva.append(numero)
        quantidade_negativos = len(lista_negativa)
        soma_positivo = sum(lista_positiva) 

    def maior_menor(numero):
        maior_numero = max(numero)
        menor_numero = min (numero)
        lista_maior.append(maior_numero)
        lista_menor.append(menor_numero)

    def impares_pares(numero):
        pares = 0
        if numero % 2 == 0:
            pares +=1
        
        return numero,positivo_negativo,maior_menor
    
    

print("\n=====Saida=====")
positivo_negativo(numero)
maior_menor(numero)
for contador, numero in enumerate(lista_numero):
    print(f"{contador +1}ª numero: {numero}")
        