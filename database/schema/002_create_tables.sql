-- ==========================================================
-- SIGFA PLATFORM
-- Arquivo: 002_create_tables.sql
-- BLOCO 01 - CORE
-- ==========================================================

-- ==========================================================
-- EMPRESAS
-- ==========================================================

CREATE TABLE IF NOT EXISTS sigfa.company (

    id              SERIAL PRIMARY KEY,

    uuid            UUID DEFAULT gen_random_uuid(),

    corporate_name  VARCHAR(250) NOT NULL,

    trade_name      VARCHAR(200),

    cnpj            VARCHAR(18),

    state_registration VARCHAR(30),

    municipal_registration VARCHAR(30),

    segment         VARCHAR(120),

    employees       INTEGER DEFAULT 0,

    city            VARCHAR(120),

    state           VARCHAR(2),

    country         VARCHAR(80) DEFAULT 'Brasil',

    phone           VARCHAR(30),

    email           VARCHAR(200),

    website         VARCHAR(200),

    active          BOOLEAN DEFAULT TRUE,

    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE sigfa.company IS 'Empresas cadastradas no SIGFA';

-- ==========================================================
-- PERFIS
-- ==========================================================

CREATE TABLE IF NOT EXISTS security.profiles (

    id              SERIAL PRIMARY KEY,

    uuid            UUID DEFAULT gen_random_uuid(),

    name            VARCHAR(100) NOT NULL,

    description     TEXT,

    active          BOOLEAN DEFAULT TRUE,

    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE security.profiles IS 'Perfis de acesso do sistema';

-- ==========================================================
-- PERMISSÕES
-- ==========================================================

CREATE TABLE IF NOT EXISTS security.permissions (

    id              SERIAL PRIMARY KEY,

    uuid            UUID DEFAULT gen_random_uuid(),

    code            VARCHAR(80) UNIQUE,

    name            VARCHAR(150),

    description     TEXT,

    module          VARCHAR(100),

    active          BOOLEAN DEFAULT TRUE,

    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE security.permissions IS 'Permissões do sistema';

-- ==========================================================
-- USUÁRIOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS security.users (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    company_id          INTEGER NOT NULL,

    profile_id          INTEGER,

    name                VARCHAR(200) NOT NULL,

    email               VARCHAR(200) UNIQUE NOT NULL,

    password_hash       TEXT NOT NULL,

    phone               VARCHAR(30),

    avatar              TEXT,

    last_login          TIMESTAMP,

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_company
        FOREIGN KEY(company_id)
        REFERENCES sigfa.company(id),

    CONSTRAINT fk_profile
        FOREIGN KEY(profile_id)
        REFERENCES security.profiles(id)

);

COMMENT ON TABLE security.users IS 'Usuários do SIGFA';
-- ==========================================================
-- KNOWLEDGE BASE
-- BLOCO 02
-- ==========================================================

-- ==========================================================
-- OMC
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.omc (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    code                VARCHAR(30) UNIQUE NOT NULL,

    title               VARCHAR(250) NOT NULL,

    category            VARCHAR(150),

    subcategory         VARCHAR(150),

    objective           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    maturity_level      NUMERIC(5,2) DEFAULT 0,

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE knowledge.omc IS 'Objetos Mestres do Conhecimento';

-- ==========================================================
-- CONCEITOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.concepts (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(250) NOT NULL,

    definition          TEXT,

    objective           TEXT,

    process             VARCHAR(150),

    area                VARCHAR(150),

    domain              VARCHAR(150),

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_concepts_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.concepts IS 'Conceitos da Base Cognitiva';

-- ==========================================================
-- MÉTODOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.methods (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(250),

    objective           TEXT,

    application         TEXT,

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_methods_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.methods IS 'Métodos utilizados pelo SIGFA';

-- ==========================================================
-- FERRAMENTAS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.tools (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(250),

    description         TEXT,

    application         TEXT,

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_tools_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.tools IS 'Ferramentas da Qualidade';

-- ==========================================================
-- KPIs
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.kpis (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(250) NOT NULL,

    description         TEXT,

    formula             TEXT,

    unit                VARCHAR(50),

    target_value        NUMERIC(12,2),

    warning_value       NUMERIC(12,2),

    critical_value      NUMERIC(12,2),

    frequency           VARCHAR(50),

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_kpis_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.kpis IS 'Indicadores de desempenho';

-- ==========================================================
-- PERGUNTAS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.questions (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    question            TEXT NOT NULL,

    question_type       VARCHAR(50),

    weight              NUMERIC(5,2),

    required_evidence   BOOLEAN DEFAULT FALSE,

    help_text           TEXT,

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_questions_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.questions IS 'Perguntas utilizadas nos diagnósticos';

-- ==========================================================
-- EVIDÊNCIAS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.evidences (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(250),

    description         TEXT,

    mandatory           BOOLEAN DEFAULT FALSE,

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_evidences_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.evidences IS 'Evidências exigidas pelo diagnóstico';

-- ==========================================================
-- RISCOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.risks (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(250) NOT NULL,

    description         TEXT,

    probability         VARCHAR(30),

    impact              VARCHAR(30),

    severity            VARCHAR(30),

    recommendation      TEXT,

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_risks_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.risks IS 'Catálogo de riscos do SIGFA';

-- ==========================================================
-- RECOMENDAÇÕES
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.recommendations (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    omc_id              INTEGER NOT NULL,

    code                VARCHAR(30) UNIQUE NOT NULL,

    title               VARCHAR(250),

    recommendation      TEXT,

    priority            VARCHAR(30),

    expected_result     TEXT,

    estimated_time      VARCHAR(100),

    keywords            TEXT,

    embedding           TEXT,

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_recommendations_omc
        FOREIGN KEY (omc_id)
        REFERENCES knowledge.omc(id)

);

COMMENT ON TABLE knowledge.recommendations IS 'Recomendações automáticas';

-- ==========================================================
-- RELACIONAMENTOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.relationships (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    source_type         VARCHAR(50),

    source_code         VARCHAR(30),

    target_type         VARCHAR(50),

    target_code         VARCHAR(30),

    relationship_type   VARCHAR(80),

    strength            NUMERIC(5,2),

    description         TEXT,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE knowledge.relationships IS 'Relacionamentos da Base Cognitiva';

-- ==========================================================
-- DIAGNOSIS
-- BLOCO 03
-- ==========================================================

-- ==========================================================
-- DIAGNÓSTICOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS diagnosis.diagnoses (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    company_id          INTEGER NOT NULL,

    title               VARCHAR(250),

    omc_code            VARCHAR(30),

    status              VARCHAR(30) DEFAULT 'OPEN',

    score               NUMERIC(6,2),

    maturity_level      NUMERIC(6,2),

    risk_level          VARCHAR(30),

    started_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    finished_at         TIMESTAMP,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_diagnosis_company
        FOREIGN KEY(company_id)
        REFERENCES sigfa.company(id)

);

COMMENT ON TABLE diagnosis.diagnoses IS 'Diagnósticos realizados';

-- ==========================================================
-- RESPOSTAS
-- ==========================================================

CREATE TABLE IF NOT EXISTS diagnosis.answers (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    diagnosis_id        INTEGER NOT NULL,

    question_code       VARCHAR(30),

    answer              TEXT,

    score               NUMERIC(6,2),

    observation         TEXT,

    evidence_file       TEXT,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_answers_diagnosis
        FOREIGN KEY(diagnosis_id)
        REFERENCES diagnosis.diagnoses(id)

);

COMMENT ON TABLE diagnosis.answers IS 'Respostas dos diagnósticos';

-- ==========================================================
-- PONTUAÇÕES
-- ==========================================================

CREATE TABLE IF NOT EXISTS diagnosis.scores (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    diagnosis_id        INTEGER NOT NULL,

    indicator_code      VARCHAR(30),

    value               NUMERIC(12,2),

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_scores_diagnosis
        FOREIGN KEY(diagnosis_id)
        REFERENCES diagnosis.diagnoses(id)

);

COMMENT ON TABLE diagnosis.scores IS 'Pontuações calculadas';

-- ==========================================================
-- PLANOS DE AÇÃO
-- ==========================================================

CREATE TABLE IF NOT EXISTS diagnosis.action_plans (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    diagnosis_id        INTEGER NOT NULL,

    recommendation_code VARCHAR(30),

    action_description  TEXT,

    responsible         VARCHAR(200),

    due_date            DATE,

    priority            VARCHAR(30),

    status              VARCHAR(30) DEFAULT 'PENDING',

    progress            NUMERIC(5,2) DEFAULT 0,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_action_plan
        FOREIGN KEY (diagnosis_id)
        REFERENCES diagnosis.diagnoses(id)

);

COMMENT ON TABLE diagnosis.action_plans IS
'Plano de ação gerado automaticamente pelo SIGFA';

-- ==========================================================
-- ANEXOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS diagnosis.attachments (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    diagnosis_id        INTEGER NOT NULL,

    file_name           VARCHAR(255),

    file_path           TEXT,

    file_type           VARCHAR(50),

    uploaded_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_attachment
        FOREIGN KEY (diagnosis_id)
        REFERENCES diagnosis.diagnoses(id)

);

COMMENT ON TABLE diagnosis.attachments IS
'Arquivos enviados durante os diagnósticos';

-- ==========================================================
-- HISTÓRICO
-- ==========================================================

CREATE TABLE IF NOT EXISTS diagnosis.history (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    diagnosis_id        INTEGER NOT NULL,

    event_type          VARCHAR(100),

    description         TEXT,

    user_name           VARCHAR(200),

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_history
        FOREIGN KEY (diagnosis_id)
        REFERENCES diagnosis.diagnoses(id)

);

COMMENT ON TABLE diagnosis.history IS
'Histórico completo dos diagnósticos';

-- ==========================================================
-- DASHBOARD
-- ==========================================================

-- DASHBOARDS

CREATE TABLE IF NOT EXISTS dashboard.dashboards (

    id SERIAL PRIMARY KEY,

    uuid UUID DEFAULT gen_random_uuid(),

    code VARCHAR(30) UNIQUE,

    name VARCHAR(200),

    description TEXT,

    active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE dashboard.dashboards IS
'Painéis disponíveis no SIGFA';


-- ==========================================================
-- CARDS
-- ==========================================================

CREATE TABLE IF NOT EXISTS dashboard.cards (

    id SERIAL PRIMARY KEY,

    uuid UUID DEFAULT gen_random_uuid(),

    dashboard_id INTEGER NOT NULL,

    code VARCHAR(30),

    title VARCHAR(200),

    metric_code VARCHAR(30),

    icon VARCHAR(100),

    color VARCHAR(50),

    position INTEGER,

    active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_cards_dashboard
        FOREIGN KEY (dashboard_id)
        REFERENCES dashboard.dashboards(id)

);

COMMENT ON TABLE dashboard.cards IS
'Cards exibidos no Dashboard';


-- ==========================================================
-- GRÁFICOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS dashboard.charts (

    id SERIAL PRIMARY KEY,

    uuid UUID DEFAULT gen_random_uuid(),

    dashboard_id INTEGER NOT NULL,

    code VARCHAR(30),

    title VARCHAR(200),

    chart_type VARCHAR(50),

    sql_view VARCHAR(150),

    position INTEGER,

    active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_charts_dashboard
        FOREIGN KEY (dashboard_id)
        REFERENCES dashboard.dashboards(id)

);

COMMENT ON TABLE dashboard.charts IS
'Gráficos do Dashboard';


-- ==========================================================
-- FILTROS
-- ==========================================================

CREATE TABLE IF NOT EXISTS dashboard.filters (

    id SERIAL PRIMARY KEY,

    uuid UUID DEFAULT gen_random_uuid(),

    dashboard_id INTEGER NOT NULL,

    filter_name VARCHAR(100),

    filter_type VARCHAR(50),

    source_table VARCHAR(150),

    source_field VARCHAR(150),

    active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_filters_dashboard
        FOREIGN KEY (dashboard_id)
        REFERENCES dashboard.dashboards(id)

);

COMMENT ON TABLE dashboard.filters IS
'Filtros dos Dashboards';

-- ==========================================================
-- IA
-- ==========================================================

-- ==========================================================
-- AGENTES
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.ai_agents (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(200) NOT NULL,

    specialty           VARCHAR(150),

    description         TEXT,

    model_name          VARCHAR(100),

    version             VARCHAR(20) DEFAULT '1.0',

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE knowledge.ai_agents IS
'Cadastro dos Agentes Especialistas do SIGFA';


-- ==========================================================
-- MEMÓRIA DOS AGENTES
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.ai_memories (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    agent_id            INTEGER NOT NULL,

    context             TEXT,

    source_type         VARCHAR(50),

    source_code         VARCHAR(30),

    confidence          NUMERIC(5,2),

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_memory_agent
        FOREIGN KEY (agent_id)
        REFERENCES knowledge.ai_agents(id)

);

COMMENT ON TABLE knowledge.ai_memories IS
'Memória utilizada pelos agentes';


-- ==========================================================
-- REGRAS DE IA
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.ai_rules (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    code                VARCHAR(30) UNIQUE,

    title               VARCHAR(250),

    condition           TEXT,

    action              TEXT,

    priority            INTEGER,

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE knowledge.ai_rules IS
'Regras de decisão da IA';


-- ==========================================================
-- PROMPTS
-- ==========================================================

CREATE TABLE IF NOT EXISTS knowledge.ai_prompts (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    agent_id            INTEGER,

    title               VARCHAR(250),

    prompt              TEXT,

    version             VARCHAR(20),

    active              BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_prompt_agent
        FOREIGN KEY (agent_id)
        REFERENCES knowledge.ai_agents(id)

);

COMMENT ON TABLE knowledge.ai_prompts IS
'Prompts oficiais dos Agentes';


-- ==========================================================
-- HISTÓRICO DE RECOMENDAÇÕES
-- ==========================================================

CREATE TABLE IF NOT EXISTS diagnosis.ai_recommendations (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    diagnosis_id        INTEGER NOT NULL,

    agent_code          VARCHAR(30),

    recommendation      TEXT,

    confidence          NUMERIC(5,2),

    accepted            BOOLEAN,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_ai_recommendation
        FOREIGN KEY (diagnosis_id)
        REFERENCES diagnosis.diagnoses(id)

);

COMMENT ON TABLE diagnosis.ai_recommendations IS
'Recomendações geradas pela IA';

-- ==========================================================
-- AUDITORIA
-- ==========================================================

CREATE TABLE IF NOT EXISTS logs.audit_logs (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    user_id             INTEGER,

    module              VARCHAR(100),

    action              VARCHAR(100),

    table_name          VARCHAR(100),

    record_id           INTEGER,

    old_data            JSONB,

    new_data            JSONB,

    ip_address          VARCHAR(50),

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE logs.audit_logs IS
'Auditoria das alterações realizadas no sistema';


-- ==========================================================
-- LOG DE APIs
-- ==========================================================

CREATE TABLE IF NOT EXISTS logs.api_logs (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    endpoint            VARCHAR(255),

    method              VARCHAR(20),

    status_code         INTEGER,

    execution_time_ms   NUMERIC(10,2),

    user_id             INTEGER,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE logs.api_logs IS
'Registro das chamadas das APIs';


-- ==========================================================
-- LOG DOS AGENTES IA
-- ==========================================================

CREATE TABLE IF NOT EXISTS logs.ai_logs (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    agent_code          VARCHAR(30),

    diagnosis_id        INTEGER,

    prompt              TEXT,

    response            TEXT,

    tokens              INTEGER,

    execution_time_ms   NUMERIC(10,2),

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE logs.ai_logs IS
'Histórico das interações dos agentes inteligentes';


-- ==========================================================
-- NOTIFICAÇÕES
-- ==========================================================

CREATE TABLE IF NOT EXISTS logs.notifications (

    id                  SERIAL PRIMARY KEY,

    uuid                UUID DEFAULT gen_random_uuid(),

    company_id          INTEGER,

    title               VARCHAR(250),

    message             TEXT,

    notification_type   VARCHAR(50),

    readed              BOOLEAN DEFAULT FALSE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_notification_company
        FOREIGN KEY (company_id)
        REFERENCES sigfa.company(id)

);

COMMENT ON TABLE logs.notifications IS
'Notificações do sistema';

