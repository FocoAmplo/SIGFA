-- ==========================================================
-- SIGFA PLATFORM
-- Módulo: Database
-- Arquivo: 006_create_triggers.sql
-- Versão: 1.0.0
-- Objetivo:
-- Triggers automáticos do SIGFA
-- ==========================================================

-------------------------------------------------------------
-- FUNÇÃO PARA UPDATED_AT
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION sigfa.fn_update_timestamp()

RETURNS TRIGGER

LANGUAGE plpgsql

AS $$

BEGIN

    NEW.updated_at = CURRENT_TIMESTAMP;

    RETURN NEW;

END;

$$;

-------------------------------------------------------------
-- COMPANY
-------------------------------------------------------------

CREATE TRIGGER trg_company_updated

BEFORE UPDATE

ON sigfa.company

FOR EACH ROW

EXECUTE FUNCTION sigfa.fn_update_timestamp();



-------------------------------------------------------------
-- USERS
-------------------------------------------------------------

CREATE TRIGGER trg_users_updated

BEFORE UPDATE

ON security.users

FOR EACH ROW

EXECUTE FUNCTION sigfa.fn_update_timestamp();



-------------------------------------------------------------
-- DIAGNOSES
-------------------------------------------------------------

CREATE TRIGGER trg_diagnoses_updated

BEFORE UPDATE

ON diagnosis.diagnoses

FOR EACH ROW

EXECUTE FUNCTION sigfa.fn_update_timestamp();

