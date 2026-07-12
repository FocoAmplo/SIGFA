-- ==========================================================
-- SIGFA PLATFORM
-- Módulo: Database
-- Arquivo: 004_create_views.sql
-- Versão: 1.0.0
-- Objetivo:
-- Views utilizadas pelos Dashboards e APIs
-- ==========================================================

-------------------------------------------------------------
-- RESUMO DAS EMPRESAS
-------------------------------------------------------------

CREATE OR REPLACE VIEW dashboard.vw_company_summary AS

SELECT

    c.id,

    c.uuid,

    c.corporate_name,

    c.segment,

    c.city,

    c.state,

    COUNT(DISTINCT d.id) AS total_diagnoses,

    COUNT(DISTINCT ap.id) AS total_action_plans,

    ROUND(AVG(d.score),2) AS average_score,

    ROUND(AVG(d.maturity_level),2) AS maturity

FROM sigfa.company c

LEFT JOIN diagnosis.diagnoses d

ON d.company_id = c.id

LEFT JOIN diagnosis.action_plans ap

ON ap.diagnosis_id = d.id

GROUP BY

c.id,

c.uuid,

c.corporate_name,

c.segment,

c.city,

c.state;

-------------------------------------------------------------
-- RESUMO DOS KPIs
-------------------------------------------------------------

CREATE OR REPLACE VIEW dashboard.vw_kpi_summary AS

SELECT

    d.company_id,

    s.indicator_code,

    COUNT(s.id)                         AS total_records,

    ROUND(AVG(s.value),2)               AS average_value,

    MIN(s.value)                        AS minimum_value,

    MAX(s.value)                        AS maximum_value

FROM diagnosis.scores s

INNER JOIN diagnosis.diagnoses d

ON d.id = s.diagnosis_id

GROUP BY

d.company_id,

s.indicator_code;