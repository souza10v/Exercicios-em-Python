// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


media=0
maisvelho=0
maisvelhoi=0
quantsexo=0
for c in range (1,5):
    print("==== Cadastro {} ====".format(c))
    nome=str(input("Digite o nome: "))
    sexo=str(input("Digite o sexo: ").upper().strip())
    idade=int(input("Digete a idade: "))

    if c ==1:
        media=idade
        if sexo == 'F':
            if idade <20:
               quantsexo=1
        else:
            maisvelho=nome
            maisvelhoi=int(idade)
    else:
        media =(media+idade)/2
        if sexo =='F':
            if idade<20:
               quantsexo = int(quantsexo + 1)
        else:
            if idade > maisvelhoi:
                maisvelho=nome
print('A idade média do grupo é {}.'.format(media))
print("O homem mais velho do grupo é {}." .format(maisvelho))
print("A quantidade de mulheres com idade menor que 20 é {}.".format(quantsexo))

