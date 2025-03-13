import pygame
import random

pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 870, 600
FDS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
fonte = pygame.font.Font(None, 35)
pygame.display.set_caption("🏃🏽‍♂️🏃🏽‍♀️RUN GAME🏃🏽‍♀️🏃🏽‍♂️")

# Música de fundo
som_fundo = pygame.mixer.Sound('assets/music/musica.mp3')
som_fundo.set_volume(1)
som_fundo.play()

# Carregar imagens dos fundos
fundo_fase1 = pygame.image.load("assets/img/RUA.png").convert_alpha()
fundo_fase2 = pygame.image.load("assets/img/RUA2.png").convert()
fundo_fase3 = pygame.image.load("assets/img/RUA3.png").convert()

# Função para carregar o fundo correto conforme a pontuação
def atualizar_fundo(score):
    if score > 30:
        return pygame.transform.scale(fundo_fase3, (WIDTH, HEIGHT))
    elif score > 15:
        return pygame.transform.scale(fundo_fase2, (WIDTH, HEIGHT))
    else:
        return pygame.transform.scale(fundo_fase1, (WIDTH, HEIGHT))


## **CLASSE CARRO**
class Carro:
    def __init__(self):        
        self.imagem = pygame.image.load("assets/img/CARRO.png").convert_alpha()
        self.carro_width = 170
        self.carro_height = 160
        self.imagem = pygame.transform.scale(self.imagem, (self.carro_width, self.carro_height))
        self.rect = self.imagem.get_rect()

        # Faixas da estrada e posição inicial
        self.faixas = [300, 435, 570]
        self.faixa_atual = 1
        self.rect.centerx = self.faixas[self.faixa_atual]  
        self.rect.centery = HEIGHT - self.carro_height / 2  

    def mover(self, direcao):
        if direcao == "esquerda" and self.faixa_atual > 0:
            self.faixa_atual -= 1
        elif direcao == "direita" and self.faixa_atual < 2:
            self.faixa_atual += 1
        self.rect.centerx = self.faixas[self.faixa_atual]
    
    def desenho(self, window):
        window.blit(self.imagem, self.rect)


## **CLASSE BARRICADA**
class Barricada:
    def __init__(self):
        self.imagem = pygame.image.load("assets/img/barricada.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.rect = self.imagem.get_rect()
        self.faixas = [270, 405, 540]
        self.speed = 10
        self.reposicionar()

    def reposicionar(self):
        """Reposiciona a barricada aleatoriamente no topo da tela."""
        self.rect.x = random.choice(self.faixas)
        self.rect.y = -self.rect.height

    def update(self, score):
        """Move a barricada e aumenta a velocidade conforme a pontuação."""
        self.rect.y += self.speed
        
        if score > 30:
            self.speed = 20
        elif score > 15:
            self.speed = 15
        else:
            self.speed = 10

        if self.rect.top >= HEIGHT:
            self.reposicionar()

    def desenho(self, window):
        """Desenha a barricada na tela."""
        window.blit(self.imagem, self.rect)


# **Função para mostrar pontuação corretamente (AGORA EM PRETO)**
def mostra_pontuacao(window, tempo_inicial):
    """Calcula e exibe a pontuação com base no tempo de jogo."""
    contagem_tempo = int(pygame.time.get_ticks() / 1000) - tempo_inicial  
    texto_pontuacao_tela = fonte.render(f"Pontuação: {contagem_tempo}", False, (0, 0, 0))  # **Texto em preto**
    texto_pontuacao_retangulo = texto_pontuacao_tela.get_rect(center=(WIDTH/2, 50))  
    window.blit(texto_pontuacao_tela, texto_pontuacao_retangulo)
    return contagem_tempo  


# **Função para exibir a tela de Game Over**
def game_over():
    window.fill((0, 0, 0))
    fonte_game_over = pygame.font.Font(None, 70)
    texto_game_over = fonte_game_over.render("GAME OVER", True, (255, 0, 0))
    window.blit(texto_game_over, (WIDTH // 2 - texto_game_over.get_width() // 2, HEIGHT // 3))

    fonte_restart = pygame.font.Font(None, 40)
    texto_restart = fonte_restart.render("Pressione qualquer tecla para reiniciar", True, (255, 255, 255))
    window.blit(texto_restart, (WIDTH // 2 - texto_restart.get_width() // 2, HEIGHT // 2))

    pygame.display.update()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                esperando = False
                main()


# **Função principal do jogo**
def main():
    carro = Carro()
    barricada = Barricada()
    
    speed_fundo = 10  
    clock = pygame.time.Clock()
    tempo_inicial = int(pygame.time.get_ticks() / 1000)
    loop = True

    while loop:
        window.fill((255, 255, 255))  # **Fundo branco para garantir contraste com o texto preto**

        # Atualiza a imagem do fundo conforme a pontuação
        score = int(pygame.time.get_ticks() / 1000) - tempo_inicial
        imagem_fundo = atualizar_fundo(score)
        imagem_fundo_rect = imagem_fundo.get_rect()

        # Atualiza a posição do fundo
        imagem_fundo_rect.y += speed_fundo
        if imagem_fundo_rect.top >= HEIGHT:
            imagem_fundo_rect.y -= imagem_fundo_rect.height

        # Desenha o fundo atualizado
        window.blit(imagem_fundo, imagem_fundo_rect)
        imagem_fundo_rect_2 = imagem_fundo_rect.copy()
        imagem_fundo_rect_2.y -= imagem_fundo_rect_2.height
        window.blit(imagem_fundo, imagem_fundo_rect_2)

        # Atualiza e desenha os objetos
        barricada.update(score)
        barricada.desenho(window)
        carro.desenho(window)

        # Movimentação do carro
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            carro.mover("esquerda")
            pygame.time.wait(100)
        if keys[pygame.K_RIGHT]:
            carro.mover("direita")
            pygame.time.wait(100)

        # Verifica colisão
        if carro.rect.colliderect(barricada.rect):
            game_over()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # DESENHA A PONTUAÇÃO POR ÚLTIMO, para ficar por cima de tudo
        mostra_pontuacao(window, tempo_inicial)

        pygame.display.update()
        clock.tick(FDS)

# Iniciar o jogo
main()
