// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


lista=[]
s=0
lista.append(int(input("Insira um valor: ")))
while True:
    s=input("Deseja continuar? [S/N] ").upper()
    if s == 'S' :
        lista.append(int(input("Insira um valor: ")))
    else:
        break
if 5 in (lista):
    print("O 5 está na lista.")
else:
    print("O 5 não está na lista.")
print(f"Você digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"A lista ordenada em ordem descresente é {lista }")

