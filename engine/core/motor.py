"""
SIGFA Engine 0.1
Motor Principal
"""

from regras import aplicar_regras
from indicadores import calcular_indicadores
from diagnostico import gerar_diagnostico


def executar(dados_empresa):

    indicadores = calcular_indicadores(dados_empresa)

    regras = aplicar_regras(indicadores)

    diagnostico = gerar_diagnostico(indicadores, regras)

    return diagnostico