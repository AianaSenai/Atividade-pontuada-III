import os
os.system("cls||clear")

lista_numero = []
lista_negativa = []
lista_positiva = []
lista_pares = []
lista_impares = []

for i in range(3):
    numero =float(input(f"Digite o {i+1}° numero: "))
    lista_numero.append(numero)
    
    def impares_pares(numero):
        if numero % 2 == 0:
            pares += 1
            lista_pares.append(numero)
        else:
            impares += 1
            lista_pares.append(numero)
    
    
    def positivos_negativos(numero):
        if numero > 0:
            positivo += 1
        else:
            negativo += 1
        soma = sum(numero)
        media = soma /3
        return numero, impares_pares, positivos_negativos   
      
soma = sum(numero)
media = soma /3  

maior_numero = max(lista_numero)
menor_numero = min(lista_numero)
