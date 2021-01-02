// -------------------------------------------------------------------------
// github.com/souza10v
// souza10vv@gmail.com
// -------------------------------------------------------------------------


print("====="*10)
times = ('Santos', 'Flamengo', 'Palmeiras', 'Atlético', 'São Paulo',
         'Corinthians', 'Internacional', 'Atlético-PR', 'Botafogo', 'Bahia',
         'Ceará SC', 'Goiás', 'Grêmio', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Chapecoense', 'Fluminense', 'CSA', 'Avaí')

print("Os cinco primeiros times são: {} ".format(times[:5]) )
print("Os quatro últimos: {} ".format(times[-4:]))
print(f"Os times em ordem: {sorted(times)} ")
print(f"O Chapecoense está na poscição {times.index('Chapecoense')} posição.")
print("====="*10)
