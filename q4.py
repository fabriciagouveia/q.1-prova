#Annanda Lopes Jacobs e Fabricia Dos Santos Gouveia

cardapio = {
    100: {"Especificação": "Cachorro quente", "Preço": 1.20},
    101: {"Especificação": "Bauru simples", "Preço": 1.30},
    102: {"Especificação": "Bauru com ovo", "Preço": 1.50},
    103: {"Especificação": "Hambúrger", "Preço": 1.20},
    104: {"Especificação": "Cheeseburguer", "Preço": 1.30},
    105: {"Especificação": "Refrigerante", "Preço": 1.00}
}

pedido = []
total = 0

while True:
    print("\nMenu Inicial:")
    print("1. Cardápio")
    print("2. Realizar pagamento")
    print("3. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("\nCardápio:")
        for codigo, item in cardapio.items():
            print(codigo, "-", item["Especificação"], "-", f"R${item['Preço']:.2f}")
        
        while True:
            codigo = int(input("Digite o código do produto desejado (ou 0 para voltar ao menu): "))
            if codigo == 0:
                break
            if codigo not in cardapio:
                print("Código inválido. Tente novamente.")
                continue
            
            quantidade = int(input("Digite a quantidade desejada: "))
            pedido.append({"Código": codigo, "Quantidade": quantidade})
            
            mais = input("Deseja adicionar mais algum item? (S/N): ")
            if mais.lower() != "s":
                break
            
    elif opcao == 2:
        total = 0
        print("\nPedido:")
        for item in pedido:
            codigo = item["Código"]
            quantidade = item["Quantidade"]
            preco = cardapio[codigo]["Preço"]
            total_item = quantidade * preco
            total += total_item
            print(f"{quantidade} x {cardapio[codigo]['Especificação']} = R${total_item:.2f}")
        print("Total a pagar: R${:.2f}".format(total))
        
    elif opcao == 3:
        print("Encerrando o programa.")
        break
        
    else:
        print("Opção inválida. Escolha novamente.")
