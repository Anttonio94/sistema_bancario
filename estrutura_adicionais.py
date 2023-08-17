MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade =int(input("informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade< MAIOR_IDADE:
    print("Não pode tirar a CNH.")



if idade >= MAIOR_IDADE:
    print("Maior idade , pode tirar a CNH.")
else:
    print("ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("pode fazer aula teóricas, mas não aulas praticas.")
else:
    print("ainda não pode tirar CNH.")