// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


frase=str(input("Digite a frase:")).strip().upper() #strip tira espaços vazio e upper todas maisculas
palavras=frase.split() #quebra as palavras e transforma em um array
junto=''.join(palavras) #une as palavras[
inverso=''
for c in range (len(junto)-1,-1,-1):
    inverso += junto[c]
if inverso==junto:
    print("É um palindro.")
else:
    print("Não é um palindro.")
