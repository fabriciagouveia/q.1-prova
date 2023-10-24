#Annanda Lopes Jacobs e Fabricia Dos Santos Gouveia

numeros_totais = 0
numeros_primos = []
numeros_nao_primos = []
continuar = True

while continuar:
    numero = int(input("Digite um numero inteiro (negativo para sair): "))

    if numero <0:
        continuar = False
    else:
        numeros_totais += 1
        is_primo = True
        if numero >1:
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    is_primo = False

        if is_primo:
            numeros_primos.append(numero)
        else:
            numeros_nao_primos.append(numero)

print("Quantidade total de numeros digitados:", numeros_totais)
print("Quantidade total de numeros primos:", len(numeros_primos))
print("Lista de numeros primos:", numeros_primos)
print("Lista de numeros não primos:", numeros_nao_primos)