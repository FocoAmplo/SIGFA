const Workspace = ({ content, rightPanel = '' }) => `
<div class="workspace">

    <section class="workspace-main">

        ${content}

    </section>

    <aside class="workspace-right">

        ${rightPanel}

    </aside>

</div>
`;

export default Workspace;