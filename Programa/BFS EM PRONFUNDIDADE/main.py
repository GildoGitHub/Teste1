from agenteAmbiente import *

ambiente = Ambiente()
agente = Agente(ambiente.localizacao_default())

visitados = set()
resultado = dfs(ambiente, agente, visitados)
print("profundidade ", resultado)
