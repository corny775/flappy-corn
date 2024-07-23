import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
fps = 50
screen_width = 764
screen_height = 836

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Corn')

#define font
font = pygame.font.SysFont('Comic Sans MS', 50)
font2 = pygame.font.SysFont('Comic Sans MS', 20)
#define colour
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

#define game variables
ground_scroll = 0
scroll_speed = 4
flying = False

game_over = False
pipe_gap = 325
pipe_frequency = 1550 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
#load images
bg = pygame.image.load('correctfied3.png')
ground_img = pygame.image.load('ground.jpg')
button_img = pygame.image.load('correctrestar2.png')

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
def draw_text2(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height*3/8)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 2):
            img = pygame.image.load(f'Bird100{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):

        if flying == True:
            #gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 690:
                self.rect.y += int(self.vel)
        if game_over == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = False

            #handle the animation
            self.counter += 1
            flap_cooldown = 5
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            #rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index], -(self.vel))
        else:
            self.image = pygame.transform.rotate(self.images[self.index], 0)
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pringle8.png')
        self.rect = self.image.get_rect()
        #position 1 is from the top, -1 from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap*3/8)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap*3/8)]
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()
        #check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if score == 0:
                draw_text2("A light wind swept over the corn,", font2, white, 215, 365)
                draw_text2("and all nature laughed in the sunshine", font2, white, 200, 395)
        if (score > 0 and score <= 2):
                draw_text2("All the candy corn that was ever", font2, white, 215, 365)
                draw_text2("made was made in 1911", font2, white, 250, 395)
        if (score > 2 and score <= 4):
                draw_text2("The day of fortune is like", font2, white, 245, 350)
                draw_text2("a harvest day,", font2, white, 300, 375)
                draw_text2("we must be busy when the corn is ripe", font2, white, 191, 400)
        if (score > 4 and score <= 6):
                draw_text2("I know my corn plants intimately,", font2, white, 215, 350)
                draw_text2("and I find it a great pleasure to know ", font2, white, 195, 370)
                draw_text2("them", font2, white, 340, 390)
        if (score > 6 and score <= 8):
                draw_text2("There's a fine line between", font2, white, 235, 355)
                draw_text2("patriotism and corn", font2, white, 273, 395)
        if (score > 8 and score <= 10):
                draw_text2("Manufacturing is the seed corn", font2, white, 220, 355)
                draw_text2("for others jobs in the US", font2, white, 245, 390)
        if (score > 10 and score <= 12):
                draw_text2("Corn is a greedy crop,", font2, white, 265, 355)
                draw_text2("as farmers will tell you", font2, white, 258, 390)
        if (score > 12 and score <= 14):
                draw_text2("Today's smartest advertising", font2, white, 230, 355)
                draw_text2("style is tomorrow's corn", font2, white, 252, 390)
        if (score > 14 ):
                draw_text2("you were ok", font2, white, 297, 375)
        draw_text2("exit button is to restart :)", font2, green, 430, 690)
        return action
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height*3/8))
bird_group.add(flappy)

#create restart button instance
button = Button((screen_width/2)-200, (screen_height/2)-175, button_img)

run = True
while run:
    clock.tick(fps)
    #drawing background
    screen.blit(bg,(0,0))
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    #draw the ground
    screen.blit(ground_img, (ground_scroll, 680))
    #check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
           and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
           and pass_pipe == False:
           pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
    
    draw_text(str(score), font, red, 100, 675)
    
    #look for collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    #check if corn hit the ground
    if flappy.rect.bottom >= 690:
        game_over = True
        flying = False
    if game_over == False and flying == True:
        #generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(screen_width, int(screen_height*3/8) + pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height*3/8) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        #draw and scroll ground
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pipe_group.update()

    #check for game over and reset
    if game_over == True:
        
        if button.draw() == True:
            
            game_over = False
            score = reset_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    pygame.display.update()
pygame.quit()