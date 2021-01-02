// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


print("Gerador de PA")
print("-="*10)
n=int(input("Insira o primeiro termo: "))
r=int(input("Insira a razão da PA: "))
c=10
base=n
t=10
while c !=0:
    for i in range (0,c):
        base=(i*r)+n
        print("{}".format(base), end=" -> ")
        t+=1
    print("Pausa")
    c=int(input("Quantos termos você quer mostrar a mais? "))
    n=base
print("Progressão finalizada com {} termos." .format(t))
