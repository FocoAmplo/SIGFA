import "./styles/global.css";

import App from "./App.js";
import api from "./services/api.js";
import intelligenceStore from "./store/intelligence.store.js";
import intelligenceController from "./scripts/intelligenceController.js";
import { showToast } from "./scripts/ui.js";

const root = document.getElementById("root");

if (!root) {
    throw new Error("Elemento #root não encontrado.");
}

let rendering = false;

async function renderApp() {

    if (rendering) return;

    rendering = true;

    try {
        root.innerHTML = await App();
    } finally {
        rendering = false;
    }
}

window.addEventListener("load", async () => {

    await renderApp();

    intelligenceController.initialize();

});

window.addEventListener("hashchange", renderApp);

window.addEventListener("sigfa:update", renderApp);

intelligenceStore.subscribe(async () => {

    await renderApp();

});

document.addEventListener("click", async (event) => {

    if (event.target.matches("[data-provider]")) {

        event.preventDefault();

        const provider = event.target.dataset.provider;

        const email = prompt(`Informe o e-mail para continuar com ${provider}`);

        if (!email) return;

        try {

            const data = await api.post("/auth/external", {
                provider,
                email,
                name: email.split("@")[0]
            });

            localStorage.setItem(
                "sigfa_access_token",
                data.access_token
            );

            if (data.refresh_token) {
                localStorage.setItem(
                    "sigfa_refresh_token",
                    data.refresh_token
                );
            }

            showToast(
                `Login com ${provider} realizado com sucesso.`,
                "success"
            );

            window.location.hash = "#dashboard";

        } catch (error) {

            showToast(error.message, "error");

        }

        return;
    }

    if (event.target.id === "login-submit") {

        event.preventDefault();

        const email = document.getElementById("email")?.value;
        const password = document.getElementById("password")?.value;

        if (!email || !password) {

            showToast(
                "Preencha e-mail e senha.",
                "warning"
            );

            return;

        }

        try {

            const data = await api.post("/auth/login", {
                email,
                senha: password
            });

            localStorage.setItem(
                "sigfa_access_token",
                data.access_token
            );

            if (data.refresh_token) {
                localStorage.setItem(
                    "sigfa_refresh_token",
                    data.refresh_token
                );
            }

            showToast(
                "Login realizado com sucesso.",
                "success"
            );

            window.location.hash = "#dashboard";

        } catch (error) {

            showToast(
                error.message,
                "error"
            );

        }

        return;
    }

    if (event.target.id === "login-demo") {

        event.preventDefault();

        showToast(
            "Solicitação enviada.",
            "info"
        );

    }

});

console.log("SIGFA 1.0 iniciado.");