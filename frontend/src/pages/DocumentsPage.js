import api from '../services/api.js';
import { showToast } from '../scripts/ui.js';

const DocumentsPage = async ({ companyId, companyName }) => {
    try {
        const documents = await api.get(`/empresas/${companyId}/documentos`);

        const documentRows = documents.map((doc) => `
            <article class="document-card">
                <div class="document-info">
                    <strong>${doc.titulo}</strong>
                    <span>${doc.descricao || 'Sem descrição'}</span>
                </div>

                <div class="document-actions">
                    <a
                        href="http://127.0.0.1:8000/empresas/${companyId}/documentos/${doc.id}/download"
                        target="_blank"
                        rel="noreferrer"
                    >
                        Download
                    </a>
                </div>
            </article>
        `).join('');

        return `
            <section class="page-section documents-section">

                <div class="page-header">
                    <h2>Documentos de ${companyName || 'Empresa'}</h2>

                    <p>
                        Gerencie todos os documentos utilizados pelo
                        diagnóstico e pela consultoria SIGFA.
                    </p>
                </div>

                <form
                    id="upload-document-form"
                    class="upload-document-form"
                    data-company-id="${companyId}"
                >

                    <div class="form-row">
                        <label>Título</label>
                        <input
                            id="document-title"
                            type="text"
                            placeholder="Título do documento"
                        />
                    </div>

                    <div class="form-row">
                        <label>Descrição</label>
                        <input
                            id="document-description"
                            type="text"
                            placeholder="Descrição opcional"
                        />
                    </div>

                    <div class="form-row">
                        <label>Arquivo</label>
                        <input
                            id="document-file"
                            type="file"
                        />
                    </div>

                    <button
                        type="button"
                        class="btn-primary"
                        id="upload-document-submit"
                    >
                        Enviar Documento
                    </button>

                </form>

                <div class="document-list">
                    ${documentRows.length
                ? documentRows
                : '<p>Nenhum documento enviado.</p>'
            }
                </div>

            </section>
        `;
    } catch (error) {
        showToast(error.message, 'error');

        return `
            <section class="page-section">
                <h2>Documentos</h2>
                <p>Erro ao carregar os documentos.</p>
            </section>
        `;
    }
};

export default DocumentsPage;