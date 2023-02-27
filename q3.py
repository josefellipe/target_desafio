import json

with open("dados.json", encoding='utf-8') as dados:
    faturamento_mes = json.load(dados)

def maior_faturamento(faturamento:list):
    #Ao invés de usar o sort eu poderia iterar a lista comparando o valor atual com o anterior e ficar com o maior
    faturamento.sort()
    return faturamento[-1]


def menor_faturamento(faturamento:list):
    faturamento.sort()
    return faturamento[0]


def dias_acima_media(faturamento:list):
    faturamento_sem_zero = []
    for dia in faturamento:
        if dia != 0:
            faturamento_sem_zero.append(dia)
    soma= 0
    for dia in faturamento_sem_zero:
        soma += dia
    media = soma/len(faturamento_sem_zero)
    qtd_acima_media = 0
    for dia in faturamento_sem_zero:
        if dia > media:
            qtd_acima_media += 1
    return qtd_acima_media

def pegar_valores(faturamentos:list):
    valores = []
    for faturamento in faturamentos:
        valores.append(faturamento.get("valor"))
    return valores



lista_valores = pegar_valores(faturamento_mes)
maior = maior_faturamento(lista_valores)
menor = menor_faturamento(lista_valores)
qtd_dia_acima_media = dias_acima_media(lista_valores)


print(f"""
Maior valor: {maior}
Menor valor: {menor}
Quantidade de dias acima da média: {qtd_dia_acima_media}
""")