idades = [30, 39, 27, 18]

idades_ano_que_vem = [(idade + 1) for idade in idades if idade > 21]

type(idades)


def faz_processamento(lista):
    print(len(lista))


faz_processamento(idades)