// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
k=True
while k == True:
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair")
    o=int(input("Digite a opção: "))
    if o == 1:
        print("A soma é de {} + {} = {}.".format(n1,n2, n1+n2))
        k == True
    elif o == 2:
        print("A muplicaçao de {} + {} = {}.".format(n1,n2,n1+n2))
        k == True
    elif o == 3:
        if n1 > n2:
            print("O maior número é: {}".format(n1))
            k == True
        else:
            print("o maior número é: {}".format(n2))
            k == True
    elif o  == 4:
        n1=int(input("Digite o novo primeiro número: "))
        n2=int(input("Digite o novo segundo número: "))
        k == True
    elif o == 5:
        print("Fim da execução.")
        k == False
        break
    else:
        print("Opção inválida.")
