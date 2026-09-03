"""Agente baseado em objetivos da Aula 6 — navegação em grade."""


class AmbienteMapa:
    def __init__(self, tamanho=5, posicao_inicial=(0, 0)):
        self.tamanho = tamanho
        self.posicao = posicao_inicial
        self.objetivo = (tamanho - 1, tamanho - 1)

    def perceber(self):
        return self.posicao, self.objetivo

    def executar(self, acao):
        x, y = self.posicao

        if acao == 'Direita' and x < self.tamanho - 1:
            x += 1
        elif acao == 'Esquerda' and x > 0:
            x -= 1
        elif acao == 'Baixo' and y < self.tamanho - 1:
            y += 1
        elif acao == 'Cima' and y > 0:
            y -= 1

        self.posicao = (x, y)


def agente_baseado_objetivo(percepcao):
    """Move na direção que reduz a distância até o objetivo."""
    (x, y), (gx, gy) = percepcao

    if x < gx:
        return 'Direita'
    if x > gx:
        return 'Esquerda'
    if y < gy:
        return 'Baixo'
    if y > gy:
        return 'Cima'
    return 'Parar'


def posicao_livre(pos, obstaculos, tamanho):
    x, y = pos
    dentro = 0 <= x < tamanho and 0 <= y < tamanho
    return dentro and pos not in obstaculos


def agente_com_obstaculos(percepcao, obstaculos, tamanho):
    """Desafio da Aula 6: tenta evitar movimentos que atingem obstáculos."""
    (x, y), (gx, gy) = percepcao
    candidatos = []

    if x < gx:
        candidatos.append('Direita')
    if x > gx:
        candidatos.append('Esquerda')
    if y < gy:
        candidatos.append('Baixo')
    if y > gy:
        candidatos.append('Cima')

    for acao in candidatos:
        nx, ny = x, y
        if acao == 'Direita':
            nx += 1
        elif acao == 'Esquerda':
            nx -= 1
        elif acao == 'Baixo':
            ny += 1
        elif acao == 'Cima':
            ny -= 1

        if posicao_livre((nx, ny), obstaculos, tamanho):
            return acao

    return 'Parar'


def demonstracao():
    ambiente = AmbienteMapa()
    print('Início:', ambiente.posicao, '-> Objetivo:', ambiente.objetivo)

    for passo in range(1, 12):
        percepcao = ambiente.perceber()
        acao = agente_baseado_objetivo(percepcao)

        if acao == 'Parar':
            print(f'Passo {passo}: chegou ao objetivo em {ambiente.posicao}')
            break

        ambiente.executar(acao)
        print(f'Passo {passo}: ação {acao} -> nova posição {ambiente.posicao}')


if __name__ == '__main__':
    demonstracao()
