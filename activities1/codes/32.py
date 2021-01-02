// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------



numero=int(input("Insira um número inteiro: "))
print('''[1] para converter para binário
[2] para converter para octal
[3] para converter para hexadecimal.''')
operacao=int(input("Sua opção:  "))

if operacao == 1:
    print("O número {} em binário é {}".format(numero,bin(numero)[2:]))
elif operacao == 2:
    print("O número {} em octal é {}".format(numero,oct(numero)[2:]))
elif operacao == 3:
    print("O número {} em hexadecimal é {}".format(numero,hex(numero)[2:]))
else:
    print("Opção inválida")

