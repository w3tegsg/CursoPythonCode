frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
count = 0
for caracter in frase:
    if caracter == 'r':
        count += 1
print("O caracter R apareceu %s vezes na frase" %(count))