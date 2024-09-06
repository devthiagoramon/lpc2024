def get_numero_maiores_que_20(valor: int):
    dezena = valor // 10
    unidade = valor % 10

    match dezena:
        case 2:
            return "Vinte e " + str(get_numero_menores_que_20(unidade))
        case 3:
            return "Trinta e " + str(get_numero_menores_que_20(unidade))
        case 4:
            return "Quarenta e " + str(get_numero_menores_que_20(unidade))
        case 5:
            return "Cinquenta e " + str(get_numero_menores_que_20(unidade))
        case 6:
            return "Sessenta e " + str(get_numero_menores_que_20(unidade))
        case 7:
            return "Setenta e " + str(get_numero_menores_que_20(unidade))
        case 8:
            return "Oitenta e " + str(get_numero_menores_que_20(unidade))
        case 9:
            return "Noventa e " + str(get_numero_menores_que_20(unidade))


def get_numero_menores_que_20(valor: int):
    match valor:
        case 1:
            return "um"
        case 2:
            return "dois"
        case 3:
            return "três"
        case 4:
            return "quatro"
        case 5:
            return "cinco"
        case 6:
            return "seis"
        case 7:
            return "sete"
        case 8:
            return "oito"
        case 9:
            return "nove"
        case 10:
            return "dez"
        case 11:
            return "onze"
        case 12:
            return "doze"
        case 13:
            return "treze"
        case 14:
            return "quatorze"
        case 15:
            return "quinze"
        case 16:
            return "dezesseis"
        case 17:
            return "dezessete"
        case 18:
            return "dezoito"
        case 19:
            return "dezenove"
        case 20:
            return "vinte"


def main():
    valor = int(input("Digite um valor para ser transformado para extenso entre 1 e 99: "))
    if 1 <= valor <= 20:
        print(get_numero_menores_que_20(valor))
    elif 20 <= valor <= 99:
        print(get_numero_maiores_que_20(valor))
    else:
        print("Número inválido!")


if __name__ == "__main__":
    main()
