
from agenteAmbiente import *
percepcoes = []
Q1, Q2 = 'Q1', 'Q2'

ambiente = Ambiente()
print("Estado do Ambiente:", ambiente.estado)
localizacao_agente = ambiente.localizacao_default()
agente = Agente(localizacao_agente)
percepcao = ambiente.percepcao(agente)
accao = agente.programa_tabela(percepcao)
ambiente.executar_accao(accao, agente)

print("Percepção:", percepcao)
print("Ação a Realizar:", accao)
print("Pontuação:", agente.performace)
print("Estado do Ambiente:", ambiente.estado)
print("Localização do Agente:", agente.localizacao)

# Troca de Localizacao do Agente
localizacao_anterior = agente.localizacao
localizacao_agente = Q1 if localizacao_anterior == Q2 else Q2
agente.localizacao = localizacao_agente
percepcao = ambiente.percepcao(agente)
accao = agente.programa_tabela(percepcao)
ambiente.executar_accao(accao, agente)

print("\nDepois de mudar de localização:")
print("Percepção do novo Ambiente:", percepcao)
print("Ação a Realizar:", accao)
print("Pontuação:", agente.performace)
print("Estado do Ambiente:", ambiente.estado)
print("Localização do Agente:", agente.localizacao)