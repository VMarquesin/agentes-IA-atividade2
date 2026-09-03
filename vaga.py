"""Cenário de estacionamento — agente baseado em utilidade."""

vagas = [
    {
        'nome': 'Vaga coberta, longe da entrada',
        'distancia_m': 80,
        'preco': 8.0,
        'coberta': True,
    },
    {
        'nome': 'Vaga descoberta, perto da entrada',
        'distancia_m': 15,
        'preco': 6.0,
        'coberta': False,
    },
    {
        'nome': 'Vaga coberta, perto da entrada',
        'distancia_m': 20,
        'preco': 12.0,
        'coberta': True,
    },
]


def utilidade_vaga(vaga, peso_distancia=1.0, peso_preco=1.0, bonus_coberta=0.0):
    """Calcula a utilidade de uma vaga considerando custo e benefício."""
    custo = peso_distancia * vaga['distancia_m'] + peso_preco * vaga['preco']
    beneficio = bonus_coberta if vaga['coberta'] else 0
    return beneficio - custo


def agente_baseado_utilidade_vaga(vagas, **pesos):
    """Retorna a vaga com maior valor de utilidade."""
    return max(vagas, key=lambda v: utilidade_vaga(v, **pesos))


if __name__ == '__main__':
    configuracoes = [
        (
            'Distância mais importante',
            {'peso_distancia': 1.0, 'peso_preco': 1.0, 'bonus_coberta': 0.0},
            'A vaga descoberta perto da entrada vence porque tem a menor combinação de distância e preço.',
        ),
        (
            'Cobertura valorizada',
            {'peso_distancia': 1.0, 'peso_preco': 1.0, 'bonus_coberta': 30.0},
            'A vaga coberta perto da entrada vence porque o bônus pela cobertura compensa o preço maior.',
        ),
        (
            'Preço e cobertura mais importantes que distância',
            {'peso_distancia': 0.05, 'peso_preco': 3.0, 'bonus_coberta': 20.0},
            'A vaga coberta longe da entrada vence porque sua distância quase não pesa e ela é mais barata que a outra vaga coberta.',
        ),
    ]

    print('=== TESTES DO CENÁRIO ESTACIONAMENTO ===')
    for titulo, pesos, explicacao in configuracoes:
        escolhida = agente_baseado_utilidade_vaga(vagas, **pesos)
        print(f'\n{titulo}')
        print('Pesos:', pesos)
        for vaga in vagas:
            valor = utilidade_vaga(vaga, **pesos)
            print(f"  {vaga['nome']}: utilidade = {valor:.2f}")
        print('Escolha:', escolhida['nome'])
        print('Por quê:', explicacao)
