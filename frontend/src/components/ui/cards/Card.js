import { colors } from "../../../theme";

const Card = ({
    title = "",
    subtitle = "",
    children = "",
    footer = "",
    className = ""
} = {}) => {

    return `

        <section class="sigfa-card ${className}">

            ${title ? `

                <header class="sigfa-card-header">

                    <div>

                        <h3 class="sigfa-card-title">

                            ${title}

                        </h3>

                        ${subtitle
                ? `<p class="sigfa-card-subtitle">${subtitle}</p>`
                : ""}

                    </div>

                </header>

            ` : ""}

            <div class="sigfa-card-body">

                ${children}

            </div>

            ${footer
            ? `

                <footer class="sigfa-card-footer">

                    ${footer}

                </footer>

                `
            : ""}

        </section>

    `;

};

export default Card;