"""Arquivo principal da Unidade 1 — integra os três tipos de agentes."""

from semaforo import AmbienteSemaforo, agente_semaforo
from navegacao import AmbienteMapa, agente_baseado_objetivo
from utilidade import rotas_v2, agente_utilidade_v2


def meta_agente(cenario, percepcao=None):
    """Direciona cada cenário para o tipo de agente correspondente."""

    if cenario == 'transito':
        # Agente REATIVO: decide somente a partir da percepção atual das filas.
        if percepcao is None:
            raise ValueError('O cenário transito precisa de uma percepção.')
        return agente_semaforo(percepcao)

    elif cenario == 'navegacao':
        # Agente BASEADO EM OBJETIVOS: escolhe ações que aproximam do objetivo.
        if percepcao is None:
            raise ValueError('O cenário navegacao precisa de uma percepção.')
        return agente_baseado_objetivo(percepcao)

    elif cenario == 'escolha_rota':
        # Agente BASEADO EM UTILIDADE: compara alternativas por uma função de utilidade.
        # Desafio integrado da Aula 7: critério extra de segurança.
        melhor_rota = agente_utilidade_v2(
            rotas_v2,
            peso_tempo=0.3,
            peso_pedagio=1,
            peso_seguranca=6,
        )
        return melhor_rota['nome']

    else:
        raise ValueError(f'Cenário desconhecido: {cenario}')


def demonstrar_transito():
    print('\n=== CENÁRIO 1: TRÂNSITO ===')
    ambiente = AmbienteSemaforo()
    percepcao = ambiente.perceber()
    acao = meta_agente('transito', percepcao)
    print('Percepção:', percepcao)
    print('Ação escolhida:', acao)


def demonstrar_navegacao():
    print('\n=== CENÁRIO 2: NAVEGAÇÃO ===')
    ambiente = AmbienteMapa()
    print('Início:', ambiente.posicao, '| Objetivo:', ambiente.objetivo)

    for passo in range(1, 20):
        percepcao = ambiente.perceber()
        acao = meta_agente('navegacao', percepcao)

        if acao == 'Parar':
            print(f'Objetivo alcançado em {ambiente.posicao}.')
            break

        ambiente.executar(acao)
        print(f'Passo {passo}: {acao} -> {ambiente.posicao}')


def demonstrar_escolha_rota():
    print('\n=== CENÁRIO 3: ESCOLHA DE ROTA ===')
    rota_escolhida = meta_agente('escolha_rota')
    print('Rota escolhida considerando tempo, pedágio e segurança:')
    print(rota_escolhida)


def demonstracao_completa():
    print('DEMONSTRAÇÃO COMPLETA — UNIDADE 1')
    demonstrar_transito()
    demonstrar_navegacao()
    demonstrar_escolha_rota()


if __name__ == '__main__':
    demonstracao_completa()
