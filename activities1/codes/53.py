// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


from random import randint
nrand= randint(1,11)
k=0
n=int(input("Digite o seu palpite entre 1 e 10: "))
while n != nrand:
    n=int(input("Número inválido. Digite outro palpite: "))
    k+=1
print("Certa resposta. Foram utilizados {} palpites até o acerto.".format(k))
