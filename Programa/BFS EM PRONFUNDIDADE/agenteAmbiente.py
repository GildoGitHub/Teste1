import random
from collections import deque

class Ambiente:
    def __init__(self):
        self.estado = {'Q1': random.choice(['cheio', 'vazio']),
                       'Q2': random.choice(['cheio', 'vazio'])}
        self.accao = ['encher', 'esquerda', 'direita']

    def percepcao(self, agente):
        return (agente.localizacao, self.estado[agente.localizacao])

    def localizacao_default(self):
        return random.choice(['Q1', 'Q2'])

    def executar_accao(self, accao, agente):
        if accao == 'esquerda':
            agente.performace -= 1
        elif accao == 'direita':
            agente.performace -= 1
        elif accao == 'encher':
            agente.performace += 10
            self.estado[agente.localizacao] = "cheio"

class Agente:
    def __init__(self, localizacao):
        self.performace = 0
        self.localizacao = localizacao

    def programa_tabela(self, percepcao):

        tabela = {('Q1', 'cheio'): 'direita',
                  ('Q1', 'vazio'): 'encher',
                  ('Q2', 'cheio'): 'esquerda',
                  ('Q2', 'vazio'): 'encher',
                  (('Q1', 'vazio'), ('Q1', 'cheio')): 'esquerda',
                  (('Q1', 'cheio'), ('Q2', 'vazio')): 'encher',
                  (('Q2', 'cheio'), ('Q1', 'vazio')): 'encher',
                  (('Q2', 'vazio'), ('Q2', 'cheio')): 'encher',
                  (('Q1', 'vazio'), ('Q1', 'cheio'), ('Q2', 'vazio')): 'encher',
                  (('Q2', 'vazio'), ('Q2', 'cheio'), ('Q1', 'vazio')): 'encher'}

        return tabela.get(percepcao)

def dfs_search(ambiente, initial_state):
    frontier = [initial_state]
    explored = set()

    while frontier:
        state = frontier.pop()

        if is_goal_state(state):
            return state

        explored.add(state)

        for action in reversed(ambiente.accoes_possiveis(state)):
            next_state = ambiente.resultado(state, action)
            if next_state not in explored and next_state not in frontier:
                frontier.append(next_state)

    return None
def is_goal_state(state, ambiente):
    return 'cheio' in state.values()