// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


import random
n1=str(input("Digite o nome do aluno 1 :"))
n2=str(input("Digite o nome do aluno 2 :"))
n3=str(input("Digite o nome do aluno 3 :"))
n4=str(input("Digite o nome do aluno 4 :"))
lista=[n1,n2,n3,n4]
print("O aluno que irá apagar o quadro é o número: {}" .format(random.choice(lista)))

