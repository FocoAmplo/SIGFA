const AIHero = () => {
    return `
        <section class="ai-hero">

            <div class="ai-hero-header">

                <span class="ai-hero-badge">
                    CENTRO DE INTELIGÊNCIA SIGFA
                </span>

                <h1 class="ai-hero-title">
                    👋 Boa noite, Silvanio
                </h1>

                <p class="ai-hero-description">
                    Como posso ajudar sua empresa hoje?
                </p>

            </div>

            <div class="ai-prompt">

                <textarea
                    placeholder="Ex.: Analise meu fluxo de caixa dos últimos 90 dias..."
                ></textarea>

                <div class="ai-toolbar">

                    <div class="ai-toolbar-left">

                        <button>📄 PDF</button>

                        <button>📊 Excel</button>

                        <button>🖼 Imagem</button>

                        <button>🎤 Voz</button>

                    </div>

                    <button class="ai-send">

                        Perguntar ao SIGFA →

                    </button>

                </div>

            </div>

        </section>
    `;
};

export default AIHero;