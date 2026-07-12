const API_BASE = 'http://127.0.0.1:8000';

const defaultHeaders = (isForm = false) => ({
    ...(isForm ? {} : { 'Content-Type': 'application/json' }),
});

const handleResponse = async (response) => {
    const text = await response.text();
    const data = text ? JSON.parse(text) : null;
    if (!response.ok) {
        const message = data?.detail || data?.message || response.statusText;
        throw new Error(message);
    }
    return data;
};

const request = async (path, options = {}, isForm = false) => {
    const token = localStorage.getItem('sigfa_access_token');
    const headers = {
        ...(options.headers || {}),
        ...defaultHeaders(isForm),
    };

    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    const response = await fetch(`${API_BASE}${path}`, {
        ...options,
        headers,
    });

    return handleResponse(response);
};

const post = (path, body) => request(path, { method: 'POST', body: JSON.stringify(body) });
const postForm = (path, formData) => request(path, { method: 'POST', body: formData }, true);
const upload = (path, formData) => request(path, { method: 'POST', body: formData }, true);
const get = (path) => request(path, { method: 'GET' });

export default {
    post,
    postForm,
    get,
    upload,
};
