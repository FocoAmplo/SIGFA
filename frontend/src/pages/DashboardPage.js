import AIHero from '../components/dashboard/AIHero.js';
import DynamicWorkspace from '../components/common/DynamicWorkspace.js';
import SpecialistCard from '../components/panels/SpecialistCard.js';

const DashboardPage = async () => {

    return `

        <section class="dashboard-page">

            ${AIHero()}

            <section class="dashboard-workspace">

                <div class="workspace-left">

                    ${DynamicWorkspace()}

                </div>

                <aside class="workspace-right">

                    ${SpecialistCard()}

                </aside>

            </section>

        </section>

    `;

};

export default DashboardPage;