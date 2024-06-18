class Player:
    """Representa um jogador do jogo."""

    def __init__(self, nome, level, exp, exp_max, hp, hp_max, dano):
        """
        Inicializa um objeto jogador.

        Args:
            nome (str): O nome do jogador.
            level (int): O nível do jogador.
            exp (int): A experiência atual do jogador.
            exp_max (int): A quantidade máxima de experiência necessária para subir de nível.
            hp (int): A quantidade atual de pontos de vida do jogador.
            hp_max (int): A quantidade máxima de pontos de vida do jogador.
            dano (int): O dano que o jogador pode causar.
        """
        self.nome = nome
        self.level = level
        self.exp = exp
        self.exp_max = exp_max
        self.hp = hp
        self.hp_max = hp_max
        self.dano = dano

    def level_up(self):
        """Realiza o processo de nivelamento do jogador."""
        if self.exp >= self.exp_max:
            self.level += 1
            self.exp = 0
            self.exp_max *= 2
            self.hp_max += 20

    def reset(self):
        """Reseta os pontos de vida do jogador para o máximo."""
        self.hp = self.hp_max

    def atacar(self, npc):
        """
        Realiza um ataque ao NPC.

        Args:
            npc (NPC): O NPC que será atacado.
        """
        npc.hp -= self.dano


class NPC:
    """Representa um NPC (Non-Player Character) do jogo."""

    def __init__(self, nome, level, dano, hp, hp_max, exp):
        """
        Inicializa um objeto NPC.

        Args:
            nome (str): O nome do NPC.
            level (int): O nível do NPC.
            dano (int): O dano que o NPC pode causar.
            hp (int): A quantidade atual de pontos de vida do NPC.
            hp_max (int): A quantidade máxima de pontos de vida do NPC.
            exp (int): A experiência que o NPC concede ao ser derrotado.
        """
        self.nome = nome
        self.level = level
        self.dano = dano
        self.hp = hp
        self.hp_max = hp_max
        self.exp = exp

    def reset(self):
        """Reseta os pontos de vida do NPC para o máximo."""
        self.hp = self.hp_max

    def atacar(self, player):
        """
        Realiza um ataque ao jogador.

        Args:
            player (Player): O jogador que será atacado.
        """
        player.hp -= self.dano


class Batalha:
    """Gerencia uma batalha entre um jogador e um NPC."""

    def __init__(self, player, npc):
        """
        Inicializa um objeto de batalha.

        Args:
            player (Player): O jogador que participará da batalha.
            npc (NPC): O NPC que participará da batalha.
        """
        self.player = player
        self.npc = npc

    def iniciar(self):
        """Inicia a batalha entre o jogador e o NPC."""
        while self.player.hp > 0 and self.npc.hp > 0:
            self.player.atacar(self.npc)
            self.npc.atacar(self.player)
            self.exibir_info_batalha()

        if self.player.hp > 0:
            print(f"O {self.player.nome} venceu e ganhou {self.npc.exp} de EXP!")
            self.player.exp += self.npc.exp
            self.player.level_up()
        else:
            print(f"O {self.npc.nome} venceu!")

        self.player.reset()
        self.npc.reset()

    def exibir_info_batalha(self):
        """Exibe informações sobre a batalha (pontos de vida do jogador e do NPC)."""
        print(f"Player: {self.player.hp}/{self.player.hp_max}")
        print(f"NPC {self.npc.nome}: {self.npc.hp}/{self.npc.hp_max}")
        print("--------------------\n")


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
