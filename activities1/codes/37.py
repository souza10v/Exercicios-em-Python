// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


s1=int(input("Primeiro segmento: "))
s2=int(input("Segundo segmento: "))
s3=int(input("Terceiro segmento:"))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1 :
    print("É possível formar um triângulo. ")
    if s1==s2==s3:
        print("Triângulo equilátero")
    elif s1 != s2 != s3:
        print("Triângulo escaleno")
    else:
        print("Triangulo isóceles.")
else:
    print("Não é possível formar um triângulo. ")

