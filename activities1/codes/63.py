// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


from random import randint
k=0
print("----" * 10)
print("Vamos jogar Par ou Impar?")
while True:
    print("----" * 10)
    n1=int(input("Digite um valor: "))
    n2=randint(1,20)
    v=str(input("Par ou Impar? [P/I]:")).upper()
    if (n1+n2)%2==0  and v=="P":
        print(f"A soma dos números é {n1+n2}, voce jogou PAR e ganhou.")
        k += 1
        print("Jogue novamente...")
    else:
        print(f"A soma dos números é {n1 + n2}, voce jogou IMPAR e perdeu.")
        break
print("----" * 10)
print("Fim de Jogo.")
print("----" * 10)
print(f"Você venceu {k} vezes.")

