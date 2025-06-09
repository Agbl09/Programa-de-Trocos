valor_mercadoria = float(input("Valor da mercadoria: "))
valor_pago = float(input("Valor pago: "))

if valor_pago == valor_mercadoria:
    print("Não existe troco!")

elif valor_pago < valor_mercadoria:
    valor_faltante = round(valor_mercadoria - valor_pago, 2)

    print(f"Faltam R${valor_faltante}")

elif valor_pago > valor_mercadoria:
    troco = round(valor_pago - valor_mercadoria, 2)

    print(f"Troco: R${troco}")

    moedas_notas = [5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

    for moeda_nota in moedas_notas:
        quantidade = int(troco // moeda_nota)

        if quantidade > 0:
            if moeda_nota >= 2:
                print(f"{int(quantidade)} Nota(s) de R${moeda_nota}")
            
            else:
                print(f"{int(quantidade)} Moeda(s) de R${moeda_nota}")

            troco -= round(quantidade * moeda_nota, 2)