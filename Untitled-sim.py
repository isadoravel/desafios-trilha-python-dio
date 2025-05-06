saldo = 2000.00
qtd_saque = 0
saques_realizados = []
depositos_realizados = []
opcoes_operacoes = ["s", "d", "e", "q"]


menu_centralizado = ("Bem vindo! Informe a operação que deseja realizar: \n ----- [s]: saque, [d]: depósito, [e]: extrato, [q]: sair ---- \n operação:e").center(151)

operacao = input(menu_centralizado).lower().strip()

while operacao in opcoes_operacoes:

    if operacao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        if valor_deposito <= 0:
            print("Valor do depósito mínimo: R$ 1,00\n")
        else: 
            depositos_realizados.append(valor_deposito)
            saldo += valor_deposito
            print(f"Depósito no valor de {valor_deposito:.2f} realizado com o sucesso")
            

    elif operacao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        if valor_saque > 500:
            print("O limite de valor por saque é R$ 500,00. Saque não realizado")
        elif valor_saque > saldo:
            print("O valor do saque é maior que o valor do saldo. Saque não realizado")
        elif qtd_saque >= 3:
            print("O limite de 3 saques diários foi excedido. Saque não realizado\n")
        else: 
            qtd_saque += 1
            saques_realizados.append(valor_saque)
            saldo -= valor_saque
            print(f"Saque no valor de {valor_saque:.2f} realizado com o sucesso")
            
    elif operacao =="e":
        print("\n=============== EXTRATO ===============")
        if not depositos_realizados and not saques_realizados:
            print("Não foram realizadas movimentações")
        else: 
            print("Depósitos:")
            for i in depositos_realizados:
                print(f"R$:{i:.2f} \n")
            print("Saques: ")
            for i in saques_realizados:
                print(f"R$:{i:.2f} \n")
            print(f"Saldo final: {saldo}")

    else:
        print("Operação finalizada")
        break
    operacao = input(menu_centralizado).lower().strip()

print(f"Saldo: ")
print("\nSessão encerrada. Volte sempre!")