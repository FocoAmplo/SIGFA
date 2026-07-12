import api from '../services/api.js';

const SuperManagerPage = () => `
  <section class="intel-platform">
    <div class="intel-chat-shell">
      <aside class="intel-sidebar">
        <div class="intel-sidebar-header">
          <span class="section-label">Nosso agente de IA</span>
          <h2>Coletando informações do cliente</h2>
          <p>O agente acompanha contexto, riscos, indicadores e próximos passos do projeto.</p>
        </div>

        <div class="intel-metrics">
          <div class="intel-metric-card">
            <span>Indicadores</span>
            <strong>+18%</strong>
            <small>Performance operacional</small>
          </div>
          <div class="intel-metric-card">
            <span>Riscos</span>
            <strong>3</strong>
            <small>Itens prioritários</small>
          </div>
          <div class="intel-metric-card">
            <span>Ações</span>
            <strong>7</strong>
            <small>Próximos passos</small>
          </div>
        </div>
      </aside>

      <div class="intel-chat-panel">
        <div class="intel-chat-header">
          <div>
            <span class="section-label">Centro de Inteligência SIGFA</span>
            <h1>Assistente executivo</h1>
          </div>
          <div class="intel-badge">Operação · Estratégia · IA</div>
        </div>

        <div class="intel-chat-messages">
          <div class="message message-assistant">
            <strong>Agente SIGFA</strong>
            <p>Olá. Estou pronto para analisar o contexto do projeto, os documentos enviados e os indicadores relacionados. Descreva a situação ou faça o upload dos arquivos.</p>
          </div>
        </div>

        <form id="super-manager-form" class="intel-chat-form">
          <div class="intel-chat-input-row">
            <textarea id="ai-prompt" rows="3" placeholder="Descreva o cenário, o desafio ou o que você quer diagnosticar..."></textarea>
            <button type="submit" class="btn btn-primary">Enviar</button>
          </div>
          <div class="intel-upload-row">
            <label class="intel-upload">
              <input id="ai-files" type="file" multiple accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.xml,.png,.jpg,.jpeg,.gif,.webp,.mp3,.wav,.mp4,.mov,.txt">
              <span>📎 Anexar documentos</span>
            </label>
            <select id="ai-provider" class="intel-select">
              <option value="mock">Modo simulado</option>
              <option value="openai">OpenAI</option>
              <option value="anthropic">Anthropic</option>
            </select>
          </div>
        </form>

        <section id="ai-response" class="intel-response" style="display:none;"></section>
      </div>
    </div>
  </section>
`;

export default SuperManagerPage;
