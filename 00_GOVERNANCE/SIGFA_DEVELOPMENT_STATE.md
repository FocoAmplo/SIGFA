\# SIGFA\_DEVELOPMENT\_STATE.md

\> Estado Oficial de Desenvolvimento do SIGFA  
\>  
\> Local:  
\> 00\_GOVERNANCE/UX/SIGFA\_DEVELOPMENT\_STATE.md  
\>  
\> Versão: 1.0  
\>  
\> Status: ATIVO  
\>  
\> Última Atualização: 15/07/2026  
\>  
\> Responsável: Equipe SIGFA / IA

\---

\# 1\. OBJETIVO

Este documento registra o estado atual do desenvolvimento do SIGFA.

Seu objetivo é permitir que qualquer novo desenvolvedor, inteligência artificial, ChatGPT, Codex ou agente autônomo continue exatamente do ponto onde o desenvolvimento foi interrompido.

Este documento deve ser atualizado ao final de cada sessão de desenvolvimento.

\---

\# 2\. SITUAÇÃO GERAL DO PROJETO

Projeto:

SIGFA — Sistema Integrado de Gestão Foco Amplo

Versão Atual:

SIGFA 1.0

Objetivo da Versão:

Entrega do MVP Enterprise totalmente funcional.

Status Geral:

EM DESENVOLVIMENTO

Arquitetura:

CONGELADA

Não serão realizadas alterações arquiteturais durante o desenvolvimento da versão 1.0.

Todas as melhorias estruturais ficam reservadas para o SIGFA 2.0.

\---

\# 3\. OBJETIVO PRINCIPAL

Transformar o SIGFA em uma Plataforma Corporativa Inteligente.

A IA não será um chatbot.

A IA será o núcleo operacional da plataforma.

Todas as informações recebidas serão processadas, persistidas, organizadas e reutilizadas pela plataforma.

Toda resposta da IA torna-se patrimônio intelectual permanente da empresa.

\---

\# 4\. TECNOLOGIAS OFICIAIS

Frontend

JavaScript ES6

Vite

CSS Modular

Design System próprio

Sem React

Sem Vue

Sem Angular

Backend

Python

FastAPI

SQLAlchemy

Pydantic

JWT

Banco

PostgreSQL (Produção)

SQLite (Apenas Desenvolvimento Local)

Banco gerenciado pelo DBeaver.

IA

Google Gemini

SDK google-genai

python-dotenv

API Key configurada

Cliente oficial funcionando

\---

\# 5\. SITUAÇÃO ATUAL

Frontend

✓ Login

✓ Dashboard Base

✓ Sidebar

✓ TopBar

✓ Centro de Inteligência

✓ Store

✓ Comunicação Frontend → Backend

Backend

✓ FastAPI

✓ Swagger

✓ Health

✓ Models

✓ Schemas

✓ Services

✓ CRUD

✓ JWT

✓ Upload de Arquivos

✓ Endpoint /ai/chat

Banco

✓ PostgreSQL conectado

✓ DBeaver conectado

✓ Estrutura criada

IA

✓ API Key configurada

✓ Cliente Gemini funcionando

✓ Comunicação validada

Ainda falta integrar totalmente ao fluxo da plataforma.

\---

\# 6\. ARQUITETURA CONGELADA

Não alterar:

Nomes de Pastas

Nomes de Arquivos

Models

Schemas

Services

APIs

Fluxo Frontend

Fluxo Backend

Estrutura PostgreSQL

Qualquer alteração deverá ser incremental.

\---

\# 7\. ARQUIVOS MAIS IMPORTANTES

Frontend

frontend/src/store/intelligence.store.js

frontend/src/services/intelligenceApi.js

frontend/src/scripts/intelligenceController.js

frontend/src/components/dashboard/AIHero.js

frontend/src/components/common/DynamicWorkspace.js

frontend/src/components/dashboard/KPIOverview.js

frontend/src/components/panels/SpecialistCard.js

frontend/src/pages/DashboardPage.js

Backend

backend/app/main.py

backend/app/api/ai.py

backend/app/services/ai\_service.py

backend/app/services/document\_analysis.py

backend/app/models/

backend/app/schemas/

backend/app/services/

Governança

00\_GOVERNANCE/UX/SIGFA\_UI\_MASTER.md

00\_GOVERNANCE/UX/SIGFA\_DEVELOPMENT\_STATE.md

\---

\# 8\. FLUXO FUNCIONAL DEFINITIVO

Usuário

↓

Centro de Inteligência

↓

Pergunta

ou

Upload

↓

FastAPI

↓

Gemini

↓

JSON Estruturado

↓

Persistência PostgreSQL

↓

Atualização da Store

↓

Painel Direito

↓

Console Operacional

↓

Dashboard Executivo

↓

Histórico

\---

\# 9\. FUNCIONAMENTO DA IA

A IA não responde apenas texto.

Ela produz conhecimento estruturado.

Toda resposta deverá gerar:

Diagnóstico

Indicadores

Alertas

Plano de Ação

Recomendações

Especialista

Histórico

Dashboard

Console

Conhecimento

Todos esses elementos serão persistidos.

\---

\# 10\. JSON OFICIAL

Toda resposta da IA deverá seguir a estrutura:

{  
    "company": {},  
    "documents": \[\],  
    "diagnosis": {},  
    "knowledge": {},  
    "indicators": \[\],  
    "charts": \[\],  
    "alerts": \[\],  
    "recommendations": \[\],  
    "action\_plan": \[\],  
    "dashboard": {},  
    "timeline": \[\],  
    "logs": \[\]  
}

Nenhuma informação deverá ser gerada diretamente pelo Frontend.

\---

\# 11\. CENTRO DE INTELIGÊNCIA

Representa a Home da plataforma.

Não existe menu chamado Centro de Inteligência.

Ao entrar no SIGFA o usuário já está nele.

Funções:

Receber perguntas.

Receber documentos.

Conversar.

Exibir histórico.

Exibir processamento.

Atualizar indicadores.

Atualizar console.

\---

\# 12\. DASHBOARD EXECUTIVO

Página independente.

Não pertence à Home.

Contém:

Financeiro

Produção

RH

Qualidade

Comercial

Compras

Fornecedores

Estoque

Logística

Fluxo de Caixa

Lucro

EBITDA

OEE

KPIs

BI

Relatórios

Todos os dados são provenientes da Base Cognitiva.

\---

\# 13\. PAINEL DIREITO

Representa o pulso da empresa.

Nunca conterá textos extensos.

Nunca possuirá botões.

Nunca possuirá formulários.

Exibe apenas:

Saúde Geral

Financeiro

Produção

Qualidade

Comercial

RH

Alertas

Documentos

Última Atualização

\---

\# 14\. CONSOLE OPERACIONAL

Localização

Rodapé.

Formato

Horizontal.

Mensagens contínuas.

Exemplo

18:32 Documento recebido ► IA iniciou análise ► Fluxo de Caixa atualizado ► Dashboard sincronizado ► Novo alerta ► Plano de ação criado ► ...

Todas as mensagens são geradas automaticamente pelo Backend.

\---

\# 15\. STORE

Arquivo Oficial

frontend/src/store/intelligence.store.js

Estado Atual

loading

conversation

company

diagnosis

dashboard

indicators

charts

recommendations

actionPlan

alerts

specialist

A evolução prevista inclui:

documents

knowledge

timeline

logs

\---

\# 16\. O QUE JÁ FOI CONCLUÍDO

Arquitetura congelada.

Frontend estruturado.

Backend estruturado.

Gemini conectado.

Store criada.

Centro de Inteligência criado.

Upload funcionando.

Comunicação Frontend → Backend funcionando.

Comunicação Backend → Gemini validada.

Banco PostgreSQL conectado.

\---

\# 17\. O QUE ESTÁ EM ANDAMENTO

Substituição da resposta simulada.

Integração completa do Gemini.

Persistência automática.

Atualização automática da Store.

Atualização automática da interface.

Console Operacional.

Painel Direito.

Dashboard Executivo.

\---

\# 18\. PRÓXIMA SPRINT

Sprint 4.2 — Plataforma Viva

Objetivo:

Transformar o Centro de Inteligência em um ambiente operacional.

Etapas:

1\.

Conectar definitivamente o endpoint /ai/chat ao ai\_service.py.

2\.

Eliminar build\_analysis() simulado.

3\.

Enviar contexto ao Gemini.

4\.

Receber JSON estruturado.

5\.

Persistir PostgreSQL.

6\.

Atualizar intelligence.store.js.

7\.

Atualizar Painel Direito.

8\.

Atualizar Console Operacional.

9\.

Preparar Dashboard Executivo.

\---

\# 19\. CRITÉRIO DE CONCLUSÃO DO SIGFA 1.0

O SIGFA será considerado operacional quando:

✓ Receber documentos.

✓ Interpretar documentos.

✓ Conversar com o usuário.

✓ Gerar diagnóstico.

✓ Persistir PostgreSQL.

✓ Atualizar Store.

✓ Atualizar Painel Direito.

✓ Atualizar Console Operacional.

✓ Atualizar Dashboard Executivo.

✓ Gerar Plano de Ação.

✓ Gerar Alertas.

✓ Construir Base Cognitiva.

✓ Manter Histórico Corporativo.

\---

\# 20\. REGRAS OBRIGATÓRIAS

Nunca alterar a arquitetura congelada.

Nunca renomear arquivos.

Nunca mover pastas.

Nunca criar dados fictícios no Frontend.

Toda informação deverá possuir origem no Backend.

Toda resposta da IA deverá ser persistida.

Toda atualização deverá refletir automaticamente na interface.

O SIGFA é uma Plataforma Corporativa Inteligente.

A IA representa apenas o motor da plataforma.

O conhecimento produzido pertence permanentemente à empresa.

\---

\# 21\. ORIENTAÇÃO PARA NOVOS CHATS

Antes de iniciar qualquer desenvolvimento, ler obrigatoriamente:

1\.

00\_GOVERNANCE/UX/SIGFA\_UI\_MASTER.md

2\.

00\_GOVERNANCE/UX/SIGFA\_DEVELOPMENT\_STATE.md

Somente após compreender completamente estes documentos o desenvolvimento poderá prosseguir.

Nenhuma sugestão deverá contrariar a arquitetura, os fluxos ou as decisões registradas nesses documentos.

Este documento representa o estado oficial do desenvolvimento do SIGFA 1.0.  
