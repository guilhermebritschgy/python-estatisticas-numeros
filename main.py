def ler_numeros():
    lista_num = []
    while True:
        try:
            num = int(input("Digite um número (0 para parar): \n"))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue
        if num == 0:
            break
        lista_num.append(num)
    return lista_num


def calcular_estatisticas(lista_num):
    pares = []
    for numeros in lista_num:
        if numeros % 2 == 0:
            pares.append(numeros)

    if len(lista_num) == 0:
        return {
            "media": 0,
            "max_num": 0,
            "min_num": 0,
            "mensagem": "Nenhum número foi digitado. Tente novamente."
        }
    return {
        "media": sum(lista_num)/len(lista_num),
        "max_num": max(lista_num),
        "min_num": min(lista_num),
        "pares": pares,
        "contagem": len(lista_num)
    }


def exibir_resultados(estatisticas):
    if "mensagem" in estatisticas:
        print(estatisticas["mensagem"])
        return  # Se houver uma mensagem de erro, não continuar exibindo outras estatísticas

    print(f"Menor número digitado: {estatisticas['min_num']}")
    print(f"Média: {estatisticas['media']}")
    print(f"Contagem de números digitados: {estatisticas['contagem']}")
    print(
        f"lista com os números pares: {estatisticas['pares']}, Contagem: {len(estatisticas['pares'])}.")


def main():
    numeros = ler_numeros()
    estatisticas = calcular_estatisticas(numeros)
    exibir_resultados(estatisticas)


main()
