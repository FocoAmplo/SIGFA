-- ==========================================================
-- SIGFA PLATFORM
-- Módulo: Database
-- Arquivo: 007_seed_reference.sql
-- Versão: 1.0.0
-- Objetivo:
-- Dados iniciais do sistema
-- ==========================================================

-------------------------------------------------------------
-- PERFIS
-------------------------------------------------------------

INSERT INTO security.profiles
(name, description)

VALUES

('Administrador','Acesso total ao sistema'),

('Consultor','Consultor responsável pelos diagnósticos'),

('Gestor','Gestor da empresa');

-------------------------------------------------------------
-- PERMISSÕES
-------------------------------------------------------------

INSERT INTO security.permissions
(code,name,module)

VALUES

('ADM','Administrador','CORE'),

('DIA','Diagnósticos','DIAGNOSIS'),

('KNW','Base Cognitiva','KNOWLEDGE'),

('DSH','Dashboard','DASHBOARD'),

('AI','Agentes IA','AI');

-------------------------------------------------------------
-- AGENTE PRINCIPAL
-------------------------------------------------------------

INSERT INTO knowledge.ai_agents

(

code,

name,

specialty,

description,

model_name

)

VALUES

(

'AI-SIG',

'Super Gerente',

'Gestão Empresarial',

'Agente especialista responsável por orientar empresários utilizando toda a Base Cognitiva do SIGFA.',

'OPENAI'

);

