## Fase 2
import pygame 
import random 

pygame.init()

clock = pygame.time.Clock()
FDS = 60 

WIDTH = 870
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
fonte = pygame.font.Font(None, 35) #variavel para definir a fonte (não coloquei nenhuma)
pygame.display.set_caption('🏃🏽‍♂️🏃🏽‍♀️RUN GAME🏃🏽‍♀️🏃🏽‍♂️')
tempo_inicial = 0 #zera a pontuação ao reiniciar
barricada_speed = 10
#Toca a música no jogo
som_fundo = pygame.mixer.Sound('assets/music/musica.mp3') #som da musica
som_fundo.set_volume(1) #volume som do pulo
som_fundo.play() #toca a musica

imagem_fundo = pygame.image.load('assets/img/RUA.png').convert_alpha()
imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

imagem_fundo_rect = imagem_fundo.get_rect()
speed_fundo = 10


## CARRO VERMELHO 
imagem_carro_vermelho = pygame.image.load('assets/img/CARRO.png').convert_alpha()
imagem_carro_vermelho_width = 170
imagem_carro_vermelho_height  = 160
imagem_carro_vermelho = pygame.transform.scale(imagem_carro_vermelho, (imagem_carro_vermelho_width, imagem_carro_vermelho_height))
imagem_carro_vermelho_rect = imagem_carro_vermelho.get_rect()

# Defina as faixas de estrada e posicione o carro inicialmente na faixa central (405)
faixas_estrada_carro = [300, 435, 570]
faixa_atual = 1  # Começa na faixa do meio (405)
imagem_carro_vermelho_rect.centerx = faixas_estrada_carro[faixa_atual]  # Centraliza o carro horizontalmente
imagem_carro_vermelho_rect.centery = HEIGHT - imagem_carro_vermelho_height / 2  # Centraliza o carro verticalmente no fundo


## BARRICADAS 
imagem_barricada = pygame.image.load('assets/img/barricada.png').convert_alpha()
imagem_barricada = pygame.transform.scale(imagem_barricada, (50, 50))
imagem_barricada_rect = imagem_barricada.get_rect()
imagem_barricada_rect.y = -imagem_barricada.get_height()

# Defina as faixas de estrada
faixas_estrada_barricada = [270, 405, 540]


# Função para reposicionar a barricada
def reposiciona_barricada():
    imagem_barricada_rect.x = random.choice(faixas_estrada_barricada)
    imagem_barricada_rect.y = -imagem_barricada.get_height()

reposiciona_barricada()

#função que mostra a pontuação
def mostra_pontuacao(tempo_inicial):
    contagem_tempo = int(pygame.time.get_ticks() / 1000) - tempo_inicial #pega os milliseconds e subtrai do tempo inicial quando reiniciar o jogo (precisa dividir por mil para ficar em segundos)        
    if contagem_tempo > 20:
        texto_pontuacao_tela = fonte.render(f'Pontuação: {contagem_tempo}', False, (255,235,144)) #variavel para definir a pontuação Fase 2
    else:
        texto_pontuacao_tela = fonte.render(f'Pontuação: {contagem_tempo}', False, (106,168,79)) #variavel para definir a pontuação Fase 1

    texto_pontuacao_retangulo = texto_pontuacao_tela.get_rect(center = (WIDTH/2, 50)) #cria a pontuação
    window.blit(texto_pontuacao_tela, texto_pontuacao_retangulo) #desenha a pontuação na janela
    return contagem_tempo #retorna a pontuação


# Função para exibir a tela de "Game Over"
def show_game_over_screen():
    window.fill((135, 206, 250))  # Azul Celeste, mesma cor usada na tela inicial
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))  # Vermelho para o texto
    window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

    # Mensagem de reinício
    restart_font = pygame.font.SysFont(None, 40)
    restart_text = restart_font.render("Quer jogar novamente?"," Clique em qualquer tecla para reiniciar", True, (255, 255, 255))  # Branco
    window.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
    
    pygame.display.flip()

    # Aguarda o jogador pressionar uma tecla para reiniciar o jogo
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False
                show_start_screen()  # Chama a função da tela de início

# Função para exibir a tela de início
def show_start_screen():
    window.blit(imagem_inicio, imagem_inicio_rect)
    window.blit(imagem_inicio, imagem_inicio_rect_2)
    
    # Fonte maior e cor azul celeste para o título
    title_font = pygame.font.SysFont(None, 72)
    title = title_font.render("RUN GAME", True, (135, 206, 250))  # Azul Celeste
    
    # Fonte menor para a história
    font = pygame.font.SysFont(None, 40)
    story = [
        " Você está em uma estrada a qual passa muitas crianças! ",
        " É preciso que desvie das barricadas ",
        " para não causar acidentes",
        " e preservar a própria segurança! ",
        "",

    ]

    font_inicio = pygame.font.SysFont(None, 30)
    inicio = font_inicio.render("Clique em qualquer botão para iniciar o jogo.", True, (0, 0, 139))


    # Desenha o título
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
    pygame.display.flip()
    
    # Desenha a história de forma animada
    for i, line in enumerate(story):
        rendered_line = ""
        for char in line:
            rendered_line += char
            text = font.render(rendered_line, True, (255, 255, 255)) ### branco 
            window.blit(imagem_inicio, imagem_inicio_rect)
            window.blit(imagem_inicio, imagem_inicio_rect_2)
            window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
            for j in range(i):
                previous_text = font.render(story[j], True, (255, 255, 255)) ## branco 
                window.blit(previous_text, (WIDTH // 2 - previous_text.get_width() // 2, HEIGHT // 3 + 40 * (j + 1)))
            window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3 + 40 * (i + 1)))
            pygame.display.flip()
            pygame.time.wait(50)  # Delay de 50ms entre cada letra

    window.blit(inicio, (WIDTH // 2 - inicio.get_width() // 2, HEIGHT // 38))
    pygame.display.flip()

    # Aguarda o jogador pressionar uma tecla ou botão do mouse para iniciar o jogo
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                waiting = False
                tempo_inicial = int(pygame.time.get_ticks() / 1000)
                mostra_pontuacao(tempo_inicial)

# Carrega a imagem de fundo da tela de início
imagem_inicio = pygame.image.load('assets/img/FUNDO_inicio.png').convert()
imagem_inicio = pygame.transform.scale(imagem_inicio, (WIDTH, HEIGHT))
imagem_inicio_rect = imagem_inicio.get_rect()
imagem_inicio_rect_2 = imagem_inicio_rect.copy()
imagem_inicio_rect_2.x -= imagem_inicio_rect_2.width
speed_fundo = 10

# Chama a tela de início ao iniciar o jogo
show_start_screen()
tempo_inicial = int(pygame.time.get_ticks() / 1000)
############################# LOOP PRINCIPAL ###################################

loop = True 

while loop:
    
    if mostra_pontuacao(tempo_inicial)> 20:
        imagem_fundo = pygame.image.load('assets/img/RUA2.png').convert() #carrega a imagem da fase 2.
    else:
        imagem_fundo = pygame.image.load('assets/img/RUA.png').convert_alpha()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))
    imagem_fundo_rect = imagem_fundo.get_rect()

    #### Movimento com as teclas 
    keys = pygame.key.get_pressed()

    # Movimento para a esquerda
    if keys[pygame.K_LEFT]:
        if faixa_atual > 0:  # Verifica se não está na faixa mais à esquerda
            faixa_atual -= 1  # Move para a faixa à esquerda
            imagem_carro_vermelho_rect.centerx = faixas_estrada_carro[faixa_atual]
            pygame.time.wait(100)  # Pequena pausa para evitar movimento rápido demais

    # Movimento para a direita
    if keys[pygame.K_RIGHT]:
        if faixa_atual < len(faixas_estrada_carro) - 1:  # Verifica se não está na faixa mais à direita
            faixa_atual += 1  # Move para a faixa à direita
            imagem_carro_vermelho_rect.centerx = faixas_estrada_carro[faixa_atual]
            pygame.time.wait(100)  # Pequena pausa para evitar movimento rápido demais


    # Atualiza estado do jogo
    window.fill((0, 0, 0))

    # Atualiza a posição da imagem de fundo.
    imagem_fundo_rect.y += speed_fundo

    # Se o fundo saiu da janela, faz ele voltar para dentro.
    if imagem_fundo_rect.top >= HEIGHT:
        imagem_fundo_rect.y -= imagem_fundo_rect.height

    # Desenha o fundo e uma cópia para baixo.
    window.blit(imagem_fundo, imagem_fundo_rect)
    imagem_fundo_rect_2 = imagem_fundo_rect.copy()
    imagem_fundo_rect_2.y -= imagem_fundo_rect_2.height
    window.blit(imagem_fundo, imagem_fundo_rect_2)
    mostra_pontuacao(tempo_inicial)

    # Atualiza a posição da barricada
    imagem_barricada_rect.y += barricada_speed

    # Se a barricada saiu da janela, reposiciona ela no topo
    if imagem_barricada_rect.top >= HEIGHT:
        reposiciona_barricada()

    # Verifica colisão entre o carro e a barricada
    if imagem_carro_vermelho_rect.colliderect(imagem_barricada_rect):
        show_game_over_screen()  # Chama a tela de "Game Over" se houver colisão
        reposiciona_barricada()
        tempo_inicial = int(pygame.time.get_ticks() / 1000)
    if mostra_pontuacao(tempo_inicial)> 20:
        barricada_speed = 20
    else:
        barricada_speed = 10


    ## para aparecer elementos:

    # Desenha a barricada
    window.blit(imagem_barricada, imagem_barricada_rect)

    # Desenha o carro vermelho
    window.blit(imagem_carro_vermelho, imagem_carro_vermelho_rect)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()
    clock.tick(FDS)

pygame.quit()
