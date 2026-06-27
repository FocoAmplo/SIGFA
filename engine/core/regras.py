"""
Regras do SIGFA
"""

def aplicar_regras(indicadores):

    resultado = []

    if indicadores["oee"] < 85:
        resultado.append("OEE abaixo da meta")

    if indicadores["retrabalho"] > 5:
        resultado.append("Retrabalho elevado")

    return resultado