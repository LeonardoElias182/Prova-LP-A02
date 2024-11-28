velocidade_maxima = 80

velocidade = int(input('Qual é a velocidade do seu carro? '))

excesso = velocidade - velocidade_maxima

multa = excesso * 20

if velocidade > velocidade_maxima:
    print (f'Você ultrapassou a velocidade máxima permitida em {excesso} km/h. ')
    print (f'Você será multado em R$ {multa} reais')

else:
    print ('VoCê está dentro do limite de velocidade permitido.')

