// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


name=str(input("Digite o seu nome: ").strip())
print ("O nome em maisculo é {}. " .format(name.upper()))
print ("O nome em minusculo é {}. ".format(name.lower()))
print ("O nome tem {} caracteres." .format((len(name) - name.count(' '))))
#print ("O seu primeiro nome tem {} letras".format(name.find(' ')))
separa=name.split()
print('Seu primeiro nome é {} e ele tem {} letras.' .format(separa[0], len(separa[0])))
