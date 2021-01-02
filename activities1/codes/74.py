// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


lista=[]
lista.append(int(input("Insira um valor: ")))
print("Valor adicionado com sucesso...")
while True:
    value=input("Deseja continuar? [S/N] ").upper()
    if value == "S":
        n=int(input("Insira um valor: "))
        if n not in lista:
            lista.append(n)
        else:
            print("Número duplicado.")
    else:
        print("Analisando...")
        break
lista.sort()
print(lista)

