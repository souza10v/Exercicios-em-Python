// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


from datetime import date
maiori=0
menori=0
ano=date.today().year
for c in range(0,8):
    anol=int(input(("Digite o {}º ano de nascimento: ".format(c))))
    if ano-anol>=18:
        maiori=maiori+1
    else:
        menori=menori+1
print("{} pessoas já atingiram a maior idade e {} são menores de ida-de.".format(maiori,menori))

