#Exercicio usado no curso de Python da Alura

print("Bem vindo ao jogo de Adivinhação!!")

numero_secreto = 13

numero_tentativa_str = input("Quantas tentativas deseja ter?")
numero_tentativa = int(numero_tentativa_str)

contador = 1
acertou = False

for contador in range(1, numero_tentativa + 1):
    
    print("Tentativa {} de {}".format(contador, numero_tentativa))

    chute_str = input("Digite um número entre 1 e 20: ")
    print("Número digitado: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 20):
        print("Você digitiou um número fora do permitido e perdeu uma rodada!!")
        print("Por favor digite um núemro entre 1 e 20")
        continue

    if (numero_secreto == chute):
        print("Acertou miserávi!!")
        acertou = True
        break
    else:
        if(numero_secreto < chute):
            print("Você chutou alto!")
        else:
            print("Você chutou baixo!")

if(acertou):
    print("Você é fera!!!! Que tal jogar novamente?")
else:
    print("Não foi dessa vez, mas como dizia Raul: 'Tente outra vez!'")