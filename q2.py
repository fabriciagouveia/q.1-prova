#Annanda Lopes Jacobs e Fabricia Dos Santos Gouveia

alunos = []
maior_nota = 0
menor_nota = 1000

for _ in range(10):
    nome = input("Digite o nome do aluno:")
    nota = float(input("Digite a nota do aluno:"))

    while nome in [aluno[0] for aluno in alunos]:
        print("Nome ja existente, digite outro nome:")
        nome = input("Digite o nome do aluno:")

    while nota < 0 or nota > 10:
        print("Nota invalida, digite uma nota entre 0 e 10:")
        nota = float(input("Digite a nota do aluno:"))

        alunos.append([nome, nota])
    menu= True
    while True:
        print("\nMenu:")
        print("1. Informar aluno com menor e maior nota")
        print("2. Informar a média geral da turma")
        print("3. Sair")

        opcao = int(input("Escolha uma opção:"))

        if opcao == 1:
            if nota > maior_nota:
                maior_nota = nota
            if nota < menor_nota:
                menor_nota = nota
                print("menor nota:", menor_nota)
                print("maior nota:", maior_nota)
        elif opcao == 2:
            media = sum(aluno[1] for aluno in alunos) / len(alunos)
            print("media geral da turma:", media)
            if media <6:
                print("situação da turma: ruim")
            elif 6 <= media <=7:
                print("situação da turma: regular")
            elif 7.1 <= media <=8.9:
                print("situação da turma: boa")    
            else:
                print("situação da turma: excelente")
        elif opcao == 3:
            print("Encerrando o programa.")
            break
        else:
            print("Opção invalida. Escolha novamente")
