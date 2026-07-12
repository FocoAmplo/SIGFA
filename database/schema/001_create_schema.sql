-- ==========================================================
-- SIGFA PLATFORM
-- Arquivo: 001_create_schema.sql
-- Objetivo: Criação dos Schemas do Sistema
-- Versão: 1.0
-- ==========================================================

CREATE SCHEMA IF NOT EXISTS sigfa;

CREATE SCHEMA IF NOT EXISTS knowledge;

CREATE SCHEMA IF NOT EXISTS diagnosis;

CREATE SCHEMA IF NOT EXISTS dashboard;

CREATE SCHEMA IF NOT EXISTS security;

CREATE SCHEMA IF NOT EXISTS logs;

COMMENT ON SCHEMA sigfa IS 'Schema principal do SIGFA';

COMMENT ON SCHEMA knowledge IS 'Base Cognitiva';

COMMENT ON SCHEMA diagnosis IS 'Diagnósticos';

COMMENT ON SCHEMA dashboard IS 'Dashboards';

COMMENT ON SCHEMA security IS 'Usuários e Segurança';

COMMENT ON SCHEMA logs IS 'Logs do sistema';