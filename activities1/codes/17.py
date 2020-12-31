// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------



num=int(input('Digite um número:'))
n=str(num)
print("Analisando o número {}".format(num))
print("A unidade é: {} " .format(n[3]))
print("A dezena é: {}" .format(n[2]))
print("A centena é: {} " .format(n[1]))
print("O milhar é: {} " .format(n[0]))


num=int(input('Digite um número:'))
n=str(num)
u = num //1 %10
d = num //10 % 10
c = num // 100 %10
m = num //1000 %10
print("Analisando o número {}".format(num))
print("A unidade é: {} " .format(u))
print("A dezena é: {}" .format(d))
print("A centena é: {} " .format(c))
print("O milhar é: {} " .format(m))
