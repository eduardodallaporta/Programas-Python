
# Calculo de IMC - Índice de Massa Corporal

    # MENOR QUE 18,5    MAGREZA
    # ENTRE 18,5 E 24,9 NORMAL
    # ENTRE 25,0 E 29,9 SOBREPESO
    # ENTRE 30,0 E 39,9 OBESIDADE
    # MAIOR QUE 40,0    OBESIDADE GRAVE

altura_cm = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

altura_m = altura_cm / 100

IMC = peso / (altura_m ** 2)
print(f'Seu (IMC) é: {IMC:.2f}')

if IMC < 18.5:
    print('MAGREZA!')
elif IMC >= 18.5 and IMC < 24.9:
    print('NORMAL!')
elif IMC >= 25 and IMC < 29.9:
    print('SOBREPESO!')
elif IMC >= 30 and IMC < 39.9:
    print('OBESIDADE!')
else:
    print('OBESIDADE GRAVE!!')
