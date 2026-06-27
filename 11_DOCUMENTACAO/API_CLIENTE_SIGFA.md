# API do Cliente SIGFA

Esta API permite que clientes enviem textos, documentos e evidencias para processamento pelo SIGFA.

## Autenticacao

Os endpoints de envio exigem o cabecalho:

```http
X-SIGFA-API-Key: sua-chave-segura
```

Observacao: esta e a camada inicial de seguranca para testes. Em producao, o ideal e evoluir para login real com usuario, senha, JWT/sessao e permissoes por cliente.

Em ambiente local, a chave pode ser definida antes de rodar a API:

```powershell
$env:SIGFA_API_KEY="troque-por-uma-chave-forte"
.\.venv\Scripts\python.exe -m uvicorn api.server:app --app-dir 13_ENGINE --reload --host 127.0.0.1 --port 8000
```

## Verificar autenticacao

```bash
curl -H "X-SIGFA-API-Key: sua-chave-segura" \
  http://127.0.0.1:8000/auth/me
```

## Solicitar acesso

Endpoint publico para pedido inicial de acesso:

```http
POST /cliente/acesso/solicitar
```

Payload:

```json
{
  "nome": "Maria Silva",
  "email": "maria@empresa.com.br",
  "empresa": "Empresa Exemplo",
  "mensagem": "Gostaria de acessar o portal SIGFA."
}
```

## Enviar texto

```bash
curl -X POST http://127.0.0.1:8000/cliente/envios/texto \
  -H "Content-Type: application/json" \
  -H "X-SIGFA-API-Key: sua-chave-segura" \
  -d "{\"empresa\":\"Empresa Exemplo\",\"contato\":\"Maria Silva\",\"titulo\":\"Problema operacional\",\"conteudo\":\"Estoque acima da capacidade operacional.\"}"
```

## Enviar arquivo

```bash
curl -X POST http://127.0.0.1:8000/cliente/envios/arquivo \
  -H "X-SIGFA-API-Key: sua-chave-segura" \
  -F "empresa=Empresa Exemplo" \
  -F "contato=Maria Silva" \
  -F "descricao=Relatorio e evidencias para diagnostico" \
  -F "arquivo=@relatorio.pdf"
```

Extensoes aceitas:

```text
.csv, .doc, .docx, .jpeg, .jpg, .pdf, .png, .txt, .xls, .xlsx
```

Limite inicial por arquivo:

```text
25 MB
```

## Local de armazenamento

Os envios sao registrados em:

```text
02_BANCO_DADOS/ENTRADAS_CLIENTES/{empresa}/
```

Cada arquivo enviado recebe um arquivo `.meta.txt` com dados de contato, descricao, tipo e tamanho.

## Portal web

A pagina estatica em `docs/` usa `docs/app.js` para chamar a API.

Por padrao:

```text
localhost/127.0.0.1 -> http://127.0.0.1:8000
demais dominios     -> https://api.focoamplo.com.br
```

Antes de publicar em producao, configure a API em `api.focoamplo.com.br` e defina `SIGFA_API_KEY` no ambiente do servidor.
