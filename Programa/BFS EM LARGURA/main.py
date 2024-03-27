
from agente import *

ambiente = Ambiente()
agente = Agente(ambiente.localizacao_default())

resultado = bfs(ambiente, agente)
print("Resultado da busca em largura:", resultado)