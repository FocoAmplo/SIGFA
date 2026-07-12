const Topbar = ({
    title = "Dashboard",
    user = {}
} = {}) => {

    const initials =
        user.initials ||
        (user.name
            ? user.name
                .split(" ")
                .map(n => n[0])
                .slice(0, 2)
                .join("")
                .toUpperCase()
            : "?");

    return `

        <div class="topbar-wrapper">

            <div class="topbar-left">

                <h1 class="topbar-title">
                    ${title}
                </h1>

                <span class="topbar-subtitle">
                    Plataforma Inteligente de Gestão
                </span>

            </div>

            <div class="topbar-center">

                <input
                    class="topbar-search"
                    type="search"
                    placeholder="Pesquisar empresas, documentos ou indicadores..."
                />

            </div>

            <div class="topbar-right">

                <button class="topbar-button">🔔</button>

                <button class="topbar-button">⚙️</button>

                <div class="topbar-user">

                    <div class="topbar-avatar">

                        ${initials}

                    </div>

                    <div>

                        <strong>

                            ${user.name || "Usuário"}

                        </strong>

                        <small>

                            ${user.role || "Perfil"}

                            ${user.company
            ? ` • ${user.company}`
            : ""}

                        </small>

                    </div>

                </div>

            </div>

        </div>

    `;

};

export default Topbar;