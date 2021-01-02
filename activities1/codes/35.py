// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


n1=float(input("Insira a primeira nota:"))
n2=float(input("Insira a segunda nota:"))
media=(n1+n2)/2
if media >= 7:
    print("Aprovado.")
elif 7 > media >= 5:
    print("Recuperação.")
elif media < 5 :
    print("Reprovado.")
