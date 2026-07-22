import intelligenceStore from '../../store/intelligence.store.js';

const SIGFALiveFeed = () => {

    const state = intelligenceStore.getState();

    const loading = state.loading;

    const diagnosis = state.diagnosis;

    const alerts = state.alerts || [];

    const recommendations = state.recommendations || [];

    const events = [];

    if (loading) {

        events.push({
            title: "Centro de Inteligência",
            description: "Processando informações recebidas..."
        });

    }

    if (diagnosis) {

        events.push({
            title: "Diagnóstico concluído",
            description: diagnosis.summary || "Diagnóstico estratégico disponível."
        });

    }

    alerts.forEach(alert => {

        events.push({
            title: "Alerta",
            description: `${alert.title} • ${alert.severity}`
        });

    });

    recommendations.slice(0, 3).forEach(item => {

        events.push({
            title: "Recomendação",
            description: item
        });

    });

    if (events.length === 0) {

        events.push({

            title: "Sistema iniciado",

            description: "Aguardando documentos, indicadores ou solicitações para iniciar a análise."

        });

    }

    return `

        <section class="sigfa-live-feed">

            <div class="feed-header">

                <span class="section-label">

                    ATIVIDADE DO CENTRO DE INTELIGÊNCIA

                </span>

                <h2>

                    Eventos em Tempo Real

                </h2>

            </div>

            <div class="feed-list">

                ${events.map(event => `

                    <article class="feed-item">

                        <div class="feed-marker"></div>

                        <div class="feed-content">

                            <strong>

                                ${event.title}

                            </strong>

                            <p>

                                ${event.description}

                            </p>

                        </div>

                    </article>

                `).join("")}

            </div>

        </section>

    `;

};

export default SIGFALiveFeed;