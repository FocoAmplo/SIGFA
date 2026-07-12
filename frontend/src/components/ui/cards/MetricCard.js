import Card from "./Card.js";

const MetricCard = ({
    title = "",
    value = "",
    variation = "",
    icon = "📊"
} = {}) => {

    return Card({

        className: "metric-card",

        children: `

            <div class="metric-icon">

                ${icon}

            </div>

            <div class="metric-value">

                ${value}

            </div>

            <div class="metric-title">

                ${title}

            </div>

            <div class="metric-variation">

                ${variation}

            </div>

        `

    });

};

export default MetricCard;