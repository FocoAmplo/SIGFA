import intelligenceStore from '../../store/intelligence.store.js';

const DynamicWorkspace = () => {

    const state = intelligenceStore.getState();

    const messages = state.conversation || [];

    return `

        <section class="dynamic-workspace">

            <div class="workspace-conversation">

                ${messages.length

            ? messages.map(message => `

                        <article class="conversation-message ${message.role}">

                            <div class="message-header">

                                <strong>

                                    ${message.role === 'assistant'
                    ? 'SIGFA IA'
                    : 'Você'}

                                </strong>

                            </div>

                            <div class="message-body">

                                ${message.content}

                            </div>

                        </article>

                    `).join("")

            :

            `

                    <div class="conversation-placeholder">

                        <h3>

                            Centro de Inteligência pronto.

                        </h3>

                        <p>

                            Inicie uma conversa ou envie documentos para começar uma análise estratégica.

                        </p>

                    </div>

                    `

        }

            </div>

            ${state.loading

            ?

            `

                <div class="workspace-loading">

                    <span class="loading-dot"></span>

                    A IA está analisando as informações...

                </div>

                `

            :

            ''

        }

            <footer class="workspace-input">

                <textarea

                    id="ai-prompt"

                    rows="1"

                    placeholder="Pergunte ao Centro de Inteligência..."

                ></textarea>

                <div class="workspace-toolbar">

                    <input

                        id="ai-files"

                        type="file"

                        hidden

                        multiple

                        accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.xml,.png,.jpg,.jpeg,.gif,.webp,.txt"

                    />

                    <button

                        id="ai-upload-button"

                        class="workspace-upload"

                        type="button"

                        title="Anexar documentos">

                        📎

                    </button>

                    <button

                        id="ai-send"

                        class="workspace-send"

                        type="button"

                        title="Enviar">

                        ➜

                    </button>

                </div>

            </footer>

        </section>

    `;

};

export default DynamicWorkspace;