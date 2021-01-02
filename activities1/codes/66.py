// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


print("====="*10)
valor=int(input("Qual valor você deseja sacar: "))
print("====="*10)
valors=valor
resto=sacado=0
notas = [50,20,10,1]
#while resto != 0:
for c in notas:
 # print(c)
  if valors == c:
         print("Total de 1 notas de {}.".format(c))
         break
  else:
#if c >= valor:
     n1=round((valor/c)-0.5)
     #print(n1)
     n1=int(n1)
     #if n1 < 1:
        #n1=0
     if n1 != 0:
        print("Total de {:.0f} notas de {}.".format(n1,c))
        sacado += (n1 * c)
       # print(c)
       # print(sacado)
      #  print(valors)
        if sacado >= valors-1:
            break
     n2=(valor%c)
     #print(n2)
     valor=n2
print("====="*10)
print("Fim")
