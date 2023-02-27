faturamento_por_estado = [
    {
    "estado": "SP",
    "valor": 67836.43
    },
    {
    "estado": "RJ",
    "valor": 36678.66
    },
    {
    "estado": "MG",
    "valor": 29229.88
    },
    {
    "estado": "ES",
    "valor": 27165.48
    },
    {
    "estado": "Outros",
    "valor": 19849.53
    }
]

def calcular_percentual_representacao(faturamento:list):
    print(f"\nO percentual de representação de cada estado é:\n")
    soma = 0
    for estado in faturamento:
        soma += estado["valor"]
    for estado in faturamento:
        percentual = estado["valor"]/soma*100
        sigla = estado["estado"]
        print(f"{sigla}: {percentual:.2f}%")

calcular_percentual_representacao(faturamento_por_estado)