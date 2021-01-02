// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


altura=float(input("Digite a sua altura [m]: "))
peso=float(input("Digete o seu peso [kg]: "))
imc=peso/(altura*altura)
print("Seu imc é {:.2f} e você está: ".format(imc))
if imc <18:
    print("Abaixo do peso.")
elif 25>=imc>18:
    print("Peso normal.")
elif 30 >= imc > 25:
    print("Sobrepeso.")
elif 30 <= imc < 40:
    print("Obesidade.")
else:
    print("Obesidade morbida.")

