// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


valor= float(input("Insira o valor da compra:"))
print("Selecione o tipo de pagamento:")
print("[1] Pagamento à vista no dinheiro.")
print("[2] Pagamento à vista no cartão.")
print("[3] Pagamento 2 vezes no cartão.")
print("[4] Pagamento será em mais de 3 vezes")
pag=int(input("Selecione o tipo de pagamento: "))
if pag ==1:
    print("O pagamento de {:.2f} será à vista no dinheiro e o valor será R$ {:.2f}.".format(valor, valor*0.9))
elif pag ==2:
    print("O pagamento de {:.2f} será à vista no cartão e o valor será R$ {:.2f}.".format(valor,valor * 0.95))


elif pag ==3:
    print("O pagamento de {:.2f} será em 2 vezes no cartão com parcelas de {:.2f} re-ais.".format(valor,valor/2))
elif pag ==4:
    n=int(input("Quantas parcelas? "))
    print("O pagamento de {:.2f} será em {} vezes com parcelas de {:.2f}.".format(valor,n,valor*1.2/n))
else:
    print("Favor inserir um valor válido.")
