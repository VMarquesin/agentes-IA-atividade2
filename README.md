# agentes-IA-atividade2

**Unidade 1 — Integração dos Agentes**

Este projeto reúne quatro cenários desenvolvidos na Unidade 1 da disciplina de Inteligência Artificial, utilizando agentes reativos, baseados em objetivos e baseados em utilidade.

---

## Arquivos do Projeto

### `semaforo.py`
Contém o ambiente de semáforo e o `agente_semaforo`.
* **Tipo de agente:** Reativo. A decisão é tomada diretamente a partir da percepção atual das filas de carros, sem planejamento de ações futuras.
* **Detalhes:** O arquivo mantém a classe `AgenteSemaforoComMargem`, referente ao desafio de margem de segurança da Aula 5.

### `navegacao.py`
Contém o `AmbienteMapa` e o `agente_baseado_objetivo`.
* **Tipo de agente:** Baseado em objetivos. O agente conhece a posição atual e a posição objetivo, e escolhe movimentos que o aproximam do destino.
* **Detalhes:** Estão presentes as funções do exercício de obstáculos da Aula 6.

### `utilidade.py`
Contém as rotas, a função de utilidade e o agente que escolhe a melhor alternativa.
* **Tipo de agente:** Baseado em utilidade. Várias rotas podem atingir o mesmo objetivo e a escolha é feita comparando valores de utilidade.
* **Detalhes:** Foi integrado o desafio da Aula 7 que adiciona o critério `nivel_seguranca` às rotas. A função `utilidade_v2` considera tempo, pedágio e segurança.

### `vaga.py`
Contém três vagas de estacionamento, a função `utilidade_vaga` e o `agente_baseado_utilidade_vaga`.
* **Tipo de agente:** Baseado em utilidade. O agente compara as vagas considerando distância até a entrada, preço e o benefício de a vaga ser coberta.
* **Detalhes:** O arquivo possui três configurações de pesos para demonstrar como a importância atribuída a cada critério altera a vaga escolhida.

### `principal_unidade1.py`
É o arquivo principal do projeto. Ele importa os quatro cenários e implementa a função `meta_agente(cenario, percepcao=None)`.

A função direciona cada cenário para o agente correto:
* `transito` → Agente reativo;
* `navegacao` → Agente baseado em objetivos;
* `escolha_rota` → Agente baseado em utilidade (utiliza o critério extra de segurança da Aula 7);
* `estacionamento` → Agente baseado em utilidade (compara distância, preço e cobertura).

---

## Proteção das Demonstrações

Os arquivos `semaforo.py`, `navegacao.py`, `utilidade.py` e `vaga.py` possuem suas demonstrações encapsuladas dentro da seguinte verificação:

```python
if __name__ == '__main__':