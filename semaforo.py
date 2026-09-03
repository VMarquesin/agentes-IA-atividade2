"""Agente reativo da Aula 5 — controle de semáforo."""

import random


class AmbienteSemaforo:
    def __init__(self):
        self.carros = {
            'RuaA': random.randint(0, 20),
            'RuaB': random.randint(0, 20),
        }
        self.sinal_verde = 'RuaA'

    def perceber(self):
        return dict(self.carros)

    def executar(self, acao):
        self.sinal_verde = acao
        for rua in self.carros:
            if rua == acao:
                self.carros[rua] = max(
                    0, self.carros[rua] - random.randint(3, 6)
                )
            else:
                self.carros[rua] += random.randint(0, 4)


def agente_semaforo(percepcao):
    """Agente reativo: escolhe a rua com maior fila no estado atual."""
    if percepcao['RuaA'] >= percepcao['RuaB']:
        return 'RuaA'
    return 'RuaB'


class AgenteSemaforoComMargem:
    """Desafio da Aula 5: reduz trocas excessivas usando margem e tempo mínimo."""

    def __init__(self, margem=5, ciclos_minimos=2):
        self.sinal_atual = 'RuaA'
        self.ciclos_no_sinal_atual = 0
        self.margem = margem
        self.ciclos_minimos = ciclos_minimos

    def oposto(self):
        return 'RuaB' if self.sinal_atual == 'RuaA' else 'RuaA'

    def decidir(self, percepcao):
        diferenca = percepcao[self.oposto()] - percepcao[self.sinal_atual]
        pode_trocar = self.ciclos_no_sinal_atual >= self.ciclos_minimos

        if pode_trocar and diferenca >= self.margem:
            self.sinal_atual = self.oposto()
            self.ciclos_no_sinal_atual = 0
        else:
            self.ciclos_no_sinal_atual += 1

        return self.sinal_atual


def demonstracao():
    ambiente = AmbienteSemaforo()
    print('Estado inicial:', ambiente.carros)

    for ciclo in range(1, 6):
        percepcao = ambiente.perceber()
        acao = agente_semaforo(percepcao)
        ambiente.executar(acao)
        print(
            f'Ciclo {ciclo}: percebeu {percepcao} -> abre para {acao} '
            f'| novo estado: {ambiente.carros}'
        )


if __name__ == '__main__':
    demonstracao()
