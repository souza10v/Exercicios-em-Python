// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------



nome=str(input('Insira uma frase? ')).strip().lower()
letra=str(input('Qual letra você que buscar? '))
print('A letra {} aparece {} vezes.' .format(letra,nome.count(letra)))
print('Primeiro {} na posição {} e último na {}.'.format(letra,nome.find(letra)+1,nome.rfind(letra)+1))
