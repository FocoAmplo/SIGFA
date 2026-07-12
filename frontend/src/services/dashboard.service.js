export const EXECUTIVE_METRICS = [
    { title: 'Empresas', value: '24', detail: 'Contas corporativas ativas' },
    { title: 'Diagnósticos', value: '16', detail: 'Relatórios gerados este mês' },
    { title: 'Alertas', value: '7', detail: 'Intervenções recomendadas' },
    { title: 'Financeiro', value: 'R$ 4.9M', detail: 'Receita projetada 30 dias' }
];

export const INDICATOR_SUMMARY = [
    { label: 'SLA de Processos', value: '92%', status: 'Saudável' },
    { label: 'Adesão de Indicadores', value: '87%', status: 'Em ritmo' },
    { label: 'Ações em Aberto', value: '12', status: 'Atenção' }
];

export const DASHBOARD_CARDS = [
    {
        key: 'empresas',
        title: 'Empresas',
        description: 'Base de clientes corporativos com status atualizados.',
        highlight: '24 ativos',
        variant: 'info'
    },
    {
        key: 'diagnosticos',
        title: 'Diagnósticos',
        description: 'Casos analisados no último ciclo de entrega.',
        highlight: '16 concluídos',
        variant: 'success'
    },
    {
        key: 'alertas',
        title: 'Alertas',
        description: 'Itens com prioridade de correção e acompanhamento.',
        highlight: '7 pendentes',
        variant: 'warning'
    },
    {
        key: 'financeiro',
        title: 'Financeiro',
        description: 'Receita e fluxo de caixa previstos para o próximo mês.',
        highlight: 'R$ 4.9M',
        variant: 'primary'
    }
];

export const CONSULTOR_OVERVIEW = {
    title: 'Consultor Inteligente SIGFA',
    description: 'Pronto para conectar análise contextual e recomendações estratégicas ao seu gestor corporativo.',
    note: 'Disponível para expansão futura com diagnóstico automatizado e aprendizado contínuo.'
};

export const FASTAPI_PLACEHOLDER = {
    baseUrl: '/api',
    endpoints: {
        metrics: '/dashboard/metrics',
        companies: '/dashboard/companies',
        alerts: '/dashboard/alerts'
    }
};
