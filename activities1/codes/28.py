// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

if n1>n2:
    maior=n1
    menor=n2
else:
    maior=n2
    menor=n1

if maior>n3:
    maior=maior
else:
    maior=n3

if menor>n3:
    menor=n3
else:
    menor=menor

print("O maior número é {} e o menor número é {}." .format(maior,menor))

