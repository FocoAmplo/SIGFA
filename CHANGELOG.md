# CHANGELOG

Todas as alterações relevantes do SIGFA serão registradas neste documento.

---

# SIGFA 1.0

## Sprint 01 — Estrutura Inicial

Status: Concluída

### Entregas

- Estrutura inicial do projeto
- Organização das pastas
- Backend e Frontend
- Banco de dados

---

## Sprint 02 — Models e Schemas

Status: Concluída

### Entregas

- Models consolidados
- Schemas padronizados
- Relacionamentos SQLAlchemy
- Estrutura PostgreSQL

---

## Sprint 03 — Authentication Migration

Status: Concluída

### Entregas

- AuthService reconstruído
- Login atualizado
- JWT
- Refresh Token
- APIs de autenticação
- Compatibilidade com Models atuais

---

## Sprint 04 — Diagnosis Module

Status: Concluída

### Entregas

- DiagnosisService
- AnswerService
- ScoreService
- ActionPlanService
- AttachmentService
- HistoryService
- AIRecommendationService

### APIs

- /diagnosis
- /answer
- /score
- /action-plan
- /attachment
- /history
- /ai-recommendation

### Internacionalização

- Estrutura i18n criada
- Português como idioma padrão
- Inglês
- Espanhol
- Francês
- Alemão
- Italiano

---

## Sprint 04.1 — Core Stabilization

Status: Concluída

### Correções

- Correção do startup
- Correção do seed.py
- Registro dos Routers Knowledge
- Inicialização completa da aplicação
- OpenAPI validado
- Health Check validado

### Validações

- Backend OK
- Startup OK
- Database OK
- APIs OK
- Diagnosis OK
- Authentication OK

### Pendências

- Foreign Keys legadas (adiadas para evolução futura)

---