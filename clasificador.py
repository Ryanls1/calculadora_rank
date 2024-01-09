import random

nome = input('digite o nome do heroi: ')
decisao = input('gostaria de definir seu xp? S/N: ')

S = 0

faixas = {
    'Ferro':(float('-inf'),1000),
    'Bronze':(1001, 2000),
    'Prata':(2001, 5000),
    'Ouro':(5001, 7000),
    'Platina':(7001, 8000),
    'Ascendente':(8001, 9000),
    'Imortal':(9001, 10000),
    'Radiante':(10001, float('inf'))
       }

if decisao.lower() in {'s', 'sim'}:
    while True:
        S = input('Defina seu xp: ')
        if S.isdigit():
            S = int(S)
            break
    for categoria, (valor_mini, valor_max) in faixas.items():
        if valor_mini <= int(S) <= valor_max:
            print(f'o heroi {nome} com base no seu xp que é {S} ele esta na categoria {categoria}')
            break

elif decisao.lower() in {'n', 'nao', 'não'}:
    xp_aleatorio = random.randint(1,10000)
    print(f'seu xp sera gerado aleatoriamente {xp_aleatorio}')
    for categoria, (valor_mini, valor_max) in faixas.items():
        if valor_mini <= xp_aleatorio <= valor_max:
            print(f'o heroi {nome} com base no seu xp que é {xp_aleatorio} ele esta na categoria {categoria}')
            break
else:
    print(f'facilita meu codigo namoral é S ou N, esse {decisao} ta de brincadeira arruma isso ai')
