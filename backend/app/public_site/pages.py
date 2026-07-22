from fastapi.responses import HTMLResponse


PRIVACY_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="utf-8">

<title>Política de Privacidade - SIGFA</title>

<style>

body{

font-family:Arial;

max-width:900px;

margin:auto;

padding:40px;

line-height:1.7;

}

h1{

color:#14532d;

}

</style>

</head>

<body>

<h1>Política de Privacidade</h1>

<p>

O SIGFA coleta apenas as informações fornecidas voluntariamente pelos usuários durante o atendimento realizado pelo GPT Público.

</p>

<p>

Os dados poderão ser utilizados para:

</p>

<ul>

<li>qualificação comercial;</li>

<li>contato posterior;</li>

<li>elaboração de diagnósticos empresariais;</li>

<li>propostas comerciais;</li>

<li>melhoria dos serviços.</li>

</ul>

<p>

Nenhuma informação será comercializada ou compartilhada com terceiros sem autorização legal.

</p>

<p>

O usuário poderá solicitar alteração ou exclusão de seus dados a qualquer momento.

</p>

<p>

Controlador dos dados:

<b>SIGFA - Sistema Integrado de Gestão Foco Amplo</b>

</p>

</body>

</html>
"""


TERMS_HTML = """
<!DOCTYPE html>

<html lang="pt-br">

<head>

<meta charset="utf-8">

<title>Termos de Uso</title>

<style>

body{

font-family:Arial;

max-width:900px;

margin:auto;

padding:40px;

line-height:1.7;

}

</style>

</head>

<body>

<h1>Termos de Uso</h1>

<p>

O GPT Público do SIGFA possui finalidade exclusivamente consultiva e comercial.

</p>

<p>

As respostas geradas representam orientações iniciais e não substituem consultorias profissionais.

</p>

<p>

O usuário declara fornecer informações verdadeiras.

</p>

<p>

O SIGFA poderá utilizar os dados para contato comercial.

</p>

</body>

</html>
"""