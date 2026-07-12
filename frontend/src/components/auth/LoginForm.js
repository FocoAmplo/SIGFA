const LoginForm = () => {

    return `

    <section class="sigfa-login-form">

        <div class="sigfa-login-card">

            <span class="sigfa-login-small">

                Portal Corporativo

            </span>

            <h2>

                Entrar no SIGFA

            </h2>

            <p>

                Informe seus dados para acessar a plataforma.

            </p>

            <div style="display:flex; gap:10px; margin-bottom:20px; flex-wrap:wrap;">
                <button type="button" class="btn btn-secondary" data-provider="google">Google</button>
                <button type="button" class="btn btn-secondary" data-provider="microsoft">Microsoft</button>
                <button type="button" class="btn btn-secondary" data-provider="github">GitHub</button>
            </div>

            <form
                class="sigfa-form"
                autocomplete="off"
            >

                <div class="sigfa-form-group">

                    <label class="sigfa-label">

                        CNPJ

                    </label>

                    <input
                        class="sigfa-input"
                        id="cnpj"
                        type="text"
                        placeholder="00.000.000/0000-00"
                    >

                </div>

                <div class="sigfa-form-group">

                    <label class="sigfa-label">

                        Usuário

                    </label>

                    <input
                        class="sigfa-input"
                        id="email"
                        type="email"
                        placeholder="usuario@empresa.com.br"
                    >

                </div>

                <div class="sigfa-form-group">

                    <label class="sigfa-label">

                        Senha

                    </label>

                    <input
                        class="sigfa-input"
                        id="password"
                        type="password"
                        placeholder="••••••••••"
                    >

                </div>

                <div
                    style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    margin-top:10px;
                    "
                >

                    <label
                        style="
                        display:flex;
                        gap:10px;
                        align-items:center;
                        color:var(--color-text-secondary);
                        "
                    >

                        <input type="checkbox">

                        Lembrar acesso

                    </label>

                    <a href="#">

                        Esqueci minha senha

                    </a>

                </div>

                <button
                    id="login-submit"
                    class="btn btn-primary btn-full"
                    type="button"
                    style="margin-top:20px;"
                >

                    Entrar

                </button>

            </form>

            <div
                style="
                margin-top:30px;
                text-align:center;
                color:var(--color-text-muted);
                font-size:13px;
                "
            >

                🔒 Ambiente seguro • LGPD • SIGFA v1.0

            </div>

        </div>

    </section>

    `;

};

export default LoginForm;