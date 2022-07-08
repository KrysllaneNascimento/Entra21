from operator import itemgetter

times = {'Pameiras': 18,
         'Flamengo': 12,
         'Curitiba': 22}

print(times)
timesnovo = sorted(times.items(), key=itemgetter(1), reverse=True)

print(timesnovo)
print(timesnovo[1][1])
print(type(timesnovo))

for i, times in enumerate(timesnovo):
    print(f'{i + 1} - {times[0]} - {times[1]}')