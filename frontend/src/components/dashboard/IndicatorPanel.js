const IndicatorPanel = ({ items }) => {
    return `
    <section class="indicator-panel">
      <div class="section-headline">
        <span class="section-label">Indicadores</span>
        <h2>Visão rápida dos principais indicadores</h2>
      </div>
      <div class="indicator-grid">
        ${items.map(item => `
          <div class="indicator-tile">
            <span class="indicator-name">${item.label}</span>
            <strong class="indicator-value">${item.value}</strong>
            <span class="indicator-status">${item.status}</span>
          </div>
        `).join('')}
      </div>
    </section>
  `;
};

export default IndicatorPanel;
