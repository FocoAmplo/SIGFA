\# SIGFA\_CODE\_STYLE — Padrão Oficial de Codificação da Plataforma SIGFA

| Campo | Informação |  
|--------|------------|  
| Documento | SIGFA\_CODE\_STYLE |  
| Título | Padrão Oficial de Codificação da Plataforma SIGFA |  
| Versão | 1.0 |  
| Status | BASELINE |  
| Classificação | Oficial |  
| Projeto | SIGFA – Sistema Integrado de Gestão Foco Amplo |  
| Proprietário | Foco Amplo Consultoria e Soluções Empresariais |  
| Documento Mestre | PD-000 |  
| Arquitetura | ARQ-001 |  
| Atualização | Somente mediante versionamento oficial da Governança |

\---

\# 1\. Objetivo

Estabelecer o padrão oficial de codificação da Plataforma SIGFA.

Este documento define as convenções que deverão ser utilizadas durante o desenvolvimento de todos os módulos da plataforma, garantindo uniformidade, legibilidade, manutenção, escalabilidade e integração entre equipes humanas e Inteligências Artificiais.

\---

\# 2\. Finalidade

Padronizar a escrita do código-fonte da plataforma.

Garantir que qualquer profissional ou agente de Inteligência Artificial consiga compreender, evoluir e manter o código de forma consistente.

\---

\# 3\. Escopo

Este documento aplica-se a:

\- Backend  
\- Frontend  
\- Engine SIGFA  
\- Banco de Conhecimento  
\- Scripts  
\- Testes  
\- Ferramentas internas  
\- Automações  
\- Inteligência Artificial

\---

\# 4\. Público-Alvo

Este documento destina-se a:

\- Desenvolvedores  
\- Arquitetos  
\- Equipe de QA  
\- DevOps  
\- Consultores Técnicos  
\- ChatGPT  
\- Codex  
\- Gemini  
\- Demais Inteligências Artificiais

\---

\# 5\. Princípios Gerais

Todo código desenvolvido para o SIGFA deverá seguir os seguintes princípios:

\- Clareza.  
\- Simplicidade.  
\- Legibilidade.  
\- Reutilização.  
\- Baixo acoplamento.  
\- Alta coesão.  
\- Responsabilidade única.  
\- Padronização.  
\- Evolução contínua.  
\- Documentação permanente.

\---

\# 6\. Convenções Gerais

Todo código deverá:

\- possuir nomenclatura consistente;  
\- evitar abreviações desnecessárias;  
\- possuir organização previsível;  
\- utilizar idioma único por contexto;  
\- seguir os padrões definidos neste documento.

\---

\# 7\. Idioma Oficial

\#\# Código

Utilizar inglês.

Exemplos:

\- User  
\- Company  
\- Dashboard  
\- Diagnosis  
\- Knowledge

\---

\#\# Documentação

Utilizar Português (Brasil).

Toda documentação oficial permanecerá em português até a internacionalização da plataforma.

\---

\#\# Interface

Preparada para internacionalização.

Nenhum texto deverá ser fixado diretamente no código quando houver mecanismo oficial de tradução.

\---

\# 8\. Convenções de Nomenclatura

\#\# Classes

Utilizar PascalCase.

Exemplos:

\`\`\`  
UserService  
CompanyRepository  
DiagnosisEngine  
KnowledgeManager  
\`\`\`

\---

\#\# Funções

Utilizar camelCase.

Exemplos:

\`\`\`  
createUser()  
calculateIndicators()  
generateDiagnosis()  
\`\`\`

\---

\#\# Variáveis

Utilizar camelCase.

Exemplos:

\`\`\`  
companyId  
currentUser  
dashboardData  
\`\`\`

\---

\#\# Constantes

Utilizar UPPER\_SNAKE\_CASE.

Exemplos:

\`\`\`  
MAX\_UPLOAD\_SIZE  
DEFAULT\_LANGUAGE  
TOKEN\_EXPIRATION  
\`\`\`

\---

\#\# Arquivos

Utilizar nomenclatura consistente.

Exemplos:

\`\`\`  
user\_service.py  
dashboard\_controller.py  
login\_page.js  
company\_repository.py  
\`\`\`

\---

\#\# Diretórios

Sempre em letras minúsculas.

Exemplo:

\`\`\`  
components  
services  
layouts  
database  
knowledge  
engine  
\`\`\`

\---

\# 9\. Organização do Código

Cada arquivo deverá possuir apenas uma responsabilidade principal.

Evitar arquivos excessivamente extensos.

Sempre que possível utilizar componentização e modularização.

\---

\# 10\. Organização das Funções

Cada função deverá:

\- executar apenas uma responsabilidade;  
\- possuir nome objetivo;  
\- evitar efeitos colaterais;  
\- retornar resultados previsíveis.

\---

\# 11\. Comentários

Comentários deverão explicar decisões.

Jamais explicar código óbvio.

Comentários desatualizados deverão ser removidos.

\---

\# 12\. Documentação

Toda funcionalidade relevante deverá possuir documentação correspondente.

A documentação faz parte da entrega.

\---

\# 13\. Tratamento de Erros

Todo erro deverá:

\- ser tratado;  
\- ser registrado;  
\- possuir mensagem compreensível;  
\- preservar segurança da aplicação.

Jamais ocultar erros silenciosamente.

\---

\# 14\. Logging

Logs deverão registrar apenas informações relevantes.

Evitar excesso de informações.

Nunca registrar:

\- senhas;  
\- tokens;  
\- informações confidenciais;  
\- dados sensíveis.

\---

\# 15\. Reutilização

Antes de criar qualquer código deverá ser verificado:

\- componente existente;  
\- serviço existente;  
\- utilitário existente;  
\- biblioteca oficial.

Duplicação deve ser evitada.

\---

\# 16\. Organização dos Imports

Imports deverão permanecer organizados.

Ordem recomendada:

\- bibliotecas padrão;  
\- bibliotecas externas;  
\- módulos internos;  
\- componentes locais.

\---

\# 17\. Inteligência Artificial

Código produzido por IA deverá:

\- seguir este documento;  
\- seguir o ARQ-001;  
\- seguir o SIGFA\_DEVELOPMENT\_GUIDE;  
\- seguir o COMPONENT\_REGISTRY;  
\- respeitar ADRs aprovados.

A IA nunca deverá criar estruturas paralelas à arquitetura oficial.

\---

\# 18\. Boas Práticas

Recomenda-se:

\- escrever código simples;  
\- evitar duplicação;  
\- criar funções pequenas;  
\- utilizar nomes descritivos;  
\- remover código morto;  
\- preservar organização dos diretórios;  
\- manter documentação atualizada.

\---

\# 19\. Fluxo de Utilização

Este documento deverá ser consultado:

\- antes do desenvolvimento;  
\- durante implementação;  
\- durante revisão de código;  
\- durante auditorias;  
\- durante onboarding.

\---

\# 20\. Responsabilidades

\#\# Arquitetura

Definir os padrões oficiais.

\---

\#\# Desenvolvimento

Aplicar integralmente este documento.

\---

\#\# QA

Validar conformidade.

\---

\#\# Inteligência Artificial

Gerar código aderente aos padrões oficiais.

\---

\# 21\. Relação com os Demais Documentos

Documento Mestre

\- PD-000

Arquitetura

\- ARQ-001

Desenvolvimento

\- SIGFA\_DEVELOPMENT\_GUIDE

Contexto

\- SIGFA\_CONTEXT

DNA

\- DNA

Componentes

\- COMPONENT\_REGISTRY

Decisões

\- ADR

Normas

\- SIGFA\_STANDARDS

\---

\# 22\. Dependências

Este documento depende de:

\- PD-000  
\- ARQ-001  
\- SIGFA\_DEVELOPMENT\_GUIDE  
\- COMPONENT\_REGISTRY  
\- ADR  
\- SIGFA\_CONTEXT

\---

\# 23\. Versionamento

Versão inicial:

1.0 — Baseline Oficial.

Alterações futuras deverão ocorrer mediante versionamento oficial ou ADR.

\---

\# 24\. Histórico de Alterações

\#\# Versão 1.0

\- Criação do documento.  
\- Definição do padrão oficial de codificação da Plataforma SIGFA.

\---

\# 25\. Observações Arquiteturais

Este documento possui caráter normativo.

Nenhum padrão de codificação poderá contrariar a Arquitetura Oficial da Plataforma, a Governança vigente ou qualquer ADR aprovado.

\---

\# 26\. Status

BASELINE 1.0

Documento Oficial.

\---

\# 27\. Próximos Documentos Relacionados

\- SIGFA\_STANDARDS  
\- COMPONENT\_REGISTRY  
\- ADR\_INDEX

