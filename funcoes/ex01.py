def medidas(r1, r2, r3):
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        a = 'Os segmentos acima PODEM FORMAR UM TRIÂNGULO:'
        if r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1:
            b = 'ISOSCELES'
        elif r1 != r2 != r3:
            b = 'ESCALENO'
        else:
            b = 'EQUILÁTERO'
        return (f'{a}\n{b}')
    else:
        return print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')
