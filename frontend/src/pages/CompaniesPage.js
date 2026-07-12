import api from '../services/api.js';
import { showToast } from '../scripts/ui.js';
import DocumentsPage from './DocumentsPage.js';

const CompaniesPage = async ({ company } = {}) => {
    try {

        const companies = await api.get('/empresas/');

        const companyId = company ? Number(company) : null;

        const selectedCompany =
            companies.find(item => item.id === companyId) || null;

        const rows = companies.map(item => `
            <div class="company-card">

                <h3>${item.nome}</h3>

                <p>${item.cnpj ?? '--'}</p>

                <p>${item.endereco ?? 'Endereço não informado'}</p>

                <button
                    class="company-link"
                    data-company-id="${item.id}"
                >
                    Ver documentos
                </button>

            </div>
        `).join('');

        let documentsHtml = '';

        if (selectedCompany) {
            documentsHtml = await DocumentsPage({
                companyId: selectedCompany.id,
                companyName: selectedCompany.nome
            });
        }

        return `
            <section class="page-section">

                <div class="page-header">
                    <h2>Empresas</h2>

                    <p>
                        Visualize as empresas cadastradas e seus documentos.
                    </p>
                </div>

                <div class="companies-grid">
                    ${rows}
                </div>

                ${documentsHtml}

            </section>
        `;

    } catch (error) {

        showToast(error.message, 'error');

        return `
            <section class="page-section">

                <h2>Empresas</h2>

                <p>Erro ao carregar empresas.</p>

            </section>
        `;
    }
};

export default CompaniesPage;