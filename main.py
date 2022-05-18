import pygame

pygame.init()
screen = pygame.Surface((700, 500))
window = pygame.display.set_mode((700, 500))
goal = pygame.Surface((50, 50))
fire = pygame.Surface((30, 30))
player = pygame.Surface((50, 50))

background = pygame.image.load("background.webp")
goalImg = pygame.image.load("goal.png")
fireImg = pygame.image.load("fire.png")
playerImg = pygame.image.load("player.png")

goal.set_colorkey((0, 0, 0))
fire.set_colorkey((0, 0, 0))
player.set_colorkey((0, 0, 0))

x_goal = 0
y_goal = 0

x_fire = 1000
y_fire = 1000

x_player = 350
y_player = 450

done = False
coordinatesGoal = True
strike = 0
strikeCount = 10
count = 0

font = pygame.font.SysFont("Arial", 24)
win = pygame.font.SysFont("Arial", 50)

messageStr = ''

def hittingTarget(x1, y1, x2, y2, db1, db2):
    if x1 > x2-db1 and x1 < x2+db2 and y1 > y2-db1 and y1 < y2+db2:
        return 1
    else:
        return 0
    
while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            if y_player == 460:
                y_player = 460
            else: y_player += 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            if y_player == 100:
                y_player = 100
            else: y_player -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            if x_player == 10:
                x_player = 10
            else: x_player -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            if x_player == 650:
                x_player = 650
            else: x_player += 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if strike < 10:
                strike += 1
                strikeCount -= 1
                x_fire = x_player
                y_fire = y_player - 40   

    if strike:
        y_fire -= 1
        
    if hittingTarget(x_fire, y_fire, x_goal, y_goal, 30, 30):
        count += 1
        x_fire = 1000
        y_fire = 1000
        
    if coordinatesGoal:
        x_goal += 0.5
        if x_goal > 660:
            x_goal -= 0.5
            coordinatesGoal = False
    else:
        x_goal -= 0.5
        if x_goal < 0:
            x_goal += 0.5
            coordinatesGoal = True
    if y_fire == 0 and strike == 10:
        if count > 0:
            messageStr = 'You win! Yours hits: ' + str(count)
        else:
            messageStr = 'You lose( Try again!'
            
    string = font.render('Hits: ' + str(count), 0, (0, 0, 0))
    stringAttempts = font.render('Attempts left: ' + str(strikeCount), 0, (0, 0, 0))
    message = win.render(messageStr, 0, (0, 0, 0))
    screen.blit(background, (0,0))
    goal.blit(goalImg, (0, 0))
    fire.blit(fireImg, (0, 0))
    player.blit(playerImg, (0, 0))
    screen.blit(string, (600, 50))
    screen.blit(stringAttempts, (525, 75))
    screen.blit(goal, (x_goal, y_goal))
    screen.blit(player, (x_player, y_player))
    screen.blit(fire, (x_fire, y_fire))
    screen.blit(message, (150, 250))
    window.blit(screen, (0,0))
    pygame.display.update()
pygame.quit()
