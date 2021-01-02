// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


k=soma=n=0
while n != 999:
    n=int(input("Digite um número [999 para parar]: "))
    if n != 999:
        soma += n
        k += 1
print(f"A soma dos {k} números é {soma}.")
