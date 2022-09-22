print("Bem vindo ao jogo de Adivinhação!!")

numero_secreto = 13

chute_str = input("Digite um número: ")

print("Número digitado: ", chute_str)

chute = int(chute_str)

if(numero_secreto < chute):
    print("Você chutou alto!")
elif (numero_secreto > chute):
    print("Você chutou baixo!")
else:
    print("Acertou miserávi!!")