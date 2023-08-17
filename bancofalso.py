menu = """"

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
 
    opcao = input(menu)
    
    if  opcao == "1":
        
        Valor = float(input("Informe o valor de depósito:")
                       )
        if valor > 0:
         saldo += valor 
         extrato += f"Depótio: R$ { valor: .2f}\n"
         
        else:
            print("Operação falhou o valor infomado é inválido.")
            
        
    elif opcao == "2":
        valor =float(input("infome o valor de saque."))
       
        excedeu_saldo = valor > saldo
       
        excedeu_limite = valor > limite
       
        excedeu_saques = numero_saques >= LIMITE_SAQUE 
       
        if excedeu_saldo:
            print("Operação falhou, saldo insuficiente")
        
        if excedeu_limite:
            print("Operação falhou! Limite insuficiente.")
        
        if excedeu_saques:
            print("Operação falhou! excede numero de saques.")
    
        elif valor > 0:
            saldo -= valor
            extrato  == f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else: 
            print("Operacação falhou! o valor informado é invalido.")
        

    elif opcao == "3":
        
        print("\n###########EXTRATO########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("########################")
        
    
    elif opcao =="4":
        break
    else:
         print("Opção inválida, por favor selecione novamente a opção desejada.")
