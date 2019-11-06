input = int(input('Insira os dias:'))

anos = input / 365

input %= 365

meses = input / 30

input %= 30

dias = input

print (str(dias) + " dias, " + str(meses) + " meses e " + str(anos) + " anos.")