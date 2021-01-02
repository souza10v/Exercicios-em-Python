// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


lista=[]
listap=[]
listai=[]
s=0
lista.append(int(input("Insira um valor: ")))
while True:
    s=input("Deseja continuar? [S/N] ").upper()
    if s == 'S' :
        num=int(input("Insira um valor: "))
        lista.append(num)
        if num % 2 == 0:
            listap.append(num)
        else:
            listai.append(num)
    else:
        break

print(f"Você digitou {len(lista)} elementos e a lista é {lista}")
listap.sort()
print(f"Os números pares são {listap}")
listai.sort()
print(f"Os números impares são {listai}")
