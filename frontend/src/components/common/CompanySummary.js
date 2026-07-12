const CompanySummary = () => {

    const information = [

        {
            label: "Empresa",
            value: "Nenhuma empresa conectada"
        },

        {
            label: "Plano",
            value: "Experiência SIGFA"
        },

        {
            label: "Integração",
            value: "Aguardando conexão"
        },

        {
            label: "Base de Dados",
            value: "Nenhum registro recebido"
        },

        {
            label: "Documentos",
            value: "0 arquivos processados"
        },

        {
            label: "Última Atualização",
            value: "Ainda não sincronizado"
        }

    ];

    return `

        <section class="summary-card">

            <span class="section-label">

                EMPRESA

            </span>

            <h2>

                Resumo Operacional

            </h2>

            <p class="summary-description">

                O SIGFA exibirá automaticamente as informações da empresa
                após a conexão com a plataforma ou envio dos primeiros
                documentos para análise.

            </p>

            <div class="summary-status-list">

                ${information.map(item => `

                    <div class="summary-status">

                        <span>

                            ${item.label}

                        </span>

                        <strong>

                            ${item.value}

                        </strong>

                    </div>

                `).join("")}

            </div>

        </section>

    `;

};

export default CompanySummary;