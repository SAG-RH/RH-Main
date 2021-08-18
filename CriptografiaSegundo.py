import numpy as np


def converter_em_numeros(palavra):
    """receber como input a palavra que quer codificar e o retorno será uma conversão de letras em números"""
    palavra_verificada = []
    linha1 = []
    linha2 = []
    tabela_conversão = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
                        "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                        "v": 22, "w": 23, "x": 24, "y": 25, "z": 0}

    for cada_latra in palavra:
        if cada_latra != " ":
            palavra_verificada.append(tabela_conversão[cada_latra])

    if len(palavra_verificada) % 2 != 0:
        palavra_verificada.append(0)

    i = 0
    k = 0
    while i < len(palavra_verificada) / 2:
        j = 0
        while j < 2:
            if (j == 0):
                linha1.append(palavra_verificada[k])
            if (j == 1):
                linha2.append(palavra_verificada[k])
            j = j + 1
            k = k + 1
        i = i + 1

    return [linha1, linha2]

def multiplicar(escolhida, principal):
    """essa função deverá receber o resultado da função converter_em_numeros e uma matriz 2x2
        e o retorno será a multiplicação das matrizes"""
    resultado = np.dot(escolhida, principal)
    return resultado


def modulo(matriz_multiplicada):
    """como input vai receber o resultado da conta das matrizes e vai retornar uma matriz
        vai encontrar o modulo  de cada um dos números"""
    tamanho_colunas = len(matriz_multiplicada[0])
    matriz_resto_divisao = np.zeros((2, tamanho_colunas), dtype=np.float64)
    coluna = 0
    linha = 0
    for cada_linha in matriz_multiplicada:
        for numero in cada_linha:
            resto = numero % 26
            matriz_resto_divisao[linha][coluna] = resto
            coluna += 1
        linha += 1
        coluna = 0
    return matriz_resto_divisao


def converter_em_letras(matriz):
    """receber como input o retorno da função modulo e vai retornar a palavra criptografada"""

    tabela_conversão = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k",
                        12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u",
                        22: "v", 23: "w", 24: "x", 25: "y", 0: "z"}

    palavra = ""
    i = 0
    while i < len(matriz[0]):
        j = 0
        while j < 2:
            palavra = palavra + tabela_conversão[matriz[j][i]]
            j = j + 1
        i = i + 1

    return palavra

def principal(palavra):
    escolhida = np.array([[4, 3],
                          [1, 2]])
    palavra = str.lower(palavra)
    frase_convertida = converter_em_numeros(palavra)
    resultado = multiplicar(escolhida, frase_convertida)
    matriz_resto_divisao = modulo(resultado)
    convertido = converter_em_letras(matriz_resto_divisao)
    return convertido

