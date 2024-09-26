#Função SOBREJETORA
def funcao_sobrejetora(x):
    return x + 1

conjunto_A = [1, 2, 3, 4]
conjunto_B = list(map(funcao_sobrejetora, conjunto_A))
print(f"Conjunto de partida A: {conjunto_A}")
print(f"Conjunto de chegada B: {conjunto_B}")

#Função INJETORA
def funcao_injetora(x):
    return 2 * x

conjunto_A = [1, 2, 3, 4]
conjunto_B = list(map(funcao_injetora, conjunto_A)) 
print(f"Conjunto de partida A: {conjunto_A}")
print(f"Conjunto de chegada B: {conjunto_B}")

#Função COMPOSTA
def funcao_f(x):
    return x + 1

def funcao_g(x):
    return 2 * x

def funcao_composta(x):
    return funcao_f(funcao_g(x))

x = 3
resultado = funcao_composta(x)
print(f"Resultado de f(g({x})) = {resultado}")
