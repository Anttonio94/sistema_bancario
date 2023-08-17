saldo = 2000
saque = 5000

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} saque realizado saque!")