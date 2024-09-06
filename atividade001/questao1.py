import random


def lancar_dado():
    return random.randint(1, 6)


def get_quantidade_lado(lado, array):
    contador = 0
    for i in range(len(array)):
        if array[i] == lado:
            contador += 1
    return contador


def main():
    array = []

    for i in range(100):
        resultado = lancar_dado()
        array.append(resultado)

    print(f'''
        1º FACE - {get_quantidade_lado(1, array)} vezes
        2º FACE - {get_quantidade_lado(2, array)} vezes
        3º FACE - {get_quantidade_lado(3, array)} vezes
        4º FACE - {get_quantidade_lado(4, array)} vezes
        5º FACE - {get_quantidade_lado(5, array)} vezes
        6º FACE - {get_quantidade_lado(6, array)} vezes
        ''')


if __name__ == '__main__':
    main()
