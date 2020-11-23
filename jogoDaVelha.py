

def play():

    jogo = True
    rodada = 1
    vez_jogador = True #True = jogador 1, False = jogador 2
    posicoesInt = [1, 2, 3, 4, 5, 6, 7, 8, 9] #não é mostrado para os jogadores, usado para marcar posição no posicoesString
    posicoesString = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #campo de jogo que é mostrado para os jogadores

    while(jogo):

        mostrar_campo(posicoesString)

        if(rodada > 9):
            print("FIM DE JOGO")
            print("DEU VELHA")
            print("NINGUEM GANHOU")
            break

        if(vez_jogador):
            while(vez_jogador == True):

                print("JOGADOR: 1")
                posicao = int(input("Digite um número pra marcar a posição: "))

                posicaoValida = verificar_posicao_valida(posicao, posicoesInt)

                if(posicaoValida == -1):
                    print("Valor inválido")
                elif (posicaoValida == -2):
                    print("Essa posição já foi marcada")
                else:
                    posicoesInt[posicaoValida] = 0
                    posicoesString[posicaoValida] = "x"
                    vez_jogador = False

        else:
            while (vez_jogador == False):

                print("JOGADOR: 2")
                posicao = int(input("Digite um número pra marcar a posição: "))

                posicaoValida = verificar_posicao_valida(posicao, posicoesInt)

                if (posicaoValida == -1):
                    print("Valor inválido")
                elif(posicaoValida == -2):
                    print("Essa posição já foi marcada")
                else:
                    posicoesInt[posicaoValida] = 0
                    posicoesString[posicaoValida] = "o"
                    vez_jogador = True

        if(vez_jogador == False): #se "vez_jogador" for Falso, quer dizer que a ultima jogada foi do jogador 1
            vitoria = verificar_condicao_vitoria1(posicoesString) #Verifica se jogador 1 ganhou
            if(vitoria):
                mostrar_campo(posicoesString)
                print("FIM DE JOGO")
                print("JOGADOR 1 VENCEU")
                break

        if (vez_jogador == True):  # se "vez_jogador" for Verdadeiro, quer dizer que a ultima jogada foi do jogador 2
            vitoria = verificar_condicao_vitoria2(posicoesString) #Verifica se jogador 2 ganhou
            if (vitoria):
                mostrar_campo(posicoesString)
                print("FIM DE JOGO")
                print("JOGADOR 2 VENCEU")
                break

        rodada = rodada + 1

def mostrar_campo(posicoesString):
    print("       |       |       ")
    print("   {}   |   {}   |   {}   ".format(posicoesString[0], posicoesString[1], posicoesString[2]))
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print("   {}   |   {}   |   {}   ".format(posicoesString[3], posicoesString[4], posicoesString[5]))
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print("   {}   |   {}   |   {}   ".format(posicoesString[6], posicoesString[7], posicoesString[8]))
    print("       |       |       ")

def verificar_posicao_valida(posicao, posicoesInt):
    if (posicao < 1 or posicao > 9):
        return -1
    else:
        for i in range(0, 9):
            if (posicao == posicoesInt[i]):
                return i
            elif(i == 8):
                return -2

def verificar_condicao_vitoria1(posicoesString): #Verifica se jogador 1 ganhou
    for i in range(0, 7, 3):
        if (posicoesString[i] == "x" and posicoesString[i + 1] == "x" and posicoesString[i + 2] == "x"):
            return True

    for i in range(0, 3):
        if (posicoesString[i] == "x" and posicoesString[i + 3] == "x" and posicoesString[i + 6] == "x"):
            return True

    if (posicoesString[0] == "x" and posicoesString[4] == "x" and posicoesString[8] == "x"):
        return True
    elif (posicoesString[2] == "x" and posicoesString[4] == "x" and posicoesString[6] == "x"):
        return True

def verificar_condicao_vitoria2(posicoesString): #Verifica se jogador 2 ganhou
    for i in range(0, 7, 3):
        if (posicoesString[i] == "o" and posicoesString[i + 1] == "o" and posicoesString[i + 2] == "o"):
            return True

    for i in range(0, 3):
        if (posicoesString[i] == "o" and posicoesString[i + 3] == "o" and posicoesString[i + 6] == "o"):
            return True

    if (posicoesString[0] == "o" and posicoesString[4] == "o" and posicoesString[8] == "o"):
        return True
    elif (posicoesString[2] == "o" and posicoesString[4] == "o" and posicoesString[6] == "o"):
        return True

if (__name__ == "__main__"):
        play()