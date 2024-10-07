saldo = 0.0
valor_deposito = 0.0
valor_saque = 0.0
extrato = []
opcao_menu = 0

def deposito(valor_deposito, saldo, extrato):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f"Depósito de R${valor_deposito:.2f} realizado. Saldo: R${saldo:.2f}")
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}")
    else:
        print("Informe um valor válido.")
    return saldo, extrato

def saque(valor_saque, saldo, extrato):
    if valor_saque > 0 and valor_saque <= saldo:
        saldo -= valor_saque
        extrato.append(f"Saque de R${valor_saque:.2f} realizado. Saldo: R${saldo:.2f}")
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}")
    else:
        print("Informe um valor válido ou verifique se tem saldo suficiente.")
    return saldo, extrato

while opcao_menu != 5:
    print('''                Olá, bem-vindo ao sistema          
                  Por gentileza, escolha uma opção no menu abaixo
          1- Verificar o saldo;
          2- Consultar o extrato;
          3- Realizar um depósito;
          4- Realizar um saque;
          5- Sair do aplicativo;''')
    
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu:
        case 1:
            print(f"Seu saldo atual é de: R${saldo:.2f}")

        case 2:
            if extrato == []:
                print("Nenhuma movimentação realizada")
            else:
                print(f"Esse é seu histórico atual no extrato:\n {extrato}\nSaldo atual: R${saldo:.2f}")

        case 3:
            valor_deposito = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = deposito(valor_deposito, saldo, extrato)
        
        case 4:    
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(valor_saque, saldo, extrato)
        
        case 5:
            print("Obrigado por utilizar o aplicativo. Até a próxima! ^-^")
        
        case _:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
