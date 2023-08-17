texto = ""
VOGAIS ="AAPIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:     
    print()   #adiciona uma quebra de lina
    
#exemplo ultilixando a funcao built-in range
for numero in range( 0, 78, 6):
    print(numero, )