def get_digito_do_cpf(numeros_cpf: str, pesos: list):
    somaDigitos = 0
    for i in range(len(numeros_cpf)):
        somaDigitos += int(numeros_cpf[i]) * pesos[i]
    digito_gerado = somaDigitos % 11
    if digito_gerado < 10:
        return digito_gerado
    else:
        return 0


def validar_digito_validador_cpf(cpf: str):
    digito_validadores = cpf[12:]
    numeros_cpf = cpf.replace('.', '')
    numeros_cpf = numeros_cpf[0:9]
    primeiro_digito_validador = get_digito_do_cpf(numeros_cpf, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    numeros_cpf += str(primeiro_digito_validador)
    ultimo_digito_validador = get_digito_do_cpf(numeros_cpf, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    digito_validadores_gerado = str(primeiro_digito_validador) + str(ultimo_digito_validador)
    return digito_validadores_gerado == digito_validadores


def validar_formato_cpf(cpf):
    try:
        cpf_so_numeros = cpf.replace('.', '').replace("-","")
        if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-" and int(cpf_so_numeros):
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    cpf = input("Digite um cpf (No formato 111.111.111-11): ")
    if not validar_formato_cpf(cpf):
        print("ERROR: Digite no formato correto o CPF!")
        return
    if not validar_digito_validador_cpf(cpf):
        print("ERROR: Digite um CPF válido!")
        return
    print("CPF valido!")


if __name__ == "__main__":
    main()
