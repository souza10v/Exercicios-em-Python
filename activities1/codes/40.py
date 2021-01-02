// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


import random,time

print("Selecione uma opção:")
print("[1] Pedra.")
print("[2] Papel.")
print("[3] Tesoura.")
select=int(input("Qual é a jogada? "))
if select ==1:
    select="Pedra"
elif select ==2:
      select="Papel"
else :
    select="Tesoura"
print("Você escolheu {}... ".format(select))

pcselect= random.randint(0,2)

if pcselect==0:
    pcselect="Pedra"
elif pcselect==1:
    pcselect="Papel"
elif pcselect ==2:
    pcselect="Tesoura"
print("")
time.sleep(0.4)
print("JO")
time.sleep(0.4)
print("KEN")
time.sleep(0.4)
print("PO")
time.sleep(0.4)
print("")
if select==pcselect:
    print("Empate")
elif select =="Pedra" and pcselect=="Tesoura":
    print("Você jogou {} e o PC {} . Você venceu!".format(select,pcselect))
elif select =="Pedra" and pcselect=="Papel":
    print("Você jogou {} e o PC {} . Você Perdeu!".format(select,pcselect))
elif select== "Papel" and pcselect=="Tesoura":
    print("Você jogou {} e o PC {} . Você venceu!".format(select,pcselect))
elif select=="Papel" and pcselect=="Pedra":
    print("Você jogou {} e o PC {} . Você Perdeu!".format(select,pcselect))
elif select =="Tesoura" and select=="Papel":
    print("Você jogou {} e o PC {} . Você venceu!".format(select,pcselect))
elif select =="Tesoura" and select == "Papel":
    print("Você jogou {} e o PC {} . Você Perdeu!".format(select,pcselect))

