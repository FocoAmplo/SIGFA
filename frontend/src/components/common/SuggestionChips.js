const SuggestionChips = () => {

    const suggestions = [

        "Fluxo de Caixa",

        "Financeiro",

        "Produção",

        "Comercial",

        "Estoque",

        "Custos",

        "RH",

        "Indicadores"

    ];

    return `

        <section class="quick-actions">

            <h3>Sugestões Inteligentes</h3>

            <div class="quick-actions-grid">

                ${suggestions.map(item => `

                    <button class="quick-action">

                        ${item}

                    </button>

                `).join('')}

            </div>

        </section>

    `;

};

export default SuggestionChips;