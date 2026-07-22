import intelligenceStore from '../../store/intelligence.store.js';

const CompanySummary = () => {

    const state = intelligenceStore.getState();

    const company = state.company?.name || "Nenhuma empresa";

    const documents = state.documents?.length || 0;

    const diagnosis = state.diagnosis
        ? "Disponível"
        : "Aguardando";

    return `

        <footer class="company-status-bar">

            <div class="company-status-item">

                <span>Empresa</span>

                <strong>${company}</strong>

            </div>

            <div class="company-status-item">

                <span>Documentos</span>

                <strong>${documents}</strong>

            </div>

            <div class="company-status-item">

                <span>Diagnóstico</span>

                <strong>${diagnosis}</strong>

            </div>

            <div class="company-status-item">

                <span>IA</span>

                <strong>

                    ${state.loading ? "Analisando..." : "Online"}

                </strong>

            </div>

        </footer>

    `;

};

export default CompanySummary;