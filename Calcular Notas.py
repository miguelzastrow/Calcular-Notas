notaA=float(input("Digite a sua Primeira Nota:  "))
notaB=float(input("Digite a sua Segunda Nota:  "))

#calacular nota:
mediafinal=(notaA + notaB) /2

#verificação:
if notaA >=7.0:
    print("A Média %.1f - Aprovado"%mediafinal)
else:
    print("A Média %.1f - Reprovado"%mediafinal)
    