-- SIGFA 1.0 - Sprint de Integração Oficial
-- Extensão incremental: não altera nem remove estruturas existentes.

CREATE SCHEMA IF NOT EXISTS intelligence;

CREATE TABLE IF NOT EXISTS intelligence.documents (
    id              SERIAL PRIMARY KEY,
    uuid            UUID DEFAULT gen_random_uuid(),
    tenant_id       VARCHAR(120) NOT NULL,
    company_id      INTEGER NOT NULL REFERENCES sigfa.company(id),
    uploaded_by     INTEGER NOT NULL REFERENCES security.users(id),
    title           VARCHAR(180) NOT NULL,
    description     VARCHAR(500),
    filename        VARCHAR(255) NOT NULL,
    content_type    VARCHAR(120),
    content_hash    VARCHAR(128) NOT NULL,
    storage_bucket  VARCHAR(255) NOT NULL,
    storage_path    TEXT NOT NULL,
    status          VARCHAR(40) NOT NULL DEFAULT 'STORED',
    metadata        JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (tenant_id, content_hash)
);

CREATE INDEX IF NOT EXISTS idx_intelligence_documents_company
    ON intelligence.documents(company_id, created_at DESC);
