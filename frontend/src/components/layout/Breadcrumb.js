const Breadcrumb = ({ items = [] }) => {
    if (!items.length) return '';

    return `
        <nav class="breadcrumb">
            ${items
            .map((item, index) => `
                    <span class="breadcrumb-item ${index === items.length - 1 ? 'active' : ''}">
                        ${item}
                    </span>
                    ${index < items.length - 1 ? '<span class="breadcrumb-divider">›</span>' : ''}
                `)
            .join('')}
        </nav>
    `;
};

export default Breadcrumb;