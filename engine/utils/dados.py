import pandas as pd
from pathlib import Path


def ler_planilha():

    caminho = Path(__file__).parent.parent / "SIGFA.xlsx"

    planilha = {}

    xls = pd.ExcelFile(caminho)

    for aba in xls.sheet_names:

        planilha[aba] = pd.read_excel(caminho, sheet_name=aba)

    return planilha


if __name__ == "__main__":

    dados = ler_planilha()

    for aba, tabela in dados.items():

        print(f"\n===== {aba} =====")

        print(tabela.head())