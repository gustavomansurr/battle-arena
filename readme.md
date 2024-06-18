
---

# BattleArena

BattleArena é um jogo de batalha simples implementado em Python, onde um jogador enfrenta NPCs em combate.

## Descrição

O jogo consiste em um jogador que luta contra uma série de NPCs (Personagens Não-Jogáveis) em uma batalha por turnos. O jogador e os NPCs têm pontos de vida e causam dano uns aos outros até que um deles seja derrotado.

## Classes

### `Player`

- Representa um jogador do jogo.
- Atributos:
  - `nome`: Nome do jogador.
  - `level`: Nível do jogador.
  - `exp`: Experiência atual do jogador.
  - `exp_max`: Quantidade máxima de experiência necessária para subir de nível.
  - `hp`: Quantidade atual de pontos de vida do jogador.
  - `hp_max`: Quantidade máxima de pontos de vida do jogador.
  - `dano`: Dano que o jogador pode causar.
- Métodos:
  - `level_up()`: Realiza o processo de nivelamento do jogador.
  - `reset()`: Reseta os pontos de vida do jogador para o máximo.
  - `atacar(npc)`: Realiza um ataque ao NPC.

### `NPC`

- Representa um NPC (Non-Player Character) do jogo.
- Atributos:
  - `nome`: Nome do NPC.
  - `level`: Nível do NPC.
  - `dano`: Dano que o NPC pode causar.
  - `hp`: Quantidade atual de pontos de vida do NPC.
  - `hp_max`: Quantidade máxima de pontos de vida do NPC.
  - `exp`: Experiência que o NPC concede ao ser derrotado.
- Métodos:
  - `reset()`: Reseta os pontos de vida do NPC para o máximo.
  - `atacar(player)`: Realiza um ataque ao jogador.

### `Batalha`

- Gerencia uma batalha entre um jogador e um NPC.
- Atributos:
  - `player`: O jogador que participará da batalha.
  - `npc`: O NPC que participará da batalha.
- Métodos:
  - `iniciar()`: Inicia a batalha entre o jogador e o NPC.
  - `exibir_info_batalha()`: Exibe informações sobre a batalha.

## Utilização

Para clonar e executar este projeto localmente, siga estas etapas simples:

1. Certifique-se de ter o Git instalado em sua máquina. Se não tiver, você pode baixá-lo [aqui](https://git-scm.com/).
2. Abra o terminal ou prompt de comando.
3. Clone o repositório usando o seguinte comando:
   ```
   git clone https://github.com/gustavomansurr/battle-arena.git
   ```
4. Navegue até o diretório do projeto:
   ```
   cd battle-arena
   ```
5. Execute o script Python `batalha.py`:
   ```
   python batalha.py
   ```

Isso é tudo! Agora você pode desfrutar do jogo de batalha em sua própria máquina.

## Exemplo de Uso

```python
# Criando instâncias de Player e NPC
player = Player("Gustavo", 3, 0, 30, 100, 150, 30)
npcs = [NPC(f"Monstro #{i+1}", i+1, 5*(i+1), 100*(i+1), 100*(i+1), 7*(i+1)) for i in range(5)]

# Batalhando com um NPC selecionado usando a classe Batalha
npc_selecionado = npcs[0]
batalha = Batalha(player, npc_selecionado)
batalha.iniciar()

# Exibindo status do jogador após a batalha
print("Status do jogador após a batalha:")
print(f"Nome: {player.nome} // Level: {player.level} // Dano: {player.dano} // HP: {player.hp}/{player.hp_max} // EXP: {player.exp}/{player.exp_max}")
```

---
