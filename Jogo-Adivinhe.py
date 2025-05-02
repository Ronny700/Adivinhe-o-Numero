import random

def jogar ():
    numero_secreto = random.randint(1,100) #Número aleatório entre 1e 100
    tentarivas = 0
    print("Bem-vindo ao jogo de Advinhação!")
    print("Tente adivinhar o número que estou pensando, entre 1 e 100.")

    while True:
        palpite = int(input("Qual é o seu palpite? "))
        tentarivas += 1

        if palpite < numero_secreto:
            print("O número é maior! Tente novamente.")

        elif palpite > numero_secreto:
            print("O número é menor! Tente novamente.")

        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentarivas} tentarivas.")
            break

def jogar_novamente():
    while True:
        jogar()
        resposta = input("\nQuer jogar novamente? (sim/não): ").strip().lower()
        if resposta != 'sim':
            print("Obrigado por jogat! Até logo!")
            break

#Começando o jogo
jogar_novamente()