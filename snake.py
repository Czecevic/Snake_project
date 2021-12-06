import pygame
import random
import time

pygame.init()


#attribue des couleurs 
white = (255, 255, 255)
black=(0,0,0)
green = (0,255,0)

#dimension de la fenêtre 
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake ta race bordel')

clock = pygame.time.Clock()
#snake_block definit la taille du serpent et snake_speed la vitesse
snake_block = 10
snake_speed = 15

#definit la typo utiliser et la taille de la police
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#le score
def Your_score(score):
    value = score_font.render(str(score), True, white)
    dis.blit(value, [0, 0])

#le serpent
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

#le message 
def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width/6, dis_height/3])

#la boucle nous permettant de créer les mouvements du serpent et 
# mettre aussi en relation les definitons utiliser juste avant 
def gameLoop(): 
    game_over = False #le jeu est terminer s'il est égal à "True"
    game_close = False #la fenêtre se ferme s'il est égal à "True"

    x1 = dis_width / 2 #la longueur de la fenêtre divisé par 2 
    y1 = dis_height / 2 #la largeur de la fenêtre divisé par 2

    x1_change = 0 #initalise l'axe x
    y1_change = 0 #initalise l'axe y

    snake_List = []
    Length_of_snake = 1 #taille du serpent, un snake_block est égal à 1

    #nous mettons en place la nourriture de façon aléatoire sur les deux axes présent (x et y)
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # tant que le jeu n'est pas terminé, nous continuons 
    # à effectuer chacune des actions suivantes 
    while not game_over:
        #tant que le jeu est perdu alors nous affichons 
        # le message et nous laissons le choix entre deux possibilités :
        # - appuyer sur le bouton C pour rejouer
        # - appuyer sur le bouton Q pour quitter

        while game_close == True:
            dis.fill(black)
            message('Game Over! \n r - rejouer \n Q - quitter', white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
        #pour chaque evenement se déroulant dans le jeu nous laissons plusieurs choix :
        # - si l'evenement en question est arrêter (game_over == Vrai) 
        # alors nous arrêtons le jeu
        # - si nous cliquons sur un bouton du clavier, 
        # cela nous offre la possiblité d'effectuer une action
        # (haut, bas, gauche, droite qui se traduit par K_<haut>, K_<bas>, etc)
        # - via ces touches nous offrons une action basé sur les deux axes (x et y) offrant 4 choix :
        # haut = x bas = -x gauche = -y droite = y
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block
        # si le serpent touche le bord du "tableau" alors le game_close devient vrai et nous arrêtons le jeu
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        #on incremment l'axe x et y via deux autre variable utiliser pour aligner les mouvemments et deplacements de chaque action basé sur le snake 
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block]) #dessine le serpent(tableau, couleur, [axe x, axe y, largeur du serpent, longueur du serpent])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        #snake_head sera notre serpent mais au niveau de la matière physique avec des append 
        #permet de lancer le jeu
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10
            Length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
 