# Importando as Bibliotecas;
import pygame
from random import randrange, randint

# Iniciando a Biblioteca pygame;
pygame.init()

# Variáveis Globais;
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
yellowGreen = (154,205,50)

bata = yellow
bata1 = white

largura = 400
altura = 500

tamanho = 10

placar = 40

relogio = pygame.time.Clock()

config = 0

# Criando a tela;
background = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")

# Funções;
def snake(snakeXY):
    for XY in snakeXY:
        pygame.draw.rect(background, red, [XY[0], XY[1], tamanho, tamanho])

def maca(color, maca_x, maca_y):
    pygame.draw.rect(background, color, [maca_x, maca_y, tamanho, tamanho])

def text(msg, color, tam, fonte, tof, fot, x, y):
    font = pygame.font.SysFont(fonte, tam, bold=tof, italic=fot)
    texto1 = font.render(msg, True, color)
    background.blit(texto1, [x, y])

def saindo():
    pygame.quit()
    quit()

def jogo():
    jogar = True
    gameOver = False

    # Definindo a posição da cobra e da maçã;
    pos_x = randrange(0, largura - tamanho, 10)
    pos_y = randrange(0, altura - tamanho - placar, 10)

    maca_x = randrange(0, largura - tamanho, 10)
    maca_y = randrange(0, altura - tamanho - placar, 10)
    randcolor = ( randint(10,254), randint(20,254), randint(30,254) ) 

    velocidade_x = 0
    velocidade_y = 0
    snakeXY = []
    snakeLen = 3

    # loop;
    while jogar:

        # Fazendo o nosso fim de jogo;
        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    saindo()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogar = True
                        gameOver = False

                        # Definindo a posição da cobra e da maçã;
                        pos_x = randrange(0, largura - tamanho, 10)
                        pos_y = randrange(0, altura - tamanho - placar, 10)

                        maca_x = randrange(0, largura - tamanho, 10)
                        maca_y = randrange(0, altura - tamanho - placar, 10)
                        randcolor = ( randint(10,254), randint(20,254), randint(30,254) ) 

                        velocidade_x = 0
                        velocidade_y = 0
                        snakeXY = []
                        snakeLen = 3

                    if event.key == pygame.K_s:
                        saindo()

                # Fazendo os botões funcionarem;
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0] 
                    y = pygame.mouse.get_pos()[1] 

                    if x > 45 and y > 200 and x < 200 and y < 242:
                        jogar = True
                        gameOver = False

                        # Definindo a posição da cobra e da maçã;
                        pos_x = randrange(0, largura - tamanho, 10)
                        pos_y = randrange(0, altura - tamanho - placar, 10)

                        maca_x = randrange(0, largura - tamanho, 10)
                        maca_y = randrange(0, altura - tamanho - placar, 10)
                        randcolor = ( randint(10,254), randint(20,254), randint(30,254) ) 

                        velocidade_x = 0
                        velocidade_y = 0
                        snakeXY = []
                        snakeLen = 3

                    elif x > 250 and y > 200 and x < 350 and y < 242:
                        pygame.quit()
                        quit()

                    elif x > 300 and y > 450 and x < 380 and y < 480:
                        menu()
                    
            # Escrevendo na tela de morte;
            background.fill(yellowGreen)
            text("F i m  d e  j o g o", black, 35, "Arial", True, False, 70, 50)
            text("___________________________", black, 20, "Arial", True, False, 60, 80)
            text("Pontuação: " + str(snakeLen - 1), black, 20, "Arial", True, False, 130, 110)

            # Desenhando os botões;
            pygame.draw.rect(background, black, [45, 200, 155, 42])
            text("Continuar (C)", white, 20, "Arial", True, True, 58, 208)

            pygame.draw.rect(background, black, [250, 200, 100, 42])
            text("Sair (S)", white, 20, "Arial", True, True, 265, 208)

            pygame.draw.rect(background, black, [300, 450, 80, 30])
            text("Menu", yellowGreen, 18, "Arial", False, True, 317, 453)

            pygame.display.update()
            
        # Verificação da requisição de saída;
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saindo()

            # Controles;
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

                if event.key == pygame.K_a and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_d and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_w and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_s and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

                if event.key == pygame.K_KP4 and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_KP6 and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_KP8 and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_KP2 and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

                #Atalho para morrer apertando a tecla espaço:
                # if event.key == pygame.K_SPACE:
                #     snakeLen += 1

        if jogar:
            # Preenchendo o fundo;
            background.fill(black)

            # Desenhando as linhas na tela;
            # for x in range(0, 400, 10):
            #     pygame.draw.line(background, (40, 40, 40), (x, 0), (x, 500))
            # for y in range(0, 500, 10):
            #     pygame.draw.line(background, (40, 40, 40), (0, y), (400, y))

            # Desenhando a maçã;
            maca(randcolor, maca_x, maca_y)

            # Desenhando a cobra;
            snakeHead = []

            snakeHead.append(pos_x)
            snakeHead.append(pos_y)

            snakeXY.append(snakeHead)

            if len(snakeXY) > snakeLen:
                del snakeXY[0]

            snake(snakeXY)

            # Movimentação;
            pos_x += velocidade_x
            pos_y += velocidade_y

            # Verificando se a maçã foi comida, para podermos gerar uma nova e fazermos a cobra crescer;
            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura - tamanho, 10)
                maca_y = randrange(0, altura - tamanho - placar, 10)
                randcolor = ( randint(10,254), randint(20,254), randint(30,254) ) 

                snakeLen += 1

            # Verificando colisão;
            if any(Block == snakeHead for Block in snakeXY[:-3]):
                gameOver = True

            # if len(snakeXY) >= 2:
            #     # Se a cobra tiver mais de 2 quadradinhos de comprimento
            #     if snakeXY.count(snakeXY[0]) > 1:
            #         # Se a cabeça da cobra (1° elemento da lista) aparecer mais de uma vez na lista
            #         gameOver = True  # Fecho o jogo


            if config == 0:
                # Fazendo a cobra retornar para a tela;
                if pos_x + tamanho > largura:
                    pos_x = 0
                if pos_x < 0:
                    pos_x = largura - tamanho

                if pos_y + tamanho > altura - placar:
                    pos_y = 0
                if pos_y < 0:
                    pos_y = altura - tamanho - placar

            if config == 1:
                # Encerrando o jogo ao encostar na borda;
                if pos_x + tamanho > largura:
                    gameOver = True
                if pos_x < 0:
                    gameOver = True

                if pos_y + tamanho > altura - placar:
                    gameOver = True
                if pos_y < 0:
                    gameOver = True

            # Desenhando o bloco de pontos;
            pygame.draw.rect(background, yellowGreen, [0, altura-placar, largura, placar])
            text("Pontos: "+str(snakeLen - 3), black, 20, "sans", True, False, 10, altura-30)

            # Atualização da tela;
            pygame.display.update()
            relogio.tick(15)

def instrucoes():
    pygame.draw.rect(background, black, [60, 100, 300, 340])
    pygame.draw.rect(background, white, [62, 102, 296, 336])

    voltar()

def configuracoes():
    while True:
        
        pygame.draw.rect(background, black, [60, 100, 300, 340])
        pygame.draw.rect(background, white, [62, 102, 296, 336])

        pygame.draw.rect(background, black, [300, 450, 80, 30])
        text("Menu", yellowGreen, 18, "Arial", False, True, 317, 453)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                saindo()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0] 
                y = pygame.mouse.get_pos()[1] 

                if x > 300 and y > 450 and x < 380 and y < 480:
                    menu()

                elif x > 140 and y > 118 and x < 160 and y < 138:
                    pass

        text("Jogo:     Clássico      Livre", black, 30, "Roboto", False, False, 80, 120)
        pygame.draw.rect(background, black, [140, 118, 20, 20]), pygame.draw.rect(background, black, [258, 118, 20, 20]) 
        pygame.draw.rect(background, white, [142, 120, 16, 16]), pygame.draw.rect(background, yellow, [260, 120, 16, 16]) 

        text("Maça: ", black, 30, "Roboto", False, False, 80, 170)

 
        pygame.display.update()   

def creditos():
    pygame.draw.rect(background, black, [60, 100, 300, 340])
    pygame.draw.rect(background, white, [62, 102, 296, 336])

    text("Créditos", black, 25, "Arial", False, True, 154, 110)
    text("- - - - - - - -", black, 28, "Arial", False, False, 148, 122)
    text("Desenvolvido por Edson", black, 18, "Arial", False, True, 112, 190)

    pygame.draw.rect(background, black, [68, 220, 284, 130])
    pygame.draw.rect(background, white, [70, 222, 280, 126])

    text("E-mail: ", black, 21, "Arial", False, True, 75, 230)
    text("edssaac@outlook.com", black, 19, "Arial", False, True, 148, 231)

    text("GitHub: ", black, 21, "Arial", False, True, 75, 270)
    text("github.com/Edssaac", black, 19, "Arial", False, True, 152, 271)

    text("Site: ", black, 21, "Arial", False, True, 75, 310)
    text("edssaac.github.io/edd/", black, 19, "Arial", False, True, 125, 311)

    voltar()

def voltar():
    while True:
        pygame.draw.rect(background, black, [300, 450, 80, 30])
        text("Menu", yellowGreen, 18, "Arial", False, True, 317, 453)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                saindo()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0] 
                y = pygame.mouse.get_pos()[1] 

                if x > 300 and y > 450 and x < 380 and y < 480:
                    menu()

        pygame.display.update()    

def menu():
    while True:
        background.fill(yellowGreen)

        text("S n a k e", black, 50, "freesansbold.ttf", False, False, 140, 50)
        text("___________________________", black, 20, "Arial", True, False, 60, 70)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                saindo()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0] 
                y = pygame.mouse.get_pos()[1]

                if x > 112 and y > 150 and x < 297 and y < 192:
                    # Jogar;
                    jogo()

                if x > 112 and y > 210 and x < 297 and y < 252:
                    # Intruções;
                    instrucoes()

                if x > 112 and y > 270 and x < 297 and y < 312:
                    # Configurações;
                    configuracoes()

                if x > 112 and y > 330 and x < 297 and y < 372:
                    # Créditos;
                    creditos()

        pygame.draw.rect(background, black, [112, 150, 185, 42])
        text("Jogar", yellowGreen, 25, "Arial", False, True, 170, 155)

        pygame.draw.rect(background, black, [112, 210, 185, 42])
        text("Instruções", yellowGreen, 25, "Arial", False, True, 142, 215)

        pygame.draw.rect(background, black, [112, 270, 185, 42])
        text("Configurações", yellowGreen, 25, "Arial", False, True, 122, 275)

        pygame.draw.rect(background, black, [112, 330, 185, 42])
        text("Créditos", yellowGreen, 25, "Arial", False, True, 155, 335)


        pygame.display.update()

# A função menu consegue integrar tudo;
menu()


# Saindo do Jogo.
# pygame.quit()
# quit()