import LoginPage from './pages/LoginPage.js';
import AppLayout from './layouts/AppLayout.js';
import { MENU_ITEMS } from './services/navigation.js';
import { getRoute, parseRoute } from './scripts/appRouter.js';

/*
|--------------------------------------------------------------------------
| SIGFA FRONTEND
|--------------------------------------------------------------------------
| true  = abre sempre o Dashboard (desenvolvimento)
| false = usa autenticação normal (produção)
|--------------------------------------------------------------------------
*/

const DEV_MODE = false;

const App = async () => {

    const { routeKey, params } = parseRoute(window.location.hash);

    const accessToken = localStorage.getItem('sigfa_access_token');

    let currentRoute = routeKey;

    if (DEV_MODE) {

        currentRoute = 'dashboard';

    } else {

        if (!accessToken && routeKey !== 'login') {

            currentRoute = 'login';

        }

        if (accessToken && routeKey === 'login') {

            currentRoute = 'dashboard';

        }

    }

    let pageContent = '';

    if (!DEV_MODE && currentRoute === 'login') {

        pageContent = LoginPage();

    } else {

        const page = getRoute(currentRoute);

        if (page) {

            pageContent = await page(params);

        } else {

            pageContent = `

                <section class="page-section">

                    <h2>Página não encontrada</h2>

                </section>

            `;

        }

    }

    const pageTitle =

        MENU_ITEMS.find(item => item.key === currentRoute)?.label ||

        'Dashboard';

    return AppLayout({

        topbar: {

            title: `SIGFA • ${pageTitle}`

        },

        main: pageContent,

        activeMenu: currentRoute

    });

};

export default App;
