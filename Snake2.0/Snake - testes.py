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

largura = 400
altura = 500

tamanho = 10

placar = 40

relogio = pygame.time.Clock()

# Criando a tela;
background = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")


def text(msg, color, tam, fonte, tof, fot, x, y):
    font = pygame.font.SysFont(fonte, tam, bold=tof, italic=fot)
    texto1 = font.render(msg, True, color)
    background.blit(texto1, [x, y])

# Funções;
def snake(snakeXY):
    for XY in snakeXY:
        pygame.draw.rect(background, red, [XY[0], XY[1], tamanho, tamanho])

def maca(cor, maca_x, maca_y):
    pygame.draw.rect(background, cor, [maca_x, maca_y, tamanho, tamanho])

def jogo():
    jogar = True
    gameOver = False

    # Definindo a posição da cobra e da maçã;
    pos_x = randrange(0, largura - tamanho, 10)
    pos_y = randrange(0, altura - tamanho - placar, 10)

    maca_x = randrange(0, largura - tamanho, 10)
    maca_y = randrange(0, altura - tamanho - placar, 10)

    randcolor = ( randint(1,254), randint(1,254), randint(1,254) ) 

    velocidade_x = 0
    velocidade_y = 0
    snakeXY = []
    snakeLen = 1

    # loop;
    while jogar:

        # Fazendo o nosso fim de jogo;
        while gameOver:
            background.fill(yellowGreen)
            text("F i m  d e  j o g o", black, 35, "Arial", True, False, 70, 50)
            text("para continuar tecle C ou S para sair", black, 30, "Roboto", False, True, 20, 450)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogar = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogar = True
                        gameOver = False

                        # Definindo a posição da cobra e da maçã;
                        pos_x = randrange(0, largura - tamanho, 10)
                        pos_y = randrange(0, altura - tamanho - placar, 10)

                        maca_x = randrange(0, largura - tamanho, 10)
                        maca_y = randrange(0, altura - tamanho - placar, 10)

                        velocidade_x = 0
                        velocidade_y = 0
                        snakeXY = []
                        snakeLen = 1

                    if event.key == pygame.K_s:
                        jogar = False
                        gameOver = False

        # Verificação da requisição de saída;
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogar = False

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

                if event.key == pygame.K_SPACE:
                    snakeLen += 1

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

                randcolor = ( randint(1,254), randint(1,254), randint(1,254) ) 

                snakeLen += 1

            # Verificando colisão;
            if any(Block == snakeHead for Block in snakeXY[:-1]):
                gameOver = True

            # if len(snakeXY) >= 2:
            #     # Se a cobra tiver mais de 2 quadradinhos de comprimento
            #     if snakeXY.count(snakeXY[0]) > 1:
            #         # Se a cabeça da cobra (1° elemento da lista) aparecer mais de uma vez na lista
            #         gameOver = True  # Fecho o jogo

            # Fazendo a cobra retornar para a tela;
            if pos_x + tamanho > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x = largura - tamanho

            if pos_y + tamanho > altura - placar:
                pos_y = 0
            if pos_y < 0:
                pos_y = altura - tamanho - placar

            # Encerrando o jogo ao encostar na borda;
            # if pos_x + tamanho > largura:
            #     gameOver = True
            # if pos_x < 0:
            #     gameOver = True

            # if pos_y + tamanho > altura:
            #     gameOver = True
            # if pos_y < 0:
            #     gameOver = True

            # Desenhando o bloco de pontos;
            pygame.draw.rect(background, yellowGreen, [0, altura-placar, largura, placar])
            text("Pontos: "+str(snakeLen - 1), black, 20, "sans", True, False, 10, altura-30)

            # Atualização da tela;
            pygame.display.update()
            relogio.tick(15)

jogo()

# Saindo do Jogo.
pygame.quit()
quit()