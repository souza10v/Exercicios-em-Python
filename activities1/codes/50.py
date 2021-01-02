// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


maior=0
menor=0
for c in range (1,6):
 peso=float(input(("Insira o peso {} em kg: ".format(c))))
 if c ==1:
     menor=peso
     maior=peso
 else:
   if peso>=maior:
     maior=peso
   elif peso<=menor:
     menor=peso
print("O maior peso é {} Kilos e o menor é {} Kilos.".format(maior,menor))
