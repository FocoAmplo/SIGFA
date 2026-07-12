const AuthCard = ({ title, caption, children }) => {
    return `
    <div class="auth-card">
      <div class="auth-card-header">
        <div class="login-logo">SIGFA</div>
        <div>
          <h2>${title}</h2>
          <p class="auth-caption">${caption}</p>
        </div>
      </div>
      ${children}
    </div>
  `;
};

export default AuthCard;
