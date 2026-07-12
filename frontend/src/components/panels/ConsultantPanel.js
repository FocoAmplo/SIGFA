const IndicatorPanel = ({ items = [] }) => {

  return `

        <section class="indicator-panel">

            <div class="section-headline">

                <span class="section-label">

                    Indicadores

                </span>

                <h2>

                    Visão rápida dos principais indicadores

                </h2>

            </div>

            <div class="indicator-grid">

                ${items.map(item => `

                    <div class="indicator-tile">

                        <span class="indicator-name">

                            ${item.label || item.title || '-'}

                        </span>

                        <strong class="indicator-value">

                            ${item.value ?? 0}

                        </strong>

                        <span class="indicator-status">

                            ${item.status || item.detail || ''}

                        </span>

                    </div>

                `).join('')}

            </div>

        </section>

    `;

};

export default IndicatorPanel;