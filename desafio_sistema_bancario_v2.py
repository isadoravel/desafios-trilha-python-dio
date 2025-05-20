

menu = ("""
        Bem vindo! Informe a operação que deseja realizar:
        [s]: saque, 
        [d]: depósito, 
        [e]: extrato, 
        [nu]: cadastrar novo usuário
        [nc]: cadastrar nova conta 
        [q]: sair  \n 
        Operação: 
        """)


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if valor > limite:
        print("\nO limite de valor por saque é R$ 500,00. Saque não realizado")
    elif valor > saldo:
        print("\nO valor do saque é maior que o valor do saldo. Saque não realizado")
    elif numero_saques > limite_saques:
        print("O limite de 3 saques diários foi excedido. Saque não realizado\n")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque R$: {valor:.2f}")
        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso")
    else:
        print("Valor informado inválido. Faça nova operaçaõ com valor válido")
        
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito R$:{valor:.2f}") 
        print(f"\nDepósito no valor de R$:{valor:.2f} realizado com sucesso")
    else:
        print("\nValor do depósito mínimo: R$ 1,00")
    
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("="*10 + "EXTRATO" + 10*"=")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(f"{transacao}\n")

    print(f"Saldo final: R${saldo:.2f}")
    print("="*27)
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    
    if filtrar_usuario(usuarios, cpf):
        print("Usuário já existe! Cadastre um novo CPF")
        return
    else:
        nome = input("\nInforme o seu nome: ")
        data_nascimento = input("\nInforme a data de nascimento no formato DD-MM-AA: ")
        endereço = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereço})

    print("Usuário criado com sucesso!")

def criar_conta_corrente(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF: ")

    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        print(f"""
              Conta criada com sucesso: \n" 
              Agência: {agencia}\n
              Número da conta: {numero_conta}\n
              Usuário: {usuario}\n
               """)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else: 
        print("CPF fornecido não corresponde a nenhum usuário. Criação de conta encerrada")
        return None

def filtrar_usuario(usuarios, cpf) -> int:
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado if usuario_filtrado else None

def listar_contas(contas_correntes):
    
    for conta in contas_correntes:
        conta_unica = f"""
                Agência: {conta["Agência"]}\n,
                Número da conta: {conta["Número da conta"]}\n,
                Usuário: {conta["usuario"]}\n
                """
        print(conta_unica)
    
    if not contas_correntes:
        print("Não há contas cadastradas")
        return None
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "001"
   


    saldo = 2000
    limite = 500
    extrato = []
    numero_saques = 0 
    contas_correntes = []
    usuarios = []


    cpf = input("Informe o CPF: \n")
    usuario = filtrar_usuario(usuarios, cpf)
        
    if not usuario:
        operacao = input("Usuário inexistente. Digite [nu] para novo usuário ou [q] para sair: \n")

        if operacao.lower() == "q":
            print("Sessão encerrada :)")
            return

        elif operacao.lower() == "nu":
            criar_usuario(usuarios)
            
        else:
            print("Opção inválida")

    while True:
                    
        try:

            operacao = input(menu)

            if operacao.lower() == "s":
                valor = float(input("Informe o valor que deseja sacar"))
                saldo, extrato, numero_saques = sacar(saldo= saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

            elif operacao.lower() == "d":
                valor = float(input("Informe o valor que deseja sacar"))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif operacao.lower() == "e":
                print(exibir_extrato(saldo, extrato= extrato))

            elif operacao.lower() == "nu":
                criar_usuario(usuarios)

            elif operacao.lower() == "nc":
                numero_conta = len(contas_correntes) + 1
                contas_correntes.append(criar_conta_corrente(AGENCIA, numero_conta, usuarios))

            elif operacao.lower() == "q":
                print("Sessão encerrada :)")
                break

            else:
                raise ValueError
                    
        except (ValueError):
            print("Opção inválida! Informe uma das opções que constam no menu\n")
                

main()
