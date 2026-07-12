import './styles/global.css';
import App from './App.js';
import { showToast } from './scripts/ui.js';
import api from './services/api.js';

const root = document.getElementById('root');
if (!root) {
    throw new Error('Root element not found: #root');
}

const renderApp = async () => {
    const html = await App();
    root.innerHTML = html;
};

window.addEventListener('hashchange', renderApp);
window.addEventListener('load', renderApp);

document.addEventListener('submit', async (event) => {
    const form = event.target;
    if (!(form instanceof HTMLFormElement)) return;

    if (form.id === 'super-manager-form') {
        event.preventDefault();
        const provider = document.getElementById('ai-provider')?.value || 'mock';
        const prompt = document.getElementById('ai-prompt')?.value?.trim();
        const responseBox = document.getElementById('ai-response');
        const fileInput = document.getElementById('ai-files');
        const files = Array.from(fileInput?.files || []);
        if (!prompt) {
            showToast('Descreva o contexto ou anexe documentos para gerar o diagnóstico', 'warning');
            return;
        }
        try {
            const formData = new FormData();
            formData.append('provider', provider);
            formData.append('prompt', prompt);
            files.forEach(file => formData.append('files', file));

            const data = await api.postForm('/ai/chat', formData);
            if (responseBox) {
                responseBox.style.display = 'block';
                responseBox.innerHTML = `
                    <div class="message message-assistant">
                        <strong>Agente SIGFA</strong>
                        <p>${data.response}</p>
                    </div>
                    <div class="intel-response-grid">
                        <div class="intel-card">
                            <h4>Resumo</h4>
                            <p>${data.analysis.summary}</p>
                        </div>
                        <div class="intel-card">
                            <h4>Indicadores</h4>
                            <ul>
                                ${data.analysis.indicators.map(item => `<li><strong>${item.name}</strong> · ${item.value} · ${item.trend}</li>`).join('')}
                            </ul>
                        </div>
                        <div class="intel-card">
                            <h4>Diagnósticos</h4>
                            <ul>
                                ${data.analysis.diagnostics.map(item => `<li><strong>${item.title}</strong> · ${item.description} · ${item.severity}</li>`).join('')}
                            </ul>
                        </div>
                        <div class="intel-card">
                            <h4>Riscos</h4>
                            <ul>
                                ${data.analysis.risks.map(item => `<li><strong>${item.title}</strong> · ${item.description} · ${item.severity}</li>`).join('')}
                            </ul>
                        </div>
                        <div class="intel-card intel-card--wide">
                            <h4>Recomendações</h4>
                            <ul>
                                ${data.analysis.recommendations.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                        </div>
                        <div class="intel-card intel-card--wide">
                            <h4>Plano de ação</h4>
                            <ul>
                                ${data.analysis.action_plan.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                `;
            }
            showToast('Diagnóstico gerado com sucesso', 'success');
        } catch (error) {
            showToast(error.message, 'error');
        }
    }
});

document.addEventListener('click', async (event) => {
    if (event.target.matches('[data-provider]')) {
        event.preventDefault();
        const provider = event.target.dataset.provider;
        const email = prompt(`Informe o e-mail para continuar com ${provider}`);
        if (!email) return;
        try {
            const data = await api.post('/auth/external', {
                provider,
                email,
                name: email.split('@')[0],
            });
            localStorage.setItem('sigfa_access_token', data.access_token);
            showToast(`Login com ${provider} realizado com sucesso`, 'success');
            window.location.hash = '#dashboard';
        } catch (error) {
            showToast(error.message, 'error');
        }
    }

    if (event.target.id === 'login-submit') {
        event.preventDefault();
        const email = document.getElementById('email')?.value;
        const password = document.getElementById('password')?.value;
        if (!email || !password) {
            showToast('Preencha e-mail e senha', 'warning');
            return;
        }

        try {
            const data = await api.post('/auth/login', { email, senha: password });
            localStorage.setItem('sigfa_access_token', data.access_token);
            localStorage.setItem('sigfa_refresh_token', data.refresh_token || '');
            showToast('Login realizado com sucesso', 'success');
            window.location.hash = '#dashboard';
        } catch (error) {
            showToast(error.message, 'error');
        }
    }

    if (event.target.id === 'login-demo') {
        event.preventDefault();
        showToast('Solicitação de demonstração enviada', 'info');
    }

    if (event.target.id === 'upload-document-submit') {
        event.preventDefault();
        const form = document.getElementById('upload-document-form');
        if (!form) return;
        const companyId = form.dataset.companyId;
        const titulo = document.getElementById('document-title')?.value;
        const descricao = document.getElementById('document-description')?.value;
        const fileInput = document.getElementById('document-file');
        const file = fileInput?.files?.[0];
        if (!companyId || !titulo || !file) {
            showToast('Preencha título, arquivo e selecione a empresa', 'warning');
            return;
        }

        const formData = new FormData();
        formData.append('titulo', titulo);
        formData.append('descricao', descricao || '');
        formData.append('file', file);

        try {
            await api.upload(`/empresas/${companyId}/documentos`, formData);
            showToast('Documento enviado com sucesso', 'success');
            window.location.reload();
        } catch (err) {
            showToast(err.message, 'error');
        }
    }

    if (event.target.matches('[data-company-id]')) {
        event.preventDefault();
        const companyId = event.target.dataset.companyId;
        if (companyId) {
            window.location.hash = `#empresas?company=${companyId}`;
        }
    }
});

console.log('SIGFA frontend mounted');
