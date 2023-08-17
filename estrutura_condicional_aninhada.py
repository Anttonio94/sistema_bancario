Conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

if Conta_normal:
    if saldo >= saque:
        print(" Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print(" Saque realizado com uso do cheque especial")
    else:
        print(" Não foi possivel realizar saque! saldo insufuciente")    

elif  conta_universitaria:
    
    if saldo>= saque:
        print ("saque realizado com sucesso!")
    else:
        print ("saldo insuficiente!")