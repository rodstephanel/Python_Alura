#Exercicio usado no curso de Python da Alura

print("Bem vindo ao jogo de Adivinhação!!")

numero_secreto = 13

numero_tentativa_str = input("Quantas tentativas deseja ter?")
numero_tentativa = int(numero_tentativa_str)

contador = 1
acertou = False

while(contador <= numero_tentativa):
    
    print("Tentativa {} de {}".format(contador, numero_tentativa))

    chute_str = input("Digite um número: ")
    print("Número digitado: ", chute_str)
    chute = int(chute_str)

    if (numero_secreto == chute):
        print("Acertou miserávi!!")
        contador = numero_tentativa + 1
        acertou = True
    else:
        if(numero_secreto < chute):
            print("Você chutou alto!")
        else:
            print("Você chutou baixo!")

        contador = contador + 1

if(acertou):
    print("Você é fera!!!! Que tal jogar novamente?")
else:
    print("Não foi dessa vez, mas como dizia Raul: 'Tente outra vez!'")