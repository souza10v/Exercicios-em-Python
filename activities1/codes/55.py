// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


n=int(input("Digite um número a ser fatorado: "))
fatorial=n
text=0;
print("A solução para {}!: ".format(n), end='')
while n>1:
    print("{}".format(n),end=" X ")
    fatorial*= (n-1)
    n-=1
print("{} = {}".format(n,fatorial))

