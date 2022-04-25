import random


def mensagem():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def tentativa():
    palavra_secretas = palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secretas]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secretas):
            index = 0
            for letra in palavra_secretas:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")
def jogar():
    mensagem()
    palavra_secreta()
    tentativa()


if(__name__ == "__main__"):
    jogar()