import intelligenceStore from '../../store/intelligence.store.js';

const DEFAULT_INDICATORS = [

    {
        title: "Receita",
        status: "Aguardando dados"
    },

    {
        title: "Lucro",
        status: "Aguardando dados"
    },

    {
        title: "Fluxo de Caixa",
        status: "Aguardando dados"
    },

    {
        title: "Financeiro",
        status: "Nenhum documento"
    },

    {
        title: "Comercial",
        status: "Sem análise"
    },

    {
        title: "Produção",
        status: "Sem indicadores"
    },

    {
        title: "Qualidade",
        status: "Sem análise"
    },

    {
        title: "OEE",
        status: "Não calculado"
    }

];

const KPIOverview = () => {

    const state = intelligenceStore.getState();

    const backendIndicators = state.indicators || [];

    const indicators = DEFAULT_INDICATORS.map(item => {

        const backendItem = backendIndicators.find(indicator =>
            indicator.name?.toLowerCase() === item.title.toLowerCase()
        );

        return {

            title: item.title,

            status: backendItem
                ? `${backendItem.value}${backendItem.trend ? ` • ${backendItem.trend}` : ''}`
                : item.status

        };

    });

    return `

        <section class="kpi-overview">

            <div class="kpi-header">

                <div>

                    <span class="section-label">

                        DASHBOARD EXECUTIVO

                    </span>

                    <h2>

                        Indicadores Estratégicos

                    </h2>

                </div>

            </div>

            <div class="kpi-grid">

                ${indicators.map(indicator => `

                    <article class="kpi-card">

                        <span class="kpi-title">

                            ${indicator.title}

                        </span>

                        <strong class="kpi-value">

                            ${indicator.status}

                        </strong>

                    </article>

                `).join("")}

            </div>

        </section>

    `;

};

export default KPIOverview;