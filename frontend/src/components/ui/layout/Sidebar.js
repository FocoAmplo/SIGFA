import { MENU_ITEMS } from '../../../services/navigation.js';

const Sidebar = (active = 'dashboard') => {

    return `
        <div class="sidebar-wrapper">

            <div class="sidebar-brand">

                <img
                    src="/logo-focoamplo.png"
                    class="sidebar-logo"
                    alt="Foco Amplo"
                />

                <div class="sidebar-brand-text">

                    <span class="sidebar-company">
                        FOCO AMPLO
                    </span>

                    <strong class="sidebar-system">
                        SIGFA
                    </strong>

                </div>

            </div>

            <nav class="sidebar-menu">

                ${MENU_ITEMS.map(item => `

                    <a
                        href="${item.external || `#${item.key}`}"
                        class="sidebar-item ${active === item.key ? 'active' : ''}"
                        ${item.external ? 'target="_blank"' : ''}
                    >

                        <span class="sidebar-icon">
                            ${item.icon}
                        </span>

                        <span class="sidebar-label">
                            ${item.label}
                        </span>

                    </a>

                `).join('')}

            </nav>

            <div class="sidebar-footer">

                <div class="sidebar-status">

                    <span class="status-dot"></span>

                    Sistema Online

                </div>

                <small>
                    SIGFA 1.0
                </small>

            </div>

        </div>
    );

};

export default Sidebar;