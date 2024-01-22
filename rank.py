def rank():
    while True:
        try:
            v = int(input('quantas vitorias voce tem? '))
            d = int(input('quantas derrotas vc tem? '))
            resultado = v - d
            return resultado
        except ValueError:
            print('digite um numero')

resultado_final = rank()

faixas = {
    'Ferro':(float('-inf'),10),
    'Bronze':(11, 20),
    'Prata':(21, 50),
    'Ouro':(51, 80),
    'Diamante':(81, 90),
    'Lendário':(91, 100),
    'Imortal':(101, float('inf'))
}

for categoria, (valor_mini, valor_max) in faixas.items():
    if valor_mini <= resultado_final <= valor_max:
        print(f'o heroi tem um saldo de vitorias de {resultado_final} e esta no nivel {categoria}')
        break


