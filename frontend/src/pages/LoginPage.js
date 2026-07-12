import LoginBrand from '../components/auth/LoginBrand.js';
import LoginForm from '../components/auth/LoginForm.js';

const LoginPage = () => {

    return `

    <section class="sigfa-login-page">

        <div class="sigfa-login-container">

            ${LoginBrand()}

            ${LoginForm()}

        </div>

    </section>

    `;

};

export default LoginPage;