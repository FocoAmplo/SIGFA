import SidebarNav from '../components/navigation/SidebarNav.js';
import Topbar from '../components/layout/Topbar.js';

const AppLayout = ({ topbar, main, activeMenu = 'dashboard' }) => {
  return `
    <div class="app-shell">
      <aside class="app-sidebar">
        <div class="sidebar-brand">
          <div class="sidebar-logo">
            <img src="/src/assets/images/logo-focoamplo.png" alt="Foco Amplo" />
          </div>
          <span>Centro SIGFA</span>
        </div>
        ${SidebarNav(activeMenu)}
      </aside>

      <div class="app-main">
        ${Topbar({ title: topbar.title })}

        <main class="app-content">
          ${main}
        </main>
      </div>
    </div>
  `;
};

export default AppLayout;
