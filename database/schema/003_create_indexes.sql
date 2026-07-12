-- ==========================================================
-- SIGFA PLATFORM
-- Módulo: Database
-- Arquivo: 003_create_indexes.sql
-- Versão: 1.0.0
-- Objetivo:
-- Índices para otimização das consultas
-- ==========================================================

-------------------------------------------------------------
-- CORE
-------------------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_company_uuid
ON sigfa.company(uuid);

CREATE INDEX IF NOT EXISTS idx_company_cnpj
ON sigfa.company(cnpj);

CREATE INDEX IF NOT EXISTS idx_company_name
ON sigfa.company(corporate_name);

CREATE INDEX IF NOT EXISTS idx_users_email
ON security.users(email);

CREATE INDEX IF NOT EXISTS idx_users_company
ON security.users(company_id);

-------------------------------------------------------------
-- KNOWLEDGE
-------------------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_omc_code
ON knowledge.omc(code);

CREATE INDEX IF NOT EXISTS idx_concepts_code
ON knowledge.concepts(code);

CREATE INDEX IF NOT EXISTS idx_concepts_name
ON knowledge.concepts(name);

CREATE INDEX IF NOT EXISTS idx_methods_code
ON knowledge.methods(code);

CREATE INDEX IF NOT EXISTS idx_tools_code
ON knowledge.tools(code);

CREATE INDEX IF NOT EXISTS idx_kpis_code
ON knowledge.kpis(code);

CREATE INDEX IF NOT EXISTS idx_questions_code
ON knowledge.questions(code);

CREATE INDEX IF NOT EXISTS idx_risks_code
ON knowledge.risks(code);

CREATE INDEX IF NOT EXISTS idx_recommendations_code
ON knowledge.recommendations(code);

-------------------------------------------------------------
-- DIAGNOSIS
-------------------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_diagnosis_company
ON diagnosis.diagnoses(company_id);

CREATE INDEX IF NOT EXISTS idx_answers_diagnosis
ON diagnosis.answers(diagnosis_id);

CREATE INDEX IF NOT EXISTS idx_scores_diagnosis
ON diagnosis.scores(diagnosis_id);

CREATE INDEX IF NOT EXISTS idx_actionplans_diagnosis
ON diagnosis.action_plans(diagnosis_id);

-------------------------------------------------------------
-- IA
-------------------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_agents_code
ON knowledge.ai_agents(code);

CREATE INDEX IF NOT EXISTS idx_ai_rules_code
ON knowledge.ai_rules(code);

-------------------------------------------------------------
-- LOGS
-------------------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_api_logs_date
ON logs.api_logs(created_at);

CREATE INDEX IF NOT EXISTS idx_ai_logs_date
ON logs.ai_logs(created_at);

CREATE INDEX IF NOT EXISTS idx_audit_logs_date
ON logs.audit_logs(created_at);