const API_BASE_URL =
  window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1"
    ? "http://127.0.0.1:8000"
    : "https://api.focoamplo.com.br";

function setStatus(elementId, message, type = "success") {
  const element = document.getElementById(elementId);
  if (!element) return;
  element.textContent = message;
  element.className = `form-status ${type}`;
}

function formToObject(form) {
  return Object.fromEntries(new FormData(form).entries());
}

async function parseResponse(response) {
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const message = data.detail || data.mensagem || "Nao foi possivel concluir a solicitacao.";
    throw new Error(Array.isArray(message) ? message.map((item) => item.msg).join("; ") : message);
  }
  return data;
}

async function handleSubmit(form, callback) {
  const button = form.querySelector("button[type='submit']");
  const originalText = button.textContent;
  button.disabled = true;
  button.textContent = "Enviando...";

  try {
    await callback();
  } finally {
    button.disabled = false;
    button.textContent = originalText;
  }
}

document.getElementById("access-form")?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  setStatus("access-status", "Enviando solicitacao...");

  await handleSubmit(form, async () => {
    try {
      const payload = formToObject(form);
      const response = await fetch(`${API_BASE_URL}/cliente/acesso/solicitar`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await parseResponse(response);
      setStatus("access-status", data.mensagem || "Solicitacao enviada com sucesso.");
      form.reset();
    } catch (error) {
      setStatus("access-status", error.message, "error");
    }
  });
});

document.getElementById("text-form")?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  setStatus("text-status", "Enviando texto...");

  await handleSubmit(form, async () => {
    try {
      const { apiKey, ...payload } = formToObject(form);
      const response = await fetch(`${API_BASE_URL}/cliente/envios/texto`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-SIGFA-API-Key": apiKey,
        },
        body: JSON.stringify(payload),
      });
      const data = await parseResponse(response);
      setStatus("text-status", data.mensagem || "Texto enviado com sucesso.");
      form.reset();
    } catch (error) {
      setStatus("text-status", error.message, "error");
    }
  });
});

document.getElementById("file-form")?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  setStatus("file-status", "Enviando arquivo...");

  await handleSubmit(form, async () => {
    try {
      const formData = new FormData(form);
      const apiKey = formData.get("apiKey");
      formData.delete("apiKey");

      const response = await fetch(`${API_BASE_URL}/cliente/envios/arquivo`, {
        method: "POST",
        headers: {
          "X-SIGFA-API-Key": apiKey,
        },
        body: formData,
      });
      const data = await parseResponse(response);
      setStatus("file-status", data.mensagem || "Arquivo enviado com sucesso.");
      form.reset();
    } catch (error) {
      setStatus("file-status", error.message, "error");
    }
  });
});
