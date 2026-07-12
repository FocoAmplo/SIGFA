\# SIGFA Architecture Guide

\*\*Versão:\*\* 1.0 Baseline

\*\*Projeto:\*\* SIGFA – Sistema Integrado de Gestão Foco Amplo

\*\*Empresa:\*\* Foco Amplo

\*\*Status:\*\* Documento Oficial de Arquitetura

\---

\# 1\. Objetivo

Este documento estabelece os padrões oficiais de arquitetura do SIGFA.

Todo novo módulo, serviço, API ou componente deverá seguir obrigatoriamente estas diretrizes.

Este documento é a referência principal para:

\- Desenvolvimento  
\- Inteligência Artificial (Codex)  
\- ChatGPT  
\- Novos desenvolvedores  
\- Manutenção  
\- Evolução do SIGFA 2.0

\---

\# 2\. Filosofia do Projeto

O SIGFA não é apenas um ERP.

É uma Plataforma Inteligente de Diagnóstico, Gestão e Consultoria Empresarial baseada em Inteligência Artificial.

Sua missão é transformar informações empresariais em decisões estratégicas.

\---

\# 3\. Objetivo do SIGFA 1.0

Validar o produto com cinco clientes reais.

Demonstrar valor através de um fluxo completo:

Empresa

↓

Documentos

↓

Diagnóstico

↓

Indicadores

↓

Plano de Ação

↓

Dashboard

↓

Centro de Inteligência

↓

Consultoria

\---

\# 4\. Modelo de Negócio

O SIGFA possui três modalidades comerciais.

\#\# Plataforma

Cliente utiliza apenas o sistema.

\#\# Plataforma \+ Consultoria

Cliente utiliza o sistema juntamente com consultores da Foco Amplo.

\#\# Gestão Continuada

Contrato anual de acompanhamento estratégico utilizando o SIGFA como plataforma principal.

\---

\# 5\. Princípios Arquiteturais

Sempre utilizar:

Model

↓

Schema

↓

Service

↓

API

↓

Frontend

Toda regra de negócio permanece no Service.

Routers nunca implementam regras.

Models representam a verdade do banco.

Schemas representam contratos.

Services representam regras de negócio.

\---

\# 6\. Estrutura Oficial

backend/

app/

models/

schemas/

services/

api/

auth/

database/

storage/

knowledge/

diagnosis/

dashboard/

audit/

i18n/

frontend/

src/

components/

pages/

layouts/

services/

store/

theme/

locales/

\---

\# 7\. Framework Interno SIGFA

O projeto utiliza o Framework Interno SIGFA.

Core

Authentication

Database

Storage

Knowledge

Diagnosis

Dashboard

AI

Documents

Security

Audit

Internationalization

Utilities

Todos os módulos devem seguir o mesmo padrão.

\---

\# 8\. Banco de Dados

Banco oficial:

PostgreSQL

ORM:

SQLAlchemy

Migrações:

Alembic (SIGFA 2.0)

Todos os Models devem possuir:

UUID

created\_at

updated\_at

active (quando aplicável)

Relacionamentos explícitos

\---

\# 9\. Convenções

Models

PascalCase

User

Company

Diagnosis

Schemas

Mesmo nome do Model

UserCreate

UserUpdate

UserResponse

Services

Nome\_do\_Model \+ Service

UserService

CompanyService

DiagnosisService

APIs

Mesmo padrão

/user

/company

/diagnosis

/dashboard

\---

\# 10\. Fluxo Oficial

Model

↓

Schema

↓

Service

↓

API

↓

Validation

↓

Commit

Nunca inverter essa ordem.

\---

\# 11\. Internacionalização

Toda a plataforma será preparada para múltiplos idiomas.

Idiomas previstos:

Português

Inglês

Espanhol

Francês

Alemão

Italiano

A estrutura será implementada ainda no SIGFA 1.0.

\---

\# 12\. Inteligência Artificial

O Gemini será utilizado como mecanismo de IA.

O SIGFA será responsável por:

Orquestração

Especialistas

Memória

Prompt Engineering

Conhecimento

Plano de ação

A IA nunca acessará diretamente o banco.

Toda comunicação ocorrerá através dos Services.

\---

\# 13\. Centro de Inteligência

É o núcleo da plataforma.

Responsável por:

Diagnóstico

Especialistas

Indicadores

Plano de ação

Recomendações

Análises

Consultoria

\---

\# 14\. Segurança

JWT

Refresh Token

Hash de senha

Auditoria

Logs

Permissões

Multiempresa

\---

\# 15\. Critérios de Conclusão de Sprint

Uma Sprint somente é considerada concluída quando:

✓ Models compilam

✓ Schemas compilam

✓ Services compilam

✓ APIs compilam

✓ App inicia

✓ Validação automática executada

✓ Relatório emitido

✓ Commit realizado

\---

\# 16\. Fluxo de Desenvolvimento

ChatGPT

↓

Planejamento

↓

Codex

↓

Implementação

↓

Validação

↓

Git

↓

GitHub

\---

\# 17\. Roadmap SIGFA 1.0

Sprint 01

Estrutura

Sprint 02

Models

Sprint 03

Authentication

Sprint 04

Diagnosis

Sprint 05

Dashboard

Sprint 06

Documents

Sprint 07

Knowledge

Sprint 08

AI

Sprint 09

Frontend

Sprint 10

Validação Piloto

\---

\# 18\. Roadmap SIGFA 2.0

Marketplace

Academy

Integrações ERP

CRM

Financeiro

OCR

Workflow

BI

Automação

Especialistas IA

Aplicativo Mobile

\---

\# 19\. Visão de Longo Prazo

O SIGFA será uma Plataforma Global de Inteligência Empresarial capaz de atender empresas de qualquer porte, em diferentes países e idiomas, integrando diagnóstico, gestão, consultoria e inteligência artificial em um único ecossistema.

\---

\# 20\. Documento Vivo

Este documento é a referência oficial da arquitetura do SIGFA.

Toda alteração estrutural deverá ser registrada antes da implementação.

\# Metodologia SIGFA

O SIGFA é composto por três camadas independentes e complementares:

\#\# Plataforma

Infraestrutura tecnológica responsável por coletar, organizar, processar e apresentar informações.

\#\# Metodologia

Conjunto estruturado de modelos, conceitos, indicadores, perguntas, diagnósticos, riscos, evidências, recomendações e planos de ação que orientam a análise empresarial.

\#\# Consultoria

Aplicação prática da metodologia por especialistas da Foco Amplo, apoiados pela Inteligência Artificial do SIGFA.

Essas três camadas devem permanecer desacopladas, permitindo que a plataforma evolua tecnologicamente sem comprometer a metodologia e que a metodologia evolua continuamente sem exigir alterações estruturais na plataforma.  
