// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


id=sexom=sexof=con=0
while True:
    print("---"*10)
    print("CADASTRE UMA PESSOA")
    print("---" * 10)
    i=int(input("Qual a idade:"))
    sexo=str(input("Qual o sexo? [M/F]")).upper()
    if i >= 18:
        id+=1
    if sexo == 'M':
        sexom+=1
    elif sexo =="F" and i <20:
        sexof+=1
    con=str(input("Quer continuar?[S/N]")).upper()
    if con=="N":
         break
print(f"Total de pessoas com mais de 18 anos: {id}.")
print(f"Ao todo há {sexom} cadastrado.")
print(f"E há {sexof} mulher com menos de 20 anos. ")
