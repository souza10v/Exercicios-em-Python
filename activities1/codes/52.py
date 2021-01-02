// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


s = str(input("Digite o sexo [M/F]: ")).upper().strip()
while s != "M" and 'F':
    s = str(input("Sexo inválido. Digite o sexo [M/F]: ")).upper().strip()
print('Sexo {} valido.'.format(s))
