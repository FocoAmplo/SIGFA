const ChatWorkspace = () => {

    return `

<section class="chat-workspace">

    <div class="chat-header">

        <div>

            <span class="workspace-badge">

                CONSULTOR INTELIGENTE SIGFA

            </span>

            <h2 class="workspace-title">

                Centro de Operações Inteligente

            </h2>

            <p class="workspace-description">

                Converse naturalmente com o SIGFA.
                Faça perguntas, solicite diagnósticos,
                peça relatórios executivos ou monte planos
                de ação para sua empresa.

            </p>

        </div>

        <div class="workspace-status">

            <span class="status-indicator"></span>

            Online

        </div>

    </div>

    <div class="chat-body">

        <div class="assistant-message">

            <div class="assistant-avatar">

                IA

            </div>

            <div class="assistant-content">

                <h3>

                    Bem-vindo ao Centro de Inteligência.

                </h3>

                <p>

                    Ainda não existem dados empresariais
                    suficientes para gerar indicadores.

                </p>

                <p>

                    Para iniciar uma análise você pode:

                </p>

                <ul>

                    <li>Enviar um PDF.</li>

                    <li>Enviar uma planilha Excel.</li>

                    <li>Importar arquivos CSV.</li>

                    <li>Conversar com o Consultor Inteligente.</li>

                    <li>Solicitar um diagnóstico estratégico.</li>

                </ul>

            </div>

        </div>

        <div class="analysis-state">

            <div class="state-item active">

                Recebendo Solicitação

            </div>

            <div class="state-arrow">

                →

            </div>

            <div class="state-item">

                Processando

            </div>

            <div class="state-arrow">

                →

            </div>

            <div class="state-item">

                Especialistas

            </div>

            <div class="state-arrow">

                →

            </div>

            <div class="state-item">

                Super Gerente

            </div>

            <div class="state-arrow">

                →

            </div>

            <div class="state-item">

                Resultado

            </div>

        </div>

    </div>

    <div class="chat-input-area">

        <textarea

            class="chat-input"

            placeholder="Digite sua pergunta ou solicitação estratégica..."

        ></textarea>

        <div class="chat-actions">

            <div class="chat-tools">

                <button class="tool-btn">

                    📎 Documento

                </button>

                <button class="tool-btn">

                    🎤 Áudio

                </button>

                <button class="tool-btn">

                    📷 Imagem

                </button>
                                <button class="tool-btn">

                    📊 Excel

                </button>

                <button class="tool-btn">

                    📄 PDF

                </button>

            </div>

            <button class="chat-send">

                Enviar para Análise

            </button>

        </div>

    </div>

    <div class="workspace-quick-actions">

        <h3>

            Ações Inteligentes

        </h3>

        <div class="quick-actions-grid">

            <button class="quick-card">

                <strong>

                    Diagnóstico Empresarial

                </strong>

                <span>

                    Analisa a situação geral da empresa.

                </span>

            </button>

            <button class="quick-card">

                <strong>

                    Fluxo de Caixa

                </strong>

                <span>

                    Avaliar liquidez e movimentações financeiras.

                </span>

            </button>

            <button class="quick-card">

                <strong>

                    Produção

                </strong>

                <span>

                    Identificar gargalos e oportunidades.

                </span>

            </button>

            <button class="quick-card">

                <strong>

                    Comercial

                </strong>

                <span>

                    Avaliar vendas e desempenho da equipe.

                </span>

            </button>

            <button class="quick-card">

                <strong>

                    Plano de Ação

                </strong>

                <span>

                    Elaborar um plano estratégico baseado nos dados.

                </span>

            </button>

            <button class="quick-card">

                <strong>

                    Consultar Especialistas

                </strong>

                <span>

                    Encaminhar a análise aos especialistas SIGFA.

                </span>

            </button>

        </div>

    </div>

    <div class="workspace-warning">

        <strong>

            Transparência da IA

        </strong>

        <p>

            O SIGFA somente gera indicadores empresariais após
            receber informações reais da empresa.

            Antes disso, o Centro de Inteligência apresenta
            metodologias, orientações e explica como iniciar
            uma análise estratégica.

        </p>

    </div>
    </section>

    `;

};

export default ChatWorkspace;