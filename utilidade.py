"""Agente baseado em utilidade da Aula 7 — escolha de rota."""


rotas = [
    {'nome': 'Avenida Central', 'tempo_min': 28, 'pedagio': 0},
    {'nome': 'Marginal', 'tempo_min': 22, 'pedagio': 4.5},
    {'nome': 'Bairro Industrial', 'tempo_min': 35, 'pedagio': 0},
]


def utilidade(rota, peso_tempo=1.0, peso_pedagio=2.0):
    custo = peso_tempo * rota['tempo_min'] + peso_pedagio * rota['pedagio']
    return -custo


def agente_baseado_utilidade(rotas, **pesos):
    """Escolhe a rota com maior valor de utilidade."""
    return max(rotas, key=lambda r: utilidade(r, **pesos))


# Desafio da Aula 7: acrescentar um critério extra de utilidade — segurança.
rotas_v2 = [
    {
        'nome': 'Avenida Central',
        'tempo_min': 28,
        'pedagio': 0,
        'nivel_seguranca': 4,
    },
    {
        'nome': 'Marginal',
        'tempo_min': 22,
        'pedagio': 4.5,
        'nivel_seguranca': 3,
    },
    {
        'nome': 'Bairro Industrial',
        'tempo_min': 35,
        'pedagio': 0,
        'nivel_seguranca': 5,
    },
]


def utilidade_v2(
    rota,
    peso_tempo=1.0,
    peso_pedagio=2.0,
    peso_seguranca=0.0,
):
    custo = peso_tempo * rota['tempo_min'] + peso_pedagio * rota['pedagio']
    beneficio = peso_seguranca * rota['nivel_seguranca']
    return beneficio - custo


def agente_utilidade_v2(rotas, **pesos):
    return max(rotas, key=lambda r: utilidade_v2(r, **pesos))


def demonstracao():
    escolhida = agente_baseado_utilidade(rotas)

    for rota in rotas:
        print(rota['nome'], '-> utilidade:', round(utilidade(rota), 1))

    print('\nRota escolhida:', escolhida['nome'])

    print('\nCom critério extra de segurança:')
    escolhida_segura = agente_utilidade_v2(
        rotas_v2,
        peso_tempo=0.3,
        peso_pedagio=1,
        peso_seguranca=6,
    )
    print('Rota escolhida:', escolhida_segura['nome'])


if __name__ == '__main__':
    demonstracao()
