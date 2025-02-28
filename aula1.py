import random 
numero_max = 10
limite_tentativas= 3

sorteio = random.randint(1, numero_max)

#chute = input("digite o seu chute:")
#print(sorteio)
print ("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando,de 1 a 10")
chute=int (input("chute"))
tentativas = 1
while (limite_tentativas >= tentativas ):
    print("tentativa:",tentativas)
    chute= int(input("digite o seu chute"))
    if (chute==sorteio):
        print("Parabens,voce acertou")
    #tentativas = tentativas +1
    #print (sorteio)
    #print(chute)
    if (chute==sorteio):
       print("Parabens,voce acertou qual numero era",)
       break
    elif (chute > sorteio):
        print("chute um numero menor")
    elif(chute>sorteio):
        print("chute um numero maior")
        tentativas=tentativas + 1
