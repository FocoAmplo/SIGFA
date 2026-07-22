const Topbar = ({ title }) => {

    return `

        <header class="app-topbar">

            <div class="topbar-brand">

                <div class="topbar-title-group">

                    <span class="topbar-subtitle">

                        Plataforma Corporativa

                    </span>

                    <strong>

                        ${title}

                    </strong>

                </div>

            </div>

            <div class="topbar-actions">

                <div class="topbar-status">

                    <span class="status-dot"></span>

                    IA Online

                </div>

                <button
                    class="topbar-action"
                    type="button"
                    title="Notificações"
                >

                    🔔

                </button>

                <div class="topbar-user">

                    <div class="topbar-avatar">

                        SL

                    </div>

                    <div class="topbar-user-info">

                        <strong>Silvanio Lopes</strong>

                        <span>Gestor Master</span>

                    </div>

                </div>

            </div>

        </header>

    `;

};

export default Topbar;