
def is_palindromo(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace(' ', '')
    palindroma = ""

    for i in range(len(palavra), 0, -1):
        palindroma = palindroma + palavra[i-1]

    return palavra == palindroma


def main():
    palavra = input("Digite uma palavra: ")
    if is_palindromo(palavra):
        print("A palavra é palindroma!")
    else:
        print("A palavra não é palindroma!")


if __name__ == "__main__":
    main()
