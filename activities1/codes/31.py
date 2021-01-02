// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


casa=float(input("Qual o valor da casa? "))
salario=float(input("Qual o seu salário? "))
anos=int(input("Quantos anos você irá pagar? "))

parcela=casa/(anos*12)

if parcela>0.3*salario:
    print("Emprestimo não permitido.")
else:
    print("Emprestimo aprovado, o valor da parcela será R$ {:.2f}".format(parcela))
