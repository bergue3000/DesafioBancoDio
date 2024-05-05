import os
print("****************** SELECIONE A OPÇÃO DESEJADA ******************")
MENU = """
                ##########--MENU--##########
                #     (D): DEPOSÍTAR     #
                #     (E): EXTRATO       #
                #     (S): SACAR         #
                #     (Q): SAIR          #
                ############################
"""
saldo = 0
saque = 0
extrato = 0
numero_saque = 0
limite_saque = 3
sair = "Q"

opcao = input(MENU).upper()

while True:
    
    if opcao == "D":
        os.system("cls")
        deposito = 0
        print("---------------- DEPOSITO ------------------------------")
        deposito = float(input("Valor do Deposito R$: "))
        if deposito > 0:
            print("--------------------------------------------------------")
            print(f"Saldo Anterior R$:{saldo:.2f}")
            print("--------------------------------------------------------")
            saldo += deposito
            print("--------------------------------------------------------")
            print(f"O Saldo Atual R$:{saldo:.2f}")
            print("--------------------------------------------------------")
        else:
            print("Valor não permitido, somente e permitido valores positivos")
        
        print("************** SELECIONE A OPÇÃO DESEJADA **************")
        print("--------------------------------------------------------")
        opcao = input(MENU).upper()
    elif opcao == "E":
        os.system("cls")
        print("******************* SALDO DA CONTA ********************")
        print(f"""
        
            Total em Conta R$:{saldo:.2f}
            
            """)
        print("--------------------------------------------------------")
        print("************** SELECIONE A OPÇÃO DESEJADA **************")
        opcao = input(MENU).upper()
    elif opcao == "S":
        os.system("cls")
        saque_maximo = 500.
        
        print("******************** SAQUE ****************************")
        saque = float(input("valor do Saque R$:"))
        if  numero_saque < limite_saque and saque <= saldo and saque < saque_maximo:
            print(f"Saldo Anterior R$:{saldo:.2f}")
            saldo -= saque
            print(f"Saldo Atual R$:{saldo:.2f}")
            numero_saque += 1
            
        elif numero_saque >= limite_saque and saque < saque_maximo:
            print()
            print("***** Limite Diario de Saque atingido! *****")
            print()
        elif saque > saque_maximo:
            print(" Valor Maximo de saque excedido")
        else:
            os.system("cls")
            print("---------------------------------------------------")
            print("********* Saldo insuficiente para saque ***********")
            print()

        print("-------------------------------------------------------")
        print("************* SELECIONE A OPÇÃO DESEJADA **************")
        opcao = input(MENU).upper()
    elif opcao == "Q":
        os.system("cls")
        print("******************** Sair ****************************")
        print("Sair, Volte sempre!")
        break
    else:
        os.system("cls")
        print(" Opção invalida tente novamente!")
        print("************* SELECIONE A OPÇÃO DESEJADA *************")
        opcao = input(MENU).upper()
