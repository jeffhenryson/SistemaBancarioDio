# Dados das contas bancárias criada.
contas = {
    '12345': {'senha': 'senha123', 'saldo': 1000},
}

def autenticar(numero_conta, senha):
    if numero_conta in contas and contas[numero_conta]['senha'] == senha:
        return True
    else:
        return False

def sacar(numero_conta, valor):
    if contas[numero_conta]['saldo'] >= valor:
        contas[numero_conta]['saldo'] -= valor
        return True, "Saque realizado com sucesso."
    else:
        return False, "Saldo insuficiente."

def depositar(numero_conta, valor):
    contas[numero_conta]['saldo'] += valor
    return "Depósito realizado com sucesso."

def transferir(numero_conta_origem, numero_conta_destino, valor):
    if contas[numero_conta_origem]['saldo'] >= valor:
        contas[numero_conta_origem]['saldo'] -= valor
        contas[numero_conta_destino]['saldo'] += valor
        return True, "Transferência realizada com sucesso."
    else:
        return False, "Saldo insuficiente."

def doar(numero_conta, valor):
    if contas[numero_conta]['saldo'] >= valor:
        contas[numero_conta]['saldo'] -= valor
        # Aqui podemos adicionar o valor à uma conta de doação ou simplesmente removê-lo do sistema.
        return True, "Doação realizada com sucesso."
    else:
        return False, "Saldo insuficiente."

def verificar_saldo(numero_conta):
    return f"Seu saldo atual é: {contas[numero_conta]['saldo']:.2f} reais"

def exibir_menu():
    print("\nBem-vindo ao Sistema Bancário Simples")
    print("1. Sacar dinheiro")
    print("2. Depositar dinheiro")
    print("3. Transferir dinheiro")
    print("4. Doar dinheiro")
    print("5. Sair")

def exibir_menu():
    print("\nBem-vindo ao Sistema Bancário Simples")
    print("1. Sacar dinheiro")
    print("2. Depositar dinheiro")
    print("3. Transferir dinheiro")
    print("4. Doar dinheiro")
    print("5. Verificar saldo")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '6':
            print("Obrigado por usar o Sistema Bancário Simples. Até mais!")
            break
        
        numero_conta = input("Digite o número da sua conta: ")
        senha = input("Digite sua senha: ")
        
        if not autenticar(numero_conta, senha):
            print("Número da conta ou senha inválidos.")
            continue
        
        if opcao == '1':
            valor = float(input("Digite o valor que deseja sacar: "))
            sucesso, mensagem = sacar(numero_conta, valor)
            print(mensagem)
        elif opcao == '2':
            valor = float(input("Digite o valor que deseja depositar: "))
            mensagem = depositar(numero_conta, valor)
            print(mensagem)
        elif opcao == '3':
            numero_conta_destino = input("Digite o número da conta destino: ")
            valor = float(input("Digite o valor que deseja transferir: "))
            sucesso, mensagem = transferir(numero_conta, numero_conta_destino, valor)
            print(mensagem)
        elif opcao == '4':
            valor = float(input("Digite o valor que deseja doar: "))
            sucesso, mensagem = doar(numero_conta, valor)
            print(mensagem)
        elif opcao == '5':
            mensagem = verificar_saldo(numero_conta)
            print(mensagem)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
