const PageHeader = ({
    title = "",
    subtitle = ""
} = {}) => {

    return `

        <div class="page-header">

            <div>

                <h1 class="page-title">

                    ${title}

                </h1>

                <p class="page-subtitle">

                    ${subtitle}

                </p>

            </div>

        </div>

    `;

};

export default PageHeader;