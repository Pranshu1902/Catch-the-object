import pygame
import random

pygame.init()

red = [255,0,0]
green = (0, 255, 0)
blue = (0, 0, 128)
light_blue = [0,0,255]

score = 0

dis = pygame.display.set_mode((280,500))

# starting page
img = pygame.image.load('intro.png')

pygame.draw.rect(dis, red, [80,10,180,50])

dis.blit(img, (5,100))
font3 = pygame.font.Font('freesansbold.ttf', 40)

text3 = font3.render('Start', True, green, red)

textRect3 = text3.get_rect()  
textRect3.center = (170, 35)

dis.blit(text3, textRect3)
pygame.display.update()



dis.fill([255,255,255])

player = pygame.image.load('player.png') # 64 X 64 image

# player's coordinates
x = 100
y = 400

font = pygame.font.Font('freesansbold.ttf', 20)
value = font.render("Your Score: " + str(score), True, green, blue)
dis.blit(value, [350, 35])

# object coordinates

x_list = [30, 110, 190]

x_object = random.choice(x_list)

dis.blit(player, (x,y))

y_object_old = 10
y_object = 10

# background
bg = pygame.image.load('bg2.jpg')
dis.blit(bg, (0,0))

run = True

def game(run, x,y,x_list, x_object, y_object, y_object_old, score, goal):
    while run:
        pygame.time.delay(100)
        dist = 80
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        # motion of player
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x >80:
            x -= dist
        elif keys[pygame.K_RIGHT] and x<180:
            x += dist

    
    
        pygame.draw.rect(dis, red, (x_object, y_object_old, 50,50))
    
        if y_object_old < 440:
            y_object_old+=90
        elif y_object_old > 440:
            y_object_old = 10
            x_object = random.choice(x_list)
        
        dis.fill([255,255,255])
        dis.blit(bg, (0,0))
        pygame.draw.rect(dis, light_blue, (x_object, y_object_old, 50,50))
        value = font.render("Your score: "+str(score), True, green, red)
        goal_text = font.render("Goal: "+str(goal), True, green, red)

        font2 = pygame.font.Font('freesansbold.ttf', 40)
        lose_text = font2.render("You Lost", True, green, red)
        win_text = font2.render("You Won", True, green, red)
        dis.blit(goal_text, [10,10])
        dis.blit(value, [150, 35])
        dis.blit(player, (x,y))


    
        if y_object_old + 20 >= y:
        
            # catching
            if x_object >= x and x_object <= x+64:
                score+=1
            
            # missing
            else:
                dis.fill([255,255,255])
                dis.blit(player, (x,y))
                pygame.draw.rect(dis, light_blue, (x_object, y_object_old, 50, 50))
                value = font.render("Your Score: " + str(score), True, green, red)
                dis.blit(value, [150,35])
                dis.blit(lose_text, [50,200])
                pygame.display.update()
                pygame.time.delay(500)
                run = False

        # winning
        if goal == score:
            dis.fill([255,255,255])
            dis.blit(win_text, [50,200])
            pygame.display.update()
            pygame.time.delay(500)

    
    
        pygame.display.update()


    pygame.quit()


while True:
    x, y = pygame.mouse.get_pos()
    

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x <= 280 and x >= 80 and y <= 60 and y >= 10:
                dis.fill([0,0,0])
                white = [255,255,255]

                font5 = pygame.font.Font('freesansbold.ttf', 30)
                value5 = font5.render("Choose your goal", True, green, blue)
                dis.blit(value5, [10, 60])

                pygame.draw.rect(dis, [0,255,0], [70,150,120,50])
                font_goal = pygame.font.Font('freesansbold.ttf', 20)
                value = font5.render("25", True, white, green)
                dis.blit(value, [110, 160])
                
                pygame.draw.rect(dis, [0,0,128], [70,230,120,50])
                value = font5.render("50", True, white, blue)
                dis.blit(value, [110, 240])
                
                pygame.draw.rect(dis, [255,0,0], [70,310,120,50])
                value = font5.render("75", True, white, red)
                dis.blit(value, [110, 320])
                
                pygame.display.update()

                while True:
                    x1, y1 = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if x1<=190 and x1>= 70 and y1<= 200 and y1>=150:
                                game(True, 100,400,[30,110,190],x_object,10,10,0, 25)
                            elif x1<=190 and x1>= 70 and y1<= 280 and y1>=230:
                                game(True, 100,400,[30,110,190],x_object,10,10,0, 50)
                            elif x1<=190 and x1>= 70 and y1<= 360 and y1>=310:
                                game(True, 100,400,[30,110,190],x_object,10,10,0, 75)
