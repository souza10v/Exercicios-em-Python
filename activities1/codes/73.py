// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


ista=[]
n=0
maior=0
p1=0
menor=0
p2=0
while n < 5:
    lista.append(int(input(f"Insira o valor {n+1}: ")))
    if n==0:
        maior=lista[n]
        menor=lista[n]
    elif lista[n]>maior:
        maior=lista[n]
        p1=n
    elif lista[n]<menor:
         menor=lista[n]
         p2=n
    n+=1
print(f"A lista é: {lista}")
print(f"O maior é {maior} na posição da lista ", end='')
for i,v in enumerate(lista):
    if v==maior:
        print(f"{i+1}...",end="" )
print('')
print(f"O menor é {menor} na posição da lista ", end='')
for i,v in enumerate(lista):
    if v==menor:
        print(f"{i+1}...",end="" )
