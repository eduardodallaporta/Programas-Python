
'''
Criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em portugues. 0 usuário deverá
fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

temp_steak = int(input('Qual é a temperatura da carne? '))

if temp_steak < 48:
    print('Cozinhar por mais tempo')
elif temp_steak < 54:
    print('Steak selado')
elif temp_steak < 60:
    print('Steak ao ponto para mal')
elif temp_steak < 65:
    print('Steak ao ponto')
elif temp_steak < 71:
    print('Steak ao ponto para bem')
elif temp_steak < 81:
    print('Steak bem passado')
else:
    print('Steak QUEIMADO')
