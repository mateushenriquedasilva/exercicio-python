# Número de dias
# Número de horas
# Número de minutos
# Número de segundos

sec_ = float(input())

segundos = 0
minutos = 0
horas = 0
dias = 0

if sec_ < 60:
    segundos = sec_ / 60
if sec_ >= 60 and sec_ < 3600:
    minutos = sec_ / 60
if sec_ >= 3600 and sec_ < 86400:
    horas = sec_ / 3600
if sec_ >= 86400:
    dias = sec_ / 86400 

print(f'{dias:.0f}')
print(f'{horas:.0f}')
print(f'{minutos:.0f}')
print(f'{segundos:.0f}')