// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


lista=["zero", 'um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
while True:
    n = int(input("Digite um número: "))
    if n > 19:
        print("Digite um número menor que 20.")
    else:
        break
print(f"O número é {lista[n]}")

