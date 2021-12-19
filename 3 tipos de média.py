notas1 = float(input())
notas2 = float(input())
notas3 = float(input())

media = (notas1 + notas2 + notas3) / 3;
media_ponderada = ((notas1 * 2) + (notas2 * 2) + (notas3 * 3)) / (2+2+3);
media_ponderada_2 = ((notas1 * 1) + (notas2 * 2) + (notas3 * 2)) / (1+2+2);
print(f'{media:.2f}')
print(f'{media_ponderada:.2f}')
print(f'{media_ponderada_2:.2f}')