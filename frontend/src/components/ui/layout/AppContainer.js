import '../../../styles/layout.css';

const AppContainer = ({ sidebar, topbar, children }) => {
    return `
    <div class="sigfa-app">

      <aside class="sigfa-sidebar">
        ${sidebar || ''}
      </aside>

      <section class="sigfa-workspace">

        <header class="sigfa-topbar">
          ${topbar || ''}
        </header>

        <main class="sigfa-content">
          ${children || ''}
        </main>

      </section>

    </div>
  `;
};

export default AppContainer;