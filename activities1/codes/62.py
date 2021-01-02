// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


n=1
while n > 0:
        print("==="*10)
        n=int(input("Quer ver o valor de qual tabubada? "))
        print("===" * 10)
        if n <= 0:
            break
        for k in range(1, 11):
            print(f"{k} X {n} = {k*n}")
print("Fim")

while True:
        print("==="*10)
        n=int(input("Quer ver o valor de qual tabubada? "))
        print("===" * 10)
        if n <= 0:
            break
        for k in range(1, 11):
            print(f"{k} X {n} = {k*n}")
print("Fim")
