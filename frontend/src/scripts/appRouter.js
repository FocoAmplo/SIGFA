import LoginPage from '../pages/LoginPage.js';
import DashboardPage from '../pages/DashboardPage.js';
import CompaniesPage from '../pages/CompaniesPage.js';
import SuperManagerPage from '../pages/SuperManagerPage.js';

const ROUTES = {
    login: () => LoginPage(),
    dashboard: () => DashboardPage(),
    empresas: (params) => CompaniesPage(params),
    indicadores: () => `<section class="page-section"><h2>Indicadores</h2><p>Funcionalidade em desenvolvimento.</p></section>`,
    financeiro: () => `<section class="page-section"><h2>Financeiro</h2><p>Funcionalidade em desenvolvimento.</p></section>`,
    processos: () => `<section class="page-section"><h2>Processos</h2><p>Funcionalidade em desenvolvimento.</p></section>`,
    relatorios: () => `<section class="page-section"><h2>Relatórios</h2><p>Funcionalidade em desenvolvimento.</p></section>`,
    configuracoes: () => `<section class="page-section"><h2>Configurações</h2><p>Funcionalidade em desenvolvimento.</p></section>`,
    supergerente: () => SuperManagerPage(),
};

const parseRoute = (hash) => {
    const route = hash.replace('#', '').split('?')[0] || 'dashboard';
    const query = hash.includes('?') ? hash.split('?')[1] : '';
    const params = new URLSearchParams(query);
    return {
        routeKey: route || 'dashboard',
        params: Object.fromEntries(params.entries()),
    };
};

const getRoute = (routeKey) => ROUTES[routeKey] || ROUTES.dashboard;

export { getRoute, parseRoute };