const SpecialistCard = () => {

    const items = [

        {
            label: "Motor IA",
            value: "Online"
        },

        {
            label: "Modelo de Análise",
            value: "SIGFA Intelligence"
        },

        {
            label: "Última Execução",
            value: "Nenhuma análise realizada"
        },

        {
            label: "Alertas",
            value: "Nenhum alerta ativo"
        },

        {
            label: "Próxima Ação",
            value: "Aguardar envio de dados"
        }

    ];

    return `

        <section class="specialist-card">

            <span class="section-label">

                CONSULTOR INTELIGENTE

            </span>

            <h2>

                Motor Inteligente SIGFA

            </h2>

            <p class="specialist-description">

                O Consultor Inteligente monitora continuamente os dados recebidos da empresa, identifica riscos, oportunidades e gera recomendações estratégicas fundamentadas em informações reais.

            </p>

            <div class="specialist-list">

                ${items.map(item => `

                    <div class="specialist-item">

                        <span>

                            ${item.label}

                        </span>

                        <strong>

                            ${item.value}

                        </strong>

                    </div>

                `).join("")}

            </div>

            <button class="specialist-button">

                Abrir Consultor Inteligente

            </button>

        </section>

    `;

};

export default SpecialistCard;