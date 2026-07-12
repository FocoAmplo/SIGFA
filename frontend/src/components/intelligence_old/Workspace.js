const Workspace = () => {

    return `

<section class="intelligence-workspace">

    <div class="workspace-top">

        <div>

            <span class="workspace-badge">

                WORKSPACE INTELIGENTE

            </span>

            <h2>

                Centro de Operações Empresariais

            </h2>

            <p>

                Todas as análises, diagnósticos, indicadores,
                recomendações e planos de ação serão apresentados
                neste ambiente.

            </p>

        </div>

        <div class="workspace-mode">

            <span class="mode-online">

                ● Online

            </span>

        </div>

    </div>

    <div class="workspace-navigation">

        <button class="workspace-tab active">

            Dashboard

        </button>

        <button class="workspace-tab">

            Financeiro

        </button>

        <button class="workspace-tab">

            Comercial

        </button>

        <button class="workspace-tab">

            Produção

        </button>

        <button class="workspace-tab">

            Qualidade

        </button>

        <button class="workspace-tab">

            RH

        </button>

        <button class="workspace-tab">

            Logística

        </button>

        <button class="workspace-tab">

            Diagnóstico

        </button>

        <button class="workspace-tab">

            Plano de Ação

        </button>

        <button class="workspace-tab">

            Relatórios

        </button>

    </div>

    <div class="workspace-screen">

        <div class="workspace-empty">

            <div class="workspace-icon">

                🧠

            </div>

            <h2>

                Centro de Inteligência pronto.

            </h2>

            <p>

                Nenhum módulo foi aberto.

                Utilize o menu superior ou converse com a IA
                para iniciar uma análise.

            </p>

        </div>

    </div>

    <div class="workspace-footer">

        <div class="workspace-status-card">

            <span>

                Empresa

            </span>

            <strong>

                Não conectada

            </strong>

        </div>

        <div class="workspace-status-card">

            <span>

                Dados

            </span>

            <strong>

                Aguardando Importação

            </strong>

        </div>

        <div class="workspace-status-card">

            <span>

                Diagnóstico

            </span>

            <strong>

                Não iniciado

            </strong>

        </div>

        <div class="workspace-status-card">

            <span>

                Plano de Ação

            </span>

            <strong>

                Indisponível

            </strong>

        </div>

    </div>
        <div class="workspace-dashboard">

        <div class="dashboard-card">

            <span class="dashboard-label">

                Receita

            </span>

            <strong>

                Aguardando dados

            </strong>

            <small>

                Envie documentos para iniciar os cálculos.

            </small>

        </div>

        <div class="dashboard-card">

            <span class="dashboard-label">

                Fluxo de Caixa

            </span>

            <strong>

                Não disponível

            </strong>

            <small>

                Nenhuma informação financeira recebida.

            </small>

        </div>

        <div class="dashboard-card">

            <span class="dashboard-label">

                Produção

            </span>

            <strong>

                Sem medições

            </strong>

            <small>

                Aguardando integração.

            </small>

        </div>

        <div class="dashboard-card">

            <span class="dashboard-label">

                Qualidade

            </span>

            <strong>

                Sem indicadores

            </strong>

            <small>

                Nenhum processo avaliado.

            </small>

        </div>

    </div>

    <div class="workspace-center">

        <div class="analysis-card">

            <h3>

                Diagnóstico Empresarial

            </h3>

            <p>

                O SIGFA apresentará aqui um resumo executivo
                após receber dados reais da empresa.

            </p>

            <div class="analysis-placeholder">

                Nenhum diagnóstico disponível.

            </div>

        </div>

        <div class="analysis-card">

            <h3>

                Recomendações da IA

            </h3>

            <p>

                O Super Gerente consolidará as análises
                realizadas pelos especialistas.

            </p>

            <ul>

                <li>Aguardando documentos.</li>

                <li>Aguardando integração.</li>

                <li>Aguardando análise.</li>

            </ul>

        </div>

        <div class="analysis-card">

            <h3>

                Plano de Ação

            </h3>

            <p>

                Após a análise serão sugeridas ações
                estratégicas priorizadas.

            </p>

            <div class="analysis-placeholder">

                Plano de ação indisponível.

            </div>

        </div>

    </div>
        <div class="workspace-timeline">

        <h3>

            Timeline Inteligente

        </h3>

        <div class="timeline-list">

            <div class="timeline-item">

                <span class="timeline-time">--:--</span>

                <div class="timeline-content">

                    Aguardando primeira interação.

                </div>

            </div>

            <div class="timeline-item">

                <span class="timeline-time">--:--</span>

                <div class="timeline-content">

                    Nenhum documento recebido.

                </div>

            </div>

            <div class="timeline-item">

                <span class="timeline-time">--:--</span>

                <div class="timeline-content">

                    Nenhum diagnóstico realizado.

                </div>

            </div>

        </div>

    </div>

</section>

    `;

};

export default Workspace;