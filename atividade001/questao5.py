import random

palavra_forca = ""


def get_palavra_aleatoria():
    global palavra_forca
    with open("br-sem-acentos.txt", "r") as f:
        linhas = f.readlines()
        palavra_aleatoria_index = random.randint(0, len(linhas) - 1)
        palavra_aleatoria = linhas[palavra_aleatoria_index]
        palavra_forca = palavra_aleatoria.lower()


def get_desenho_palavra(letras_acertadas):
    global palavra_forca
    desenho_palavra = palavra_forca
    for letra_desenho_palavra in desenho_palavra:
        if letra_desenho_palavra not in letras_acertadas:
            desenho_palavra = desenho_palavra.replace(letra_desenho_palavra, "_")
    return desenho_palavra.upper()


def iniciar_jogo():
    global palavra_forca
    letras_acertadas = []
    tentativas = 1
    max_tentativas = 6

    while tentativas <= max_tentativas:
        print()
        letra = input("Digite uma letra: ")
        if len(letra) != 1:
            print("Digite somente uma letra!")
            continue
        letra = letra.lower()

        if letra in palavra_forca:
            letras_acertadas.append(letra)
            desenho_palavra = get_desenho_palavra(letras_acertadas)
            print(desenho_palavra)
            if desenho_palavra.lower() == palavra_forca:
                print("Você acertou!!!! Parábens!")
                break
        else:
            if tentativas == max_tentativas:
                print("Jogo finalizado, você desperdiçou todas as suas tentativas, tente novamente!")
            print(f"Você errou pela {tentativas}º tentativa! Tente novamente!")
            tentativas += 1


def main():
    get_palavra_aleatoria()
    iniciar_jogo()


if __name__ == "__main__":
    main()
