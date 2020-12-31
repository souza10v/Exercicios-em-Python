// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


v=float(input("Qual a velocidade?"))
if v > 80:
    print("Você está a {:.2f} acima da velocidade e será multado em {:.2f} reais." .format(v-80,(v-80)*7))
else:
    print("Você está na velocidade permitida")
