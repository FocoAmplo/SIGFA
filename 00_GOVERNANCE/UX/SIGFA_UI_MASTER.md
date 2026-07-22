\# SIGFA\_UI\_MASTER.md

\> Documento Mestre da Interface Oficial do SIGFA 1.0  
\>  
\> Status: OFICIAL  
\>  
\> Local:  
\> 00\_GOVERNANCE/UX/SIGFA\_UI\_MASTER.md  
\>  
\> Versão: 1.0  
\>  
\> Classificação: Documento Mestre de Arquitetura de Interface (UI/UX)  
\>  
\> Aplicação: Obrigatória para todo desenvolvimento Frontend, Backend, IA, Agentes, ChatGPT, Codex e futuros colaboradores.

\---

\# 1\. OBJETIVO

Este documento define oficialmente toda a arquitetura visual, estrutural e funcional da interface do SIGFA.

Seu objetivo é impedir divergências entre desenvolvedores, inteligências artificiais, agentes autônomos e futuras evoluções da plataforma.

Nenhuma alteração estrutural da interface poderá ser realizada sem atualização deste documento.

Este documento possui prioridade superior sobre sugestões de layout geradas durante conversas individuais.

\---

\# 2\. PROPÓSITO DO SIGFA

O SIGFA NÃO é um chatbot.

O SIGFA é uma Plataforma Corporativa Inteligente de Consultoria Estratégica Empresarial.

A Inteligência Artificial representa apenas um dos motores da plataforma.

Sua função é interpretar dados empresariais, produzir conhecimento estratégico, apoiar decisões e alimentar continuamente toda a base cognitiva da empresa.

Toda informação recebida transforma-se em patrimônio intelectual permanente da organização.

Nenhum dado processado deverá ser descartado.

\---

\# 3\. PRINCÍPIOS DE DESIGN

Toda interface deverá seguir obrigatoriamente os seguintes princípios.

• Simplicidade

Eliminar elementos desnecessários.

•

Clareza

Cada componente possui apenas uma responsabilidade.

•

Foco

O usuário deve concentrar sua atenção na análise empresarial.

•

Profissionalismo

Interface corporativa de alto padrão.

•

Escalabilidade

Todos os módulos devem permitir crescimento sem alteração da arquitetura.

•

Consistência

Todos os componentes seguem o mesmo Design System.

•

Dados Reais

O Frontend nunca cria informações.

Toda informação exibida deve possuir origem no Backend.

\---

\# 4\. CONCEITO DA PLATAFORMA

Fluxo Oficial

Empresa

↓

Centro de Inteligência

↓

IA Estratégica

↓

PostgreSQL

↓

Base Cognitiva

↓

Diagnósticos

↓

Indicadores

↓

Especialistas

↓

Dashboard Executivo

↓

Planos de Ação

↓

Histórico Corporativo

\---

\# 5\. ARQUITETURA OFICIAL DA HOME

A Página Inicial da Plataforma é o Centro de Inteligência.

Não existe outra página inicial.

O Centro de Inteligência representa o núcleo operacional do SIGFA.

Sua função é receber informações, interpretar dados e iniciar todo o processamento estratégico.

\---

\# 6\. COMPONENTES DA HOME

A Home será composta exclusivamente pelos seguintes elementos.

\#\# TopBar

Responsável por:

• Logo SIGFA

• Nome da Plataforma

• Status da IA

• Usuário Logado

• Notificações

Não possuirá:

Pesquisa

Duplicação de logotipo

Menus redundantes

Informações repetidas

\---

\#\# Sidebar

Menu Oficial

Dashboard Executivo

Empresas

Documentos

Diagnósticos

Planos de Ação

Relatórios

Configurações

O item "Centro de Inteligência" NÃO EXISTE.

O Dashboard Inicial já representa o Centro de Inteligência.

\---

\#\# Centro de Inteligência

Elemento principal da plataforma.

Contém apenas:

Título

Campo de Conversação

Upload de Arquivos

Botão Enviar

Histórico da Conversa

Streaming da IA

Nada além disso.

\---

\#\# Campo de Conversação

Inspirado na experiência do ChatGPT.

Características:

Altura inicial reduzida.

Expansão automática conforme o usuário escreve.

Sem ocupar grande espaço vertical.

Sem barras desnecessárias.

Upload realizado através do ícone de clips.

Botão enviar minimalista.

\---

\#\# Histórico

Toda conversa permanece registrada.

Mensagens do usuário.

Mensagens da IA.

Streaming em tempo real.

Persistência obrigatória.

\---

\# 7\. PAINEL EXECUTIVO RESUMIDO

Localização:

Lateral Direita.

Função:

Representar o estado atual da empresa.

Não possui botões.

Não possui formulários.

Não possui textos extensos.

Exibe apenas indicadores resumidos.

Saúde Geral

Financeiro

Comercial

Produção

Qualidade

RH

Documentos

Alertas

Última Atualização

Todos os dados são provenientes exclusivamente do Backend.

\---

\# 8\. CONSOLE OPERACIONAL

Localização:

Rodapé fixo.

Função:

Exibir todos os eventos operacionais da plataforma.

Formato:

Horizontal.

Nunca vertical.

As mensagens aparecem continuamente.

Exemplo

18:42 Documento recebido ► IA iniciou processamento ► Indicadores atualizados ► Dashboard sincronizado ► Plano de ação criado ► Novo alerta financeiro ► ...

O Console Operacional representa o log em tempo real da plataforma.

\---

\# 9\. DASHBOARD EXECUTIVO

O Dashboard Executivo NÃO pertence à Home.

Representa um módulo independente.

Possui ambiente próprio.

Seu objetivo é realizar análises completas.

Contém:

Financeiro

Fluxo de Caixa

Lucro

EBITDA

Compras

Fornecedores

Produção

Logística

Qualidade

RH

Estoque

OEE

Indicadores

Timeline

BI

Gráficos Avançados

Relatórios

O Dashboard Executivo somente exibe dados processados anteriormente pelo Centro de Inteligência.

\---

\# 10\. ARQUITETURA DE PROCESSAMENTO

Fluxo Oficial

Usuário

↓

Centro de Inteligência

↓

Upload

↓

FastAPI

↓

Gemini

↓

JSON Estruturado

↓

Validação

↓

PostgreSQL

↓

Store

↓

Atualização Automática

↓

Painel Executivo

↓

Dashboard

↓

Especialistas

↓

Console Operacional

↓

Histórico

\---

\# 11\. JSON OFICIAL

Toda resposta da IA deverá possuir estrutura padronizada.

Exemplo:

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

Nenhuma resposta textual isolada deverá alimentar diretamente a interface.

\---

\# 12\. BANCO DE DADOS

Banco Oficial

PostgreSQL

Gerenciado através do DBeaver.

Toda interação deverá ser persistida.

Toda resposta da IA torna-se patrimônio permanente da empresa.

Jamais descartar informações estratégicas.

\---

\# 13\. STORE OFICIAL

Arquivo Oficial

frontend/src/store/intelligence.store.js

Responsabilidades

Conversation

Company

Documents

Diagnosis

Knowledge

Indicators

Dashboard

Charts

Recommendations

Action Plan

Alerts

Timeline

Logs

Loading

Todo conteúdo da Store deverá possuir origem no Backend.

\---

\# 14\. DIRETRIZES DE DESENVOLVIMENTO

É proibido:

Criar novos componentes sem necessidade.

Duplicar componentes.

Alterar nomes de arquivos.

Alterar arquitetura congelada.

Criar indicadores fictícios.

Gerar informações diretamente no Frontend.

Criar novos layouts sem atualização deste documento.

É obrigatório:

Reutilizar componentes existentes.

Persistir todos os dados.

Atualizar automaticamente a Store.

Utilizar JSON estruturado.

Atualizar o Console Operacional.

Atualizar os Indicadores.

Atualizar os Especialistas.

Atualizar os Gráficos.

Atualizar o Dashboard Executivo.

\---

\# 15\. ESTADO "PLATAFORMA VIVA"

O SIGFA será considerado operacional quando atender simultaneamente aos seguintes critérios.

Receber documentos.

Interpretar documentos.

Processar dados.

Persistir informações.

Atualizar PostgreSQL.

Atualizar Store.

Atualizar Indicadores.

Atualizar Gráficos.

Atualizar Alertas.

Atualizar Dashboard Executivo.

Atualizar Especialistas.

Atualizar Console Operacional.

Gerar Plano de Ação.

Gerar Diagnóstico.

Gerar Histórico Corporativo.

\---

\# 16\. COMPATIBILIDADE

Este documento deverá ser utilizado por:

Desenvolvedores

Arquitetos de Software

ChatGPT

Codex

Agentes Autônomos

Ferramentas de IA

Equipe SIGFA

Consultores Foco Amplo

Parceiros Tecnológicos

\---

\# 17\. VERSIONAMENTO

Versão Atual

1.0

Status

Congelado

Alterações somente mediante atualização oficial deste documento.

\---

\# 18\. CONSIDERAÇÕES FINAIS

O objetivo do SIGFA não é oferecer uma interface semelhante a um chatbot tradicional.

O objetivo do SIGFA é constituir uma Plataforma Corporativa Inteligente, capaz de transformar dados empresariais em conhecimento estratégico permanente, alimentando continuamente toda a estrutura de gestão da empresa através de Inteligência Artificial, Base Cognitiva, Diagnósticos, Indicadores, Especialistas e Dashboard Executivo.

Este documento representa a referência oficial para toda evolução da interface do SIGFA 1.0.  
