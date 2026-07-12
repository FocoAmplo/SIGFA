const Content = ({ children = "" } = {}) => {

    return `

        <section class="sigfa-page-content">

            ${children}

        </section>

    `;

};

export default Content;