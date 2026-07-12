const render = (html) => {
    const root = document.getElementById('root');
    if (!root) return;
    root.innerHTML = html;
};

const setLocationHash = (hash) => {
    window.location.hash = hash;
};

const showToast = (message, type = 'info') => {
    const existing = document.getElementById('sigfa-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'sigfa-toast';
    toast.className = `sigfa-toast sigfa-toast--${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 4000);
};

export { render, setLocationHash, showToast };
