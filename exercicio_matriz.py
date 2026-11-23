matriz = []
somat=0

for i in range(3):
    linha = []
    for j in range(4):
        p = int(input('Digite quantidade de unidades vendidas: '))
        if p>=0:
            somat += p
            linha.append(p)
        else:
            print('Valores negativos não são permitidos')
    matriz.append(linha)

soma1 = sum(matriz[0])
print(f'Foram vendidas {soma1} camisetas')
soma2 = sum(matriz[1])
print(f'Foram vendidas {soma2} canecas')
soma3 = sum(matriz[2])
print(f'Foram vendidos {soma3} bonés\n')

soma4 = sum(linha[0] for linha in matriz)
print(f'A quinta de manhã teve {soma4} como soma total')
soma5 = sum(linha[1] for linha in matriz)
print(f'A quinta de tarde teve {soma5} como soma total')
soma6 = sum(linha[2] for linha in matriz)
print(f'A sexta de manhã teve {soma6} como soma total')
soma7 = sum(linha[3] for linha in matriz)
print(f'A sexta de tarde teve {soma7} como soma total\n')

print(f'A soma total foi de {somat}\n')

maior=0
if soma1> maior:
    maior = soma1
elif soma2> maior:
    maior = soma2
elif soma3> maior:
    maior = soma3


if soma1 == maior:
    print('As camisetas foram o produto mais vendido')
elif soma2 == maior:
    print('As canecas foram o produto mais vendido')
elif soma3 == maior:
    print('Os bonés foram o produto mais vendido')


periodos =[soma4, soma5, soma6, soma7]
mai = max(periodos)
if mai == soma4:
    print('A quinta de manhã teve mais vendas')
elif mai == soma5:
    print('A quinta de tarde teve mais vendas')
elif mai == soma6:
    print('A sexta de manhã teve mais vendas')
elif mai == soma7:
    print('A sexta de tarde teve mais vendas')

print('\n')
print(f'    PRODUTO     |   Qui.Manhã   |   Qui.Tarde   |   Sex.Manhã   |   Sex.Tarde   ')
print(f'    CAMISETAS   |       {matriz[0][0]}       |       {matriz[0][1]}       |       {matriz[0][2]}       |       {matriz[0][3]}      ')
print(f'    CANECAS     |       {matriz[1][0]}       |       {matriz[1][1]}       |       {matriz[1][2]}       |      {matriz[1][3]}  ')
print(f'    BONÉS       |       {matriz[2][0]}       |       {matriz[2][1]}       |       {matriz[2][2]}       |      {matriz[2][3]}  ')