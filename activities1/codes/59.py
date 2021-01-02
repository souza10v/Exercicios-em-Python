// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


n=int(input("Digite um número. [ 999 para parar]: "))
k=1
s=0
while n != 999:
    s+=n
    n = int(input("Digite um número. [ 999 para parar]: "))
    k+=1
print("Foram digitados {} números e a soma é {}.".format(k,s))
