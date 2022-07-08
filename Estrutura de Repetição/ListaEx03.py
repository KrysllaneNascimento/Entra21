massa = float\
    (input('Digite a massa Inicial em (g):'))
segundos = 0
while massa > 0.5:
    massa /= 2
    segundos += 50
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60
print(f'No tempo pecorrido de {horas} horas {minutos} minutos e {segundos} segundos'
      f' a massa final será {massa:.2f}')
