\# AI\_CONTEXT\_SIGFA\_1.0

Versão: 1.0  
Status: Ativo  
Projeto: SIGFA – Sistema Integrado de Gestão Foco Amplo

\---

\# Objetivo

Este documento representa o contexto permanente do desenvolvimento do SIGFA 1.0.

Seu objetivo é permitir que qualquer IA ou desenvolvedor continue o projeto exatamente do ponto onde ele foi interrompido.

Este documento deve ser considerado leitura obrigatória antes de qualquer alteração no código.

\---

\# Estado Atual

Arquitetura congelada.

Frontend funcional.

Backend funcional.

Banco estruturado.

CRUD concluído.

Swagger operacional.

Health Check operacional.

Dashboard operacional.

Centro de Inteligência operacional.

Login operacional.

JWT operacional.

Store implementada.

Comunicação Frontend → Backend implementada.

Endpoint /ai/chat implementado.

Atualmente a IA responde utilizando Mock.

\---

\# Próxima Etapa

Integrar o Gemini.

Substituir Mock.

Retornar JSON estruturado.

Atualizar Store.

Atualizar Dashboard.

\---

\# Arquitetura

A arquitetura do SIGFA está congelada.

Não alterar:

\- nomes de pastas  
\- nomes de arquivos  
\- Models  
\- Schemas  
\- APIs  
\- estrutura do banco

Qualquer evolução deverá ser incremental.

\---

\# Objetivo da IA

A IA representa o Consultor Inteligente Corporativo do SIGFA.

Ela deverá:

\- interpretar documentos  
\- responder perguntas  
\- gerar diagnósticos  
\- identificar riscos  
\- sugerir indicadores  
\- montar plano de ação  
\- alimentar dashboards

Nunca responder apenas texto livre.

Sempre gerar JSON estruturado compatível com o Frontend.

\---

\# Fluxo Oficial

Frontend

↓

POST /ai/chat

↓

api/ai.py

↓

services/ai\_service.py

↓

Gemini

↓

JSON estruturado

↓

Store

↓

Dashboard

↓

Especialista

↓

Plano de ação

↓

Chat

\---

\# Sprint Atual

Sprint 4.2

Objetivo:

Conectar a API Gemini preservando toda a arquitetura existente.

Nenhuma refatoração arquitetural deverá ser realizada.  
