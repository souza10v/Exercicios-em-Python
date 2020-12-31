// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


from random import randint
n=randint(0,5)
num = float(input("Advinhe um número entre 0 e 5. Em que número eu pensei? "))
if num==n :
    print("Você acertou!!!!")
else:
    print("Número errado. O número certo é {} .".format(n))
