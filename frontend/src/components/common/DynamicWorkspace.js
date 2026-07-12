const DynamicWorkspace = () => {

    return `

        <section class="dynamic-workspace">

            <div class="workspace-header">

                <div>

                    <span>

                        CENTRO DE OPERAÇÕES INTELIGENTE

                    </span>

                    <h2>

                        Consultor Inteligente SIGFA

                    </h2>

                </div>

                <div class="workspace-status">

                    <span class="status-online"></span>

                    IA Online

                </div>

            </div>

            <div class="workspace-conversation">

                <div class="conversation-message ai">

                    <div class="conversation-avatar">

                        IA

                    </div>

                    <div class="conversation-content">

                        <strong>

                            Bem-vindo ao Centro de Inteligência.

                        </strong>

                        <p>

                            Ainda não existem documentos enviados para análise.

                        </p>

                        <p>

                            Assim que sua empresa enviar indicadores, planilhas, documentos ou relatórios, iniciarei automaticamente a leitura das informações.

                        </p>

                    </div>

                </div>

                <div class="conversation-message system">

                    <div class="conversation-content">

                        <strong>

                            Próximas análises disponíveis

                        </strong>

                        <ul>

                            <li>Diagnóstico Financeiro</li>

                            <li>Diagnóstico Comercial</li>

                            <li>Diagnóstico Produção</li>

                            <li>Diagnóstico Qualidade</li>

                            <li>Plano Estratégico</li>

                            <li>Plano de Ação</li>

                        </ul>

                    </div>

                </div>
                            <div class="workspace-processing">

                <h3>

                    Estado do Centro de Inteligência

                </h3>

                <div class="processing-list">

                    <div class="processing-item completed">

                        <span>●</span>

                        Plataforma conectada.

                    </div>

                    <div class="processing-item completed">

                        <span>●</span>

                        Consultor Inteligente disponível.

                    </div>

                    <div class="processing-item waiting">

                        <span>●</span>

                        Aguardando documentos da empresa.

                    </div>

                    <div class="processing-item waiting">

                        <span>●</span>

                        Aguardando indicadores para análise.

                    </div>

                    <div class="processing-item waiting">

                        <span>●</span>

                        Diagnóstico Estratégico pendente.

                    </div>

                </div>

            </div>

            <div class="workspace-empty-state">

                <div class="workspace-empty-icon">

                    🧠

                </div>

                <h3>

                    Nenhuma análise em andamento

                </h3>

                <p>

                    Assim que sua empresa enviar documentos ou indicadores,
                    o SIGFA iniciará automaticamente a leitura dos dados,
                    identificará riscos, oportunidades e apresentará
                    recomendações estratégicas fundamentadas nas informações
                    recebidas.

                </p>

                <button class="workspace-start">

                    Iniciar Centro de Inteligência

                </button>

            </div>

        </section>

    `;

};

export default DynamicWorkspace;