// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


viagem= int(input("Qual a distância da sua viagem? "))
if viagem>200:
    print("A sua viagem de {:.0f} tem um custo de {:.2f} reais .".format(viagem, viagem * 0.45))
else:
    print("A sua viagem de {:.0f} tem um custo de {:.2f} reais ." .format(viagem,viagem*0.5))

