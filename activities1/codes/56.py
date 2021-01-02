// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


print("Gerador de PA")
print("-="*10)
n=int(input("Insira o primeiro termo: "))
r=int(input("Insira a razão da PA: "))
c=1
print(n,end=" -> ")
while c !=10:
    print("{}".format((c*r)+n), end=" -> ")
    c += 1
print("Fim.")
