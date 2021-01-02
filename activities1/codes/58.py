// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


print("Sequencia de Fibonnaci")
n=int(input("Quantos números da sequência de Fibonnaci? "))
a=1
c=0
f=1
print("{}".format(a),end=' -> ')
while c < n-1:
    f1=f
    f=a
    print("{}".format(f),end=" -> ")
    a=a+f1
    c+=1
print("Fim")
