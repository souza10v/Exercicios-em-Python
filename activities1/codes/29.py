// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


salario=float(input("Qual o seu salário? "))
if salario>1250:
    print('Seu salário de R$ {:.2f} será aumentado em 10%, portanto será R$ {:.2f}'.format(salario,salario*1.1))
else:
    print('Seu salário de R$ {:.2f} será aumentado em 15%, portanto será R$ {:.2f}'.format(salario,salario*1.15))
    
