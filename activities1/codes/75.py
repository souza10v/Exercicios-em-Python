// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


lista=[]
for c in range (0,5):
    n=(int(input("Insira um valor: ")))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f"O número {n} está na posição {c+1}.")
    else:
        pos=0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"O número {n} está na posição {pos+1}.")
                break
            pos += 1
print(f"A lista é {lista}")
