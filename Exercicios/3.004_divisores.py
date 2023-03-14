inNum = int(input("Introduza um numero para calcular os seus divisores: "))

listRange = list(range(1,inNum+1))

for numero in listRange:
    if inNum % numero == 0:
        print(int (numero))
