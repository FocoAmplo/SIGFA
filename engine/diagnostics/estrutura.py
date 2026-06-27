from dados import ler_planilha


def analisar_estrutura():

    dados = ler_planilha()

    print("\n========== ESTRUTURA SIGFA ==========\n")

    for aba, tabela in dados.items():

        print(f"ABA: {aba}")

        print(f"Colunas : {len(tabela.columns)}")

        print(f"Registros : {len(tabela)}")

        print("Campos:")

        for coluna in tabela.columns:
            print(f"   - {coluna}")

        print("-" * 40)


if __name__ == "__main__":
    analisar_estrutura()