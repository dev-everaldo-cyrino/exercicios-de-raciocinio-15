arq = int(input('digite o tamanho do arquivo em megaBytes : '))
bits = arq * 0.125
tempo = bits / 1.2

print('''o tempo para ler um arquivo de {} megabytes
      usando a velocidade de 1.2 megabits é de {:.0f}s'''.format(arq,tempo)) 
 