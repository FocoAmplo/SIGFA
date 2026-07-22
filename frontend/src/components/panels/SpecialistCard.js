import intelligenceStore from '../../store/intelligence.store.js';

const SpecialistCard = () => {

    const state = intelligenceStore.getState();

    const indicators = [

        {
            label: "Saúde Geral",
            value: state.dashboard?.health || 0
        },

        {
            label: "Financeiro",
            value: state.dashboard?.finance || 0
        },

        {
            label: "Comercial",
            value: state.dashboard?.commercial || 0
        },

        {
            label: "Produção",
            value: state.dashboard?.production || 0
        },

        {
            label: "Qualidade",
            value: state.dashboard?.quality || 0
        }

    ];

    return `

        <section class="specialist-card">

            <span class="section-label">

                PAINEL EXECUTIVO

            </span>

            <h2>

                Indicadores da Empresa

            </h2>

            <div class="indicator-list">

                ${indicators.map(item => `

                    <div class="indicator-row">

                        <div class="indicator-header">

                            <span>

                                ${item.label}

                            </span>

                            <strong>

                                ${item.value}%

                            </strong>

                        </div>

                        <div class="indicator-bar">

                            <div
                                class="indicator-fill"
                                style="width:${item.value}%">
                            </div>

                        </div>

                    </div>

                `).join("")}

            </div>

        </section>

    `;

};

export default SpecialistCard;