import AIHero from '../components/dashboard/AIHero.js';
import DynamicWorkspace from '../components/common/DynamicWorkspace.js';
import KPIOverview from '../components/dashboard/KPIOverview.js';
import CompanySummary from '../components/common/CompanySummary.js';
import SpecialistCard from '../components/panels/SpecialistCard.js';
import SuggestionChips from '../components/common/SuggestionChips.js';

const DashboardPage = async () => {

    return `

        <section class="dashboard-page">

            <div class="dashboard-main">

                ${AIHero()}

                ${DynamicWorkspace()}

                ${KPIOverview()}

            </div>

            <section class="dashboard-bottom">

                <div class="dashboard-company">

                    ${CompanySummary()}

                </div>

                <div class="dashboard-specialist">

                    ${SpecialistCard()}

                </div>

            </section>

            ${SuggestionChips()}

        </section>

    `;

};

export default DashboardPage;