const DashboardMetricCard = ({ title, value, detail, variant = 'default' }) => {
    return `
    <article class="dashboard-card dashboard-card--${variant}">
      <div class="card-meta">
        <span>${title}</span>
      </div>
      <div class="card-value">${value}</div>
      <p>${detail}</p>
    </article>
  `;
};

export default DashboardMetricCard;
