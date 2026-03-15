# 🏝️ Manual das Ilhas - Procurando Terras no Meio do Mar

*Senta que lá vem história! Imagine que você é um cartógrafo nos anos 90 e recebeu um mapa misterioso do governo. O mapa é uma grade cheia de 1s (terra) e 0s (água). Sua missão: contar QUANTAS ILHAS existem nesse mapa!*

---

## 🎬 O PROBLEMA (Tipo Missão do Mapa do Tesouro)

Você tem um mapa representado assim:
[
["1", "1", "0", "0", "0"],
["1", "1", "0", "0", "0"],
["0", "0", "1", "0", "0"],
["0", "0", "0", "1", "1"]
]

text

Regras:
- **"1"** = TERRA (pode andar)
- **"0"** = ÁGUA (não pode andar)
- **ILHA** = Conjunto de "1"s vizinhos (na horizontal ou vertical)

Nesse exemplo temos **3 ilhas**:
1. Os quatro "1" no canto superior esquerdo
2. O "1" solitário no meio
3. Os dois "1" no canto inferior direito

---

## 📦 O QUE VAMOS PRECISAR

```python
from collections import deque
deque (pronuncia-se "deck"): É tipo uma fila de banco, mas mais rápida!

Nos anos 90, seria como aquelas senhas de atendimento: quem chega primeiro é atendido primeiro (FIFO - First In, First Out)

Vamos usar pra explorar a ilha em "ondas" (BFS)

🏗️ A ESTRUTURA DA CLASSE
python
class Solution:
    def numIslands(self, grid):
class Solution: Mesma coisa dos problemas anteriores, é o "invólucro" que o LeetCode gosta

def numIslands(self, grid): Função que conta ilhas

self: autorreferência (igual "eu mesmo")

grid: o mapa (matriz de caracteres "0" e "1")

🛡️ PRIMEIRA PROTEÇÃO
python
        if not grid:
            return 0
if not grid: Se o mapa estiver vazio (não veio nada)

return 0: Devolve 0 ilhas (lógico, não tem mapa!)

É tipo abrir o mapa e ver que é uma folha em branco - não tem terra nenhuma!

📏 MEDINDO O MAPA
python
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
rows = len(grid): Número de linhas (quantas fileiras no mapa)

cols = len(grid[0]): Número de colunas (largura do mapa)

islands = 0: Contador de ilhas (começa zerado)

Imagina que você tá medindo o mapa com uma régua: altura × largura.

🗺️ A FUNÇÃO EXPLORADORA (BFS)
python
        def bfs(r, c):
bfs = Breadth-First Search (Busca em Largura)

É tipo jogar uma pedra na água e ver as ondas se expandindo

Vai explorar TODA a ilha a partir de um ponto inicial (r, c)

Preparando a Fila de Exploração
python
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"
queue = deque(): Cria uma fila vazia (tipo pegar senha no guichê)

queue.append((r, c)): Coloca a posição inicial na fila (primeiro da fila!)

grid[r][c] = "0": MARCA como visitado! Transforma terra em água pra não contar de novo

IMPORTANTE: Isso é tipo chegar numa ilha e hastear a bandeira - "Já estivemos aqui!"

Enquanto Tiver Gente na Fila...
python
            while queue:
                row, col = queue.popleft()
while queue: Enquanto a fila não estiver vazia

row, col = queue.popleft(): Pega o primeiro da fila (quem chegou primeiro)

É tipo atendimento de banco: enquanto tem cliente, atende o próximo!

As Quatro Direções (Norte, Sul, Leste, Oeste)
python
                directions = [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ]
Essas são as direções possíveis para explorar:

(1, 0): Desce uma linha (Sul) ⬇️

(-1, 0): Sobe uma linha (Norte) ⬆️

(0, 1): Vai pra direita (Leste) ➡️

(0, -1): Vai pra esquerda (Oeste) ⬅️

ATENÇÃO: Só essas 4! Diagonal não conta (senão viraria outro problema)

Explorando Cada Direção
python
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
for dr, dc in directions: Para cada direção possível

nr = row + dr: Nova linha = linha atual + movimento

nc = col + dc: Nova coluna = coluna atual + movimento

É tipo dar um passinho em cada direção pra ver o que tem!

Verificando se Pode Explorar
python
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == "1"
                ):
Três condições TEM QUE SER VERDADE:

0 <= nr < rows: Não pode sair do mapa (linha dentro dos limites)

0 <= nc < cols: Também não pode sair (coluna dentro dos limites)

grid[nr][nc] == "1": Tem que ser TERRA (não água e não visitado)

É tipo: "Esse pedaço existe? Tá no mapa? É terra? PODE IR!"

Adicionando na Fila e Marcando
python
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
queue.append((nr, nc)): Coloca essa nova posição na FILA pra explorar depois

grid[nr][nc] = "0": MARCA como visitado (transforma em água)

É tipo: "Descobrimos mais terra! Bota na lista de lugares pra visitar e já marca que a gente passou aqui!"

🔍 O ESCANEAMENTO DO MAPA
python
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
Agora vem a parte do cartógrafo: varrer o mapa TODO!

for r in range(rows): Para cada linha

for c in range(cols): Para cada coluna (célula)

if grid[r][c] == "1": Achou terra não visitada!

bfs(r,c): EXPLORA A ILHA INTEIRA (e marca tudo como visitado)

islands += 1: Achou mais uma ilha! Incrementa contador

É tipo: "Opa, terra não descoberta! Manda a expedição explorar tudo e risca do mapa... Isso é mais uma ilha no relatório!"

O Retorno Final
python
        return islands
Depois de varrer o mapa inteiro, devolve o número total de ilhas encontradas.

🎮 EXEMPLO PASSO A PASSO
Mapa inicial:

text
[1, 1, 0]
[1, 0, 0]
[0, 0, 1]
Passo 1: r=0, c=0 → Achou "1"
text
🤚 AQUI! [1, 1, 0]
        [1, 0, 0]
        [0, 0, 1]
Chama BFS(0,0):

Marca (0,0) como 0

Fila: [(0,0)]

Atende (0,0): olha vizinhos → (1,0) é 1, adiciona na fila

Atende (1,0): olha vizinhos → (0,0) já é 0, (1,1) é 0

Fila vazia → ilha 1 explorada!

text
islands = 1
Passo 2: Continuando varredura
r=0, c=1 → já é 0 (viramos água)
r=0, c=2 → 0

r=1, c=0 → 0
r=1, c=1 → 0
r=1, c=2 → 0

Passo 3: r=2, c=2 → Achou "1"
text
        [0, 0, 0]
        [0, 0, 0]
        [0, 0, 🤚 1]
Chama BFS(2,2):

Marca e explora (só ele, sem vizinhos)

text
islands = 2
Resultado final: 2 ilhas!
📊 VISUALIZAÇÃO DO PROCESSO
text
Mapa inicial:        Após 1ª ilha:       Após 2ª ilha:
[1, 1, 0]           [0, 0, 0]           [0, 0, 0]
[1, 0, 0]    →     [0, 0, 0]     →     [0, 0, 0]
[0, 0, 1]           [0, 0, 1]           [0, 0, 0]

islands=0           islands=1           islands=2