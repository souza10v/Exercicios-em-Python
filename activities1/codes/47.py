// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


n=int(input("Insira o número: "))
k=0
a=0

for c in range (1,n+1,1):
    if n%c==0:
        print("\033[33m {}".format(c), end=" ")
        k=1+k
    else:
        print("\033[31m{}".format(c), end=" ")
        a=1+a
print('')
if k<=2:
    print("\n\033[m O número {} foi divido {} vezes e é primo.".format(n,k))
else:
    print("\n\033[m O número {} foi divido {} vezes e não é primo".format(n,a))

