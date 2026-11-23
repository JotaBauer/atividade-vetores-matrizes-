vetor=[]
maior=0

for i in range(5):
    p = int(input(f'Qual a quantidade de chamados no {i+1}° dia? \n'))

    if p > maior:
        maior = p

    if p >=0:
        vetor.append(p)
    else:
        print('Números negativos não são aceitos! ')

soma = sum(vetor)
print(f'O total de chamados na semana foi de {soma}')

media = soma/5

print(f'A média de chamados diários foi de {media}')

if maior == vetor[0]:
    print(f'O dia com mais chamados foi a segunda-feira com {vetor[0]} chamados')
elif maior == vetor[1]:
    print(f'O dia com mais chamdos foi aterça-feira com {vetor[1]} chamados')
elif maior == vetor[2]:
    print(f' dia com mais chamados foi a quarta-feira com {vetor[2]} chamados')
elif maior == vetor[3]:
    print(f'O dia com mais chamados foi a quinta-feira com {vetor[3]} chamados')
else:
    print(f'O dia com mais chamados foi a sexta-feira com {vetor[4]} chamados')


for i in range(5):
    if vetor[i] > media:
        print(f'O {i}° dia foi um dia com chamados acima da media')

print('     DIA     |   CHAMADOS   |')
print(f'SEGUNDA      |   {vetor[0]}     |')
print(f'TERÇA        |   {vetor[1]}     |')
print(f'QUARTA       |   {vetor[2]}     |')
print(f'QUINTA       |   {vetor[3]}     |')
print(f'SEXTA        |   {vetor[4]}     |')