import { MENU_ITEMS } from '../../services/navigation.js';

const SidebarNav = (selected = 'dashboard') => {

  return `

        <nav class="sidebar-nav">

            ${MENU_ITEMS.map(item => `

                <a
                    href="${item.external || `#${item.key}`}"
                    class="sidebar-link ${selected === item.key ? 'active' : ''}"
                    ${item.external ? 'target="_blank" rel="noopener noreferrer"' : ''}
                >

                    <span class="sidebar-link-icon">

                        ${item.icon || '•'}

                    </span>

                    <span>

                        ${item.label}

                    </span>

                </a>

            `).join('')}

            <div style="flex:1"></div>

            <div class="sidebar-footer">

                <div class="footer-status">

                    <div class="status-dot"></div>

                    <span>

                        Plataforma Online

                    </span>

                </div>

                <small>

                    SIGFA Enterprise v1.0

                </small>

            </div>

        </nav>

    `;

};

export default SidebarNav;