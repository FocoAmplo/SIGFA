const Topbar = ({ title }) => {

  return `

        <header class="app-topbar">

            <div class="topbar-brand">

                <div class="topbar-logo">

                    <img
                        src="/src/assets/images/logo-focoamplo.png"
                        alt="SIGFA"
                    />

                </div>

                <div class="topbar-title-group">

                    <span class="topbar-subtitle">

                        Plataforma Corporativa

                    </span>

                    <strong>

                        ${title}

                    </strong>

                </div>

            </div>

            <div class="topbar-search">

                <input
                    type="search"
                    placeholder="Pesquisar módulos, indicadores, empresas ou documentos..."
                />

                <button
                    class="topbar-search-btn"
                    type="button"
                >

                    Buscar

                </button>

            </div>

            <div class="topbar-actions">

                <button
                    class="topbar-action"
                    type="button"
                    title="Notificações"
                >

                    N

                </button>

                <button
                    class="topbar-action"
                    type="button"
                    title="Configurações"
                >

                    C

                </button>

            </div>

            <div class="topbar-user">

                <span class="topbar-user-name">

                    Administrador

                </span>

                <span class="topbar-user-badge">

                    Enterprise

                </span>

            </div>

        </header>

    `;

};

export default Topbar;