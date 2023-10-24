#Annanda Lopes Jacobs e Fabricia Dos Santos Gouveia

abaixo_peso_mulheres = 0
peso_ideal_mulheres = 0
acima_peso_mulheres = 0
acima_ideal_mulheres = 0
obesas_mulheres = 0

abaixo_peso_homens = 0
peso_ideal_homens = 0
acima_peso_homens = 0
acima_ideal_homens = 0
obesos_homens = 0

pessoas = int(input("Digite a quantidade de pessoas:"))

for _ in range(pessoas):
    sexo = input("Digite o sexo (m ou f):")
    altura = float(input("Digite a altura (em m):"))
    peso = float(input("Digite peso (em kg):"))

    imc = peso / (altura ** 2)

    print("IMC:", imc)

    if sexo.lower() == "f":
        if imc <19.1:
            abaixo_peso_mulheres += 1
        elif imc <25.8:
            peso_ideal_mulheres += 1
        elif imc <27.3:
            acima_peso_mulheres += 1
        elif imc <31.1:
           acima_ideal_mulheres += 1
        else:
            obesas_mulheres += 1
    elif sexo.lower() == "m":
        if imc <20.7:
            abaixo_peso_homens += 1
        elif imc <26.4:
            peso_ideal_homens += 1
        elif imc <27.8:
            acima_peso_homens += 1
        elif imc <32.3:
           acima_ideal_homens += 1
        else:
            obesos_homens += 1      

print("mulheres:")
print("abaixo do peso:", abaixo_peso_mulheres)
print("peso ideal:", peso_ideal_mulheres)
print("um pouco acima do peso:", acima_peso_mulheres)
print("acima do peso ideal:", acima_ideal_mulheres)
print("obesas:",obesas_mulheres)

print("homens:")
print("abaixo do peso:", abaixo_peso_homens)
print("peso ideal:", peso_ideal_homens)
print("um pouco acima do peso:", acima_peso_homens)
print("acima do peso ideal:", acima_ideal_homens)
print("obesas:",obesos_homens)