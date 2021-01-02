// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


m=0
k=0;
for c in range (1,7):
    n=int(input("Insira um número: "))
    if n%2==0:
        m=n+m
        k=k+1
print("A soma dos {} números é {}".format(k,m))

