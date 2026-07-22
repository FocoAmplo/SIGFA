import LoginPage from "../pages/LoginPage.js";
import DashboardPage from "../pages/DashboardPage.js";
import CompaniesPage from "../pages/CompaniesPage.js";
import DocumentsPage from "../pages/DocumentsPage.js";
import ReportsPage from "../pages/ReportsPage.js";
import SettingsPage from "../pages/SettingsPage.js";

const ROUTES = {
    login: LoginPage,
    dashboard: DashboardPage,
    empresas: CompaniesPage,
    documentos: DocumentsPage,
    relatorios: ReportsPage,
    configuracoes: SettingsPage,
};

export function parseRoute(hash = "") {

    const route = hash.replace("#", "") || "dashboard";

    return {
        routeKey: route
    };

}

export function getRoute(routeKey) {

    return ROUTES[routeKey] || DashboardPage;

}