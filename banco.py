menu = """
      
      [D] - Depositar
      [S] - Sacar
      [E] - Extrato
      [Q] - Sair
      
=> """

saldo = 0
extrato = ""
saques = 0
LIMITE_DIARIO = 3
opcao = ""


while opcao != "Q":
    
    opcao = input(menu)
    
    if opcao.upper() == "D":
     
        print('--- DEPOSITO ---')  
        deposito = float(input("Informe o valor a ser depositado: "))
        
        if(deposito > 0):
            saldo += deposito
            print(f'Deposito de R$ {deposito:.2f} efetuado!!\n')
            extrato += (f"Depósito: {deposito:.2f}\n")
            
        else:
            print('Valor inválido')

    elif opcao.upper() == "S":
        
        print('--- SAQUE ---')
        
        if(saques >= LIMITE_DIARIO):
            print("Já atingiu o limite de saque diário!!")
        else:
            valor = float(input("Informe o valor do saque: "))
            
            if(valor > saldo):
                print("Saldo insuficiente!!")
            elif (valor >= 500):
                print('Limite máximo por saque é R$ 500,00')  
            else:
                saldo -= valor
                print('Saque efetuado com sucesso!')
                extrato += (f"Saque: {valor:.2f}\n")
                saques += 1
                     
    elif opcao.upper() == "E":
        
        print('\n================ EXTRATO ================')
        print("Não foram realizadas movimentações." if not extrato else extrato)    
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao.upper() == "Q":
        break
    
    else:
        print('Opcao invalida, tente novamente')