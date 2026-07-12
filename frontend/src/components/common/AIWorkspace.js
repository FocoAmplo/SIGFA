import AIHero from '../AIHero.js';
import SuggestionChips from './SuggestionChips.js';
import DynamicWorkspace from './DynamicWorkspace.js';
import CompanySummary from './CompanySummary.js';
import KPIOverview from '../dashboard/KPIOverview.js';
import SpecialistCard from '../panels/SpecialistCard.js';

const AIWorkspace = () => {

    return `

        <section class="ai-workspace">

            <div class="workspace-main">

                ${AIHero()}

                ${SuggestionChips()}

                ${DynamicWorkspace()}

            </div>

            <aside class="workspace-sidebar">

                ${CompanySummary()}

                ${KPIOverview()}

                ${SpecialistCard()}

            </aside>

        </section>

    `;

};

export default AIWorkspace;