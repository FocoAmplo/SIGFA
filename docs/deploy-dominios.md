# Deploy e domínios SIGFA

## Domínios propostos
- https://app.focoamplo.com.br/ → SIGFA
- https://diagnostico.focoamplo.com.br/ → Agente de IA / consultor
- https://focoamplo.com.br/ → site principal

## Configuração no GitHub
1. Crie um repositório no GitHub para o frontend.
2. Ative GitHub Pages na branch main ou gh-pages.
3. Use o domínio personalizado app.focoamplo.com.br para o SIGFA.
4. Para os demais domínios, repita a configuração em repositórios separados ou via GitHub Pages para cada projeto.

## Registro DNS
No provedor de DNS, crie os registros:
- app.focoamplo.com.br → CNAME → <usuario>.github.io
- diagnostico.focoamplo.com.br → CNAME → <usuario>.github.io
- focoamplo.com.br → A ou CNAME conforme a hospedagem do site principal

## Observação importante
O arquivo public/CNAME deve conter o domínio principal do projeto para o GitHub Pages.
Para o SIGFA, o valor atual é app.focoamplo.com.br.
