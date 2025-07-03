def q1(cidades):
    def cidades_maiores_que_100(idades):
        return [cidade for cidade, idade in idades.items() if idade > 100]

    resultado = cidades_maiores_que_100(cidades)
    return resultado


def q2(lista1, lista2):
    def processar_listas(lista1, lista2):
        maiores_que_zero = [num for num in lista1 + lista2 if num > 0]
        soma = sum(maiores_que_zero)
        ordenada = sorted(maiores_que_zero)
        return (soma, ordenada)

    resultado = processar_listas(lista1, lista2)
    return resultado


def q3():
    def ler_valores():
        valores = []
        while True:
            numero = int(input("Digite um número (0 para sair): "))
            if numero == 0:
                break
            valores.append(numero)
        return valores

    def processa_lista(lista):
        pares = [num for num in lista if num % 2 == 0]
        impares = [num for num in lista if num % 2 != 0]
        return pares, impares

    valores = ler_valores()
    pares, impares = processa_lista(valores)
    print("Lista de Pares:", pares)
    print("Lista de Ímpares:", impares)


def q4():
    def ler_03_alturas():
        alturas = []
        for _ in range(3):
            altura = float(input("Digite a altura: "))
            alturas.append(altura)
        return alturas

    def organizar_alturas(lista):
        ordenadas = sorted(lista)
        return [ordenadas[1], ordenadas[2], ordenadas[0]]

    def formatar_alturas(lista):
        return [f"{altura:.2f}" for altura in lista]

    alturas = ler_03_alturas()
    alturas_organizadas = organizar_alturas(alturas)
    alturas_formatadas = formatar_alturas(alturas_organizadas)

    for altura in alturas_formatadas:
        print(altura)


def main():
    # Teste q1
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)

    # Teste q2
    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)

    # Teste q3()
    q3()
    # Test q4()
    q4()


if __name__ == "__main__":
    main()
