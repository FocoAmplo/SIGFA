const UploadCenter = () => {

    return `

<section class="upload-center">

    <div class="upload-header">

        <span class="upload-badge">

            CENTRAL DE DOCUMENTOS

        </span>

        <h2>

            Envie documentos para análise

        </h2>

        <p>

            O SIGFA utiliza apenas informações fornecidas pela empresa.
            Nenhum indicador é criado sem dados reais.

        </p>

    </div>

    <div class="upload-dropzone">

        <div class="upload-icon">

            ☁️

        </div>

        <h3>

            Arraste seus arquivos aqui

        </h3>

        <p>

            ou clique para selecionar documentos.

        </p>

        <button class="upload-button">

            Selecionar Arquivos

        </button>

    </div>

    <div class="upload-types">

        <div class="upload-card">

            <span>📄</span>

            <strong>PDF</strong>

            <small>Relatórios</small>

        </div>

        <div class="upload-card">

            <span>📊</span>

            <strong>Excel</strong>

            <small>Planilhas</small>

        </div>

        <div class="upload-card">

            <span>📈</span>

            <strong>CSV</strong>

            <small>Exportações</small>

        </div>

        <div class="upload-card">

            <span>📝</span>

            <strong>Word</strong>

            <small>Documentos</small>

        </div>

        <div class="upload-card">

            <span>🖼️</span>

            <strong>Imagem</strong>

            <small>Fotos</small>

        </div>

        <div class="upload-card">

            <span>🎤</span>

            <strong>Áudio</strong>

            <small>Gravações</small>

        </div>

        <div class="upload-card">

            <span>🎥</span>

            <strong>Vídeo</strong>

            <small>Processos</small>

        </div>

        <div class="upload-card">

            <span>🗂️</span>

            <strong>XML</strong>

            <small>Notas Fiscais</small>

        </div>

    </div>

    <div class="upload-info">

        <div class="info-box">

            <strong>

                Como funciona?

            </strong>

            <p>

                Os documentos enviados são analisados pelo Motor de
                Inteligência do SIGFA e encaminhados aos Especialistas
                para geração do diagnóstico empresarial.

            </p>

        </div>
                <div class="info-box">

            <strong>

                Fluxo Inteligente

            </strong>

            <ul>

                <li>Recebimento do arquivo</li>

                <li>Validação automática</li>

                <li>Leitura do conteúdo</li>

                <li>Classificação por tipo</li>

                <li>Envio aos Especialistas</li>

                <li>Consolidação pelo Super Gerente</li>

                <li>Geração do Diagnóstico</li>

                <li>Atualização do Dashboard Executivo</li>

            </ul>

        </div>

    </div>

    <div class="upload-footer">

        <div class="upload-status">

            <span class="status-dot"></span>

            Centro de Upload disponível.

        </div>

        <button class="primary-upload">

            Iniciar Importação

        </button>

    </div>

</section>

    `;

};

export default UploadCenter;