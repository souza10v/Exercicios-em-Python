// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


total=k=baraton=0
baratop=100000000
print('---'*10)
print('           Cadastro       ')
print('---'*10)
while True:
    produto=str(input("Qual o produto: "))
    preco=float(input("Qual o preço do produto: "))
    total+=preco
    if preco >=1000:
        k+=1
    if preco <= baratop:
        baratop=preco
        baraton=str(produto)
    continuar=str(input("Deseja continuar? [S/N]")).upper()
    if continuar == "N":
        break
    print('---' * 10)
print('---' * 10)
print("O preço total dos produtos é R${:.2f}.".format(total))
print(f"Temos {k} produto custando mais que R$ 1000.00 .")
print("O produto mais barato foi {} custando {:.2f}.".format(str(baraton),baratop))

