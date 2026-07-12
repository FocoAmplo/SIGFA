-- ==========================================================
-- SIGFA PLATFORM
-- Módulo: Database
-- Arquivo: 005_create_functions.sql
-- Versão: 1.0.0
-- Objetivo:
-- Funções utilizadas pelo Dashboard, Engine e APIs
-- ==========================================================

-------------------------------------------------------------
-- NOTA GERAL DA EMPRESA
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_company_score(
    p_company_id INTEGER
)

RETURNS NUMERIC
LANGUAGE plpgsql

AS $$

DECLARE

    v_score NUMERIC;

BEGIN

    SELECT ROUND(AVG(score),2)

    INTO v_score

    FROM diagnosis.diagnoses

    WHERE company_id = p_company_id;

    RETURN COALESCE(v_score,0);

END;

$$;

-------------------------------------------------------------
-- MATURIDADE DA EMPRESA
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_company_maturity(

    p_company_id INTEGER

)

RETURNS NUMERIC

LANGUAGE plpgsql

AS $$

DECLARE

    v_maturity NUMERIC;

BEGIN

    SELECT ROUND(AVG(maturity_level),2)

    INTO v_maturity

    FROM diagnosis.diagnoses

    WHERE company_id = p_company_id;

    RETURN COALESCE(v_maturity,0);

END;

$$;

-------------------------------------------------------------
-- TOTAL DE DIAGNÓSTICOS
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_total_diagnoses(

    p_company_id INTEGER

)

RETURNS INTEGER

LANGUAGE plpgsql

AS $$

DECLARE

    v_total INTEGER;

BEGIN

    SELECT COUNT(*)

    INTO v_total

    FROM diagnosis.diagnoses

    WHERE company_id = p_company_id;

    RETURN COALESCE(v_total,0);

END;

$$;

-------------------------------------------------------------
-- PROGRESSO DOS PLANOS
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_action_plan_progress(

    p_company_id INTEGER

)

RETURNS NUMERIC

LANGUAGE plpgsql

AS $$

DECLARE

    v_progress NUMERIC;

BEGIN

    SELECT ROUND(AVG(progress),2)

    INTO v_progress

    FROM diagnosis.action_plans ap

    INNER JOIN diagnosis.diagnoses d

        ON d.id = ap.diagnosis_id

    WHERE d.company_id = p_company_id;

    RETURN COALESCE(v_progress,0);

END;

$$;

-------------------------------------------------------------
-- ÚLTIMO DIAGNÓSTICO
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_last_diagnosis(

    p_company_id INTEGER

)

RETURNS TIMESTAMP

LANGUAGE plpgsql

AS $$

DECLARE

    v_date TIMESTAMP;

BEGIN

    SELECT MAX(created_at)

    INTO v_date

    FROM diagnosis.diagnoses

    WHERE company_id = p_company_id;

    RETURN v_date;

END;

$$;

-------------------------------------------------------------
-- AÇÕES PENDENTES
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_pending_actions(

    p_company_id INTEGER

)

RETURNS INTEGER

LANGUAGE plpgsql

AS $$

DECLARE

    v_total INTEGER;

BEGIN

    SELECT COUNT(*)

    INTO v_total

    FROM diagnosis.action_plans ap

    INNER JOIN diagnosis.diagnoses d

        ON d.id = ap.diagnosis_id

    WHERE d.company_id = p_company_id

    AND ap.status <> 'COMPLETED';

    RETURN COALESCE(v_total,0);

END;

$$;

-------------------------------------------------------------
-- TOTAL DE RISCOS
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_total_risks()

RETURNS INTEGER

LANGUAGE plpgsql

AS $$

DECLARE

    v_total INTEGER;

BEGIN

    SELECT COUNT(*)

    INTO v_total

    FROM knowledge.risks

    WHERE active = TRUE;

    RETURN COALESCE(v_total,0);

END;

$$;

-------------------------------------------------------------
-- TOTAL DE OMCS
-------------------------------------------------------------

CREATE OR REPLACE FUNCTION dashboard.fn_total_omcs()

RETURNS INTEGER

LANGUAGE plpgsql

AS $$

DECLARE

    v_total INTEGER;

BEGIN

    SELECT COUNT(*)

    INTO v_total

    FROM knowledge.omc

    WHERE active = TRUE;

    RETURN COALESCE(v_total,0);

END;

$$;

