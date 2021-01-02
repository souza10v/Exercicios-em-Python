// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


value =str("S")
k=1
n = int(input("Digite um número: "))
value = str(input("Quer continuar? [S/N] ")).upper()
maior = menor =media =n

while value != "N":
    n = int(input("Digite um número: "))
    value=str(input("Quer continuar? [S/N] " )).upper()
    media=float((n+media)/2)
    if n > maior:
        maior=n
    elif n < menor:
        menor=n
    k+=1
print("Foram digitados {} números e a média é {:.2f}.".format(k,media))
print("O maior número é {} e o menor é {}.".format(maior,menor))
