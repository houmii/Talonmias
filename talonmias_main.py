# Imports here:
from __future__ import barry_as_FLUFL
from json import load
from math import pi
from operator import index
from re import S
import time
from turtle import speed
import pygame
from pygame import mixer
import sys
from pygame.locals import *
pygame.init()
import random # added for hazard spawn positon and time

# ███▀▀██▀▀███        ▀███                                        ██
# █▀   ██   ▀█          ██
#      ██     ▄█▀██▄    ██   ▄██▀██▄▀████████▄ ▀████████▄█████▄ ▀███  ▄█▀██▄  ▄██▀███ Coders:
#      ██    ██   ██    ██  ██▀   ▀██ ██    ██   ██    ██    ██   ██ ██   ██  ██   ▀▀
#      ██     ▄█████    ██  ██     ██ ██    ██   ██    ██    ██   ██  ▄█████  ▀█████▄
#      ██    ██   ██    ██  ██▄   ▄██ ██    ██   ██    ██    ██   ██ ██   ██  █▄   ██
#    ▄████▄  ▀████▀██▄▄████▄ ▀█████▀▄████  ████▄████  ████  ████▄████▄████▀██▄██████▀
#------------------------------------------------------------------------------------

#-----------------------------
# Game name

pygame.display.set_caption("Talonmias")

#-----------------------------

clock = pygame.time.Clock()

screen_size = pygame.display.set_mode((1200,  900))
bg_image_pos = (0,0)
pygame.mixer.music.set_volume(0.4)
mixer.music.load('toimintaa.wav')
splat= pygame.mixer.Sound('splat.mp3')
ouch=pygame.mixer.Sound('ouch.mp3')
firing = pygame.mixer.Sound('pulse_rifle.mp3')

mixer.music.play(-1)

# character walk animations saved in list --------------------------------
walkUp = [pygame.image.load("run_u_0.png"), pygame.image.load("run_u_1.png"), pygame.image.load("run_u_2.png"), pygame.image.load("run_u_3.png"), pygame.image.load("run_u_4.png"), pygame.image.load("run_u_5.png")]
walkDown = [pygame.image.load("run_d_0.png"), pygame.image.load("run_d_1.png"), pygame.image.load("run_d_2.png"), pygame.image.load("run_d_3.png"), pygame.image.load("run_d_4.png"), pygame.image.load("run_d_5.png")]
walkLeft = [pygame.image.load("run_l_0.png"), pygame.image.load("run_l_1.png"), pygame.image.load("run_l_2.png"), pygame.image.load("run_l_3.png"), pygame.image.load("run_l_4.png"), pygame.image.load("run_l_5.png"), pygame.image.load("run_l_6.png"), pygame.image.load("run_l_7.png")]
walkRight = [pygame.image.load("run_r_0.png"), pygame.image.load("run_r_1.png"), pygame.image.load("run_r_2.png"), pygame.image.load("run_r_3.png"), pygame.image.load("run_r_4.png"), pygame.image.load("run_r_5.png"), pygame.image.load("run_l_6.png"), pygame.image.load("run_l_7.png")]
char_stand_still = [pygame.image.load("talonmies_idle_1.png"), pygame.image.load("talonmies_idle_2.png"), pygame.image.load("talonmies_idle_1.png"), pygame.image.load("talonmies_idle_2.png")]
attack_r = [pygame.image.load("talonmies_harja_1.png"), pygame.image.load("talonmies_harja_2.png"), pygame.image.load("talonmies_harja_1.png"), pygame.image.load("talonmies_harja_2.png")]
attack_r = [pygame.image.load("talonmies_harja_1.png"), pygame.image.load("talonmies_harja_2.png"), pygame.image.load("talonmies_harja_1.png"), pygame.image.load("talonmies_harja_2.png")]

# --------------------------------------------------------------
#hazard explosion
explosion = [pygame.image.load("explosion/frame_0.png"),
             pygame.image.load("explosion/frame_1.png"),
             pygame.image.load("explosion/frame_2.png"),
             pygame.image.load("explosion/frame_3.png"),
             pygame.image.load("explosion/frame_4.png"),
             pygame.image.load("explosion/frame_5.png"),
             pygame.image.load("explosion/frame_6.png"),
             pygame.image.load("explosion/frame_7.png"),
             pygame.image.load("explosion/frame_8.png"),
             pygame.image.load("explosion/frame_09.png"),
             pygame.image.load("explosion/frame_10.png"),
             pygame.image.load("explosion/frame_11.png"),
             pygame.image.load("explosion/frame_12.png")]

#flamethrower flame images
flames_r = [pygame.image.load("flames/flame_0_r.png").convert_alpha(),
          pygame.image.load("flames/flame_1_r.png").convert_alpha(),
          pygame.image.load("flames/flame_2_r.png").convert_alpha(),
          pygame.image.load("flames/flame_3_r.png").convert_alpha()]

flames_l = [pygame.image.load("flames/flame_0_l.png").convert_alpha(),
          pygame.image.load("flames/flame_1_l.png").convert_alpha(),
          pygame.image.load("flames/flame_2_l.png").convert_alpha(),
          pygame.image.load("flames/flame_3_l.png").convert_alpha()]


#---------------------------------------------
# Colors

BLACK = (0,0,0) # Lots of there colors are to satisfaction meter
COLOR = (255, 100, 98) # Color for original spawn/object script
WHITE = (255,255,255)
GREENYELLOW = (143,245,34)
YELLOW = (234, 245, 34)
GREY = (210,210,210)
DARKGREY = (93,94,94)
RED = (255,0,0)
GREEN = (0,255,0)
GREENLIGHT = (76,230,0)
REDORANGE = (245,103,32)
YELLOWLIGHT = (230,230,0)
color = (255, 255, 255) # Color for timer

#Tiles and objects of level

seina_yla = pygame.image.load("seina_tile_ylareunus.png").convert_alpha()
seina_yla_oikea = pygame.image.load("seina_tile_ylareunus_oikea.png").convert_alpha()
seina_muuri_vasen = pygame.image.load("tile_muuri_vasen.png")
seina_muuri_oikea = pygame.image.load("tile_muuri_oikea.png")
seina_muuri_oikea_ylakulma = pygame.image.load("tile_muurisivu_reuna_o_ylakulma.png")
seina_muuri_vasen_ylakulma = pygame.image.load("tile_muurisivu_reuna_v_ylakulma.png")
seina_muuri_vasen_alakulma = pygame.image.load("tile_muurisivu_reuna_v_alakulma.png")
seina_muuri_oikea_alakulma = pygame.image.load("tile_muurisivu_reuna_o_alakulma.png")
tile_reunat = pygame.image.load("tile.png").convert_alpha()
tile_verta = pygame.image.load("tile_verta.png").convert_alpha()
seina_muuri_ala = pygame.image.load("tile_muuri_ala.png")
seina_ovet = pygame.image.load("seina_ovet.png")
seina_likainen = pygame.image.load("seina_tile_likainen.png")
tile_ruutu = pygame.image.load("tile_ruutu.png")
tile_ruutu_murtuma = pygame.image.load("tile_ruutu_murtuma.png")
seina_ilmastointi = pygame.image.load("seina_ilmastointi.png")
seina_ikkunat = pygame.image.load("seina_ikkunat.png")
seina_putki = pygame.image.load("seina_tile_putki.png")
seina_verta = pygame.image.load("seina_verta.png")

#Decorations of level

ikkuna = pygame.image.load("Koristeet/ikkuna.png").convert_alpha()
ilmastointi = pygame.image.load("Koristeet/ilmastointi.png").convert_alpha()
kyltti = pygame.image.load("Koristeet/kyltti.png").convert_alpha()
kynttila = pygame.image.load("Koristeet/kynttila.png").convert_alpha()
pensas = pygame.image.load("Koristeet/pensas.png").convert_alpha()
anturipylvas = pygame.image.load("Koristeet/pylvas_anturi.png").convert_alpha()
paneelipylvas = pygame.image.load("Koristeet/pylvas_paneelit.png").convert_alpha()
poyta = pygame.image.load("Koristeet/poyta.png").convert_alpha()
poyta_tuoli =pygame.image.load("Koristeet/poyta_tuoli.png").convert_alpha()
tuoli = pygame.image.load("Koristeet/tuoli.png").convert_alpha()
roskakori = pygame.image.load("Koristeet/roskis.png").convert_alpha()
ruoho = pygame.image.load("Koristeet/ruohoo.png").convert_alpha()
stand = pygame.image.load("Koristeet/stand_iso.png").convert_alpha()
stand_2 = pygame.image.load("Koristeet/stand_2.png").convert_alpha()
automaatti = pygame.image.load("Koristeet/vendingmachine.png").convert_alpha()

def give_level():

    #Size of tiles
    TILEWIDTH = 64  # holds the tile width and height

    for row_nb, row in enumerate(map_data):
        for col_nb, tile in enumerate(row):
            if tile == 0:
                tileImage = tile_reunat
            if tile == 1:
                tileImage = seina_yla_oikea
            if tile == 2:
                tileImage = tile_verta
            if tile == 3:
                tileImage = tile_ruutu
            if tile == 5:
                tileImage = seina_yla
            if tile == 6:
                tileImage = seina_muuri_ala
            if tile == 7:
                tileImage = seina_ovet
            if tile == 8:
                tileImage = seina_likainen
            if tile == 9:
                tileImage = seina_muuri_vasen
            if tile == 10:
                tileImage = seina_muuri_oikea
            if tile == 11:
                tileImage = seina_muuri_oikea # Have to check out if this image is correct
            if tile == 13:
                tileImage = tile_ruutu_murtuma
            if tile == 14:
                tileImage = seina_ilmastointi
            if tile == 15:
                tileImage = seina_putki
            if tile == 16:
                tileImage = seina_ikkunat
            if tile == 17:
                tileImage = seina_verta
            if tile == 18:
                tileImage = seina_muuri_vasen_alakulma
            if tile == 19:
                tileImage = seina_muuri_oikea_alakulma


            cart_y = 45 + row_nb * TILEWIDTH  #
            cart_x = 216 + col_nb * TILEWIDTH

            screen_size.blit(tileImage, (cart_x, cart_y)) # Tile and location

def give_decorations():

    screen_size.blit(tuoli, [673, 431])
    screen_size.blit(tuoli, [519, 358])
    screen_size.blit(poyta, [650, 398])
    screen_size.blit(poyta_tuoli, [450, 360])
    screen_size.blit(ilmastointi, [590, 76])
    screen_size.blit(roskakori, [837, 130])
    screen_size.blit(roskakori, [870, 161])
    screen_size.blit(stand, [320, 542])
    screen_size.blit(stand_2, [839, 420])
    screen_size.blit(tuoli, [831, 499])
    screen_size.blit(automaatti, [300, 90])
    screen_size.blit(poyta_tuoli, [736, 590])
    screen_size.blit(poyta, [579, 560])
    screen_size.blit(pensas, [281, 147])
    screen_size.blit(tuoli, [609, 527])
    screen_size.blit(tuoli, [592, 570])

# Level 1 map
map_data = [
[9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10], #1
[9, 16, 16, 7, 17, 14, 8, 8, 8, 15, 8, 10], #2
[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10], #3
[9, 0, 3, 3, 13, 3, 3, 13, 3, 3, 0, 10], #4
[9, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 10], #5
[9, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 10], #6
[9, 0, 3, 0, 0, 2, 0, 0, 0, 3, 0, 10], #7
[9, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 10], #8
[9, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 10], #9
[9, 0, 3, 3, 13, 3, 3, 3, 3, 3, 0, 10], #10
[9, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 10], #11
[18, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 19] #12
]#

#----------------------------------------------
# player class
class enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.explosionCount = 0
        self.explosiondone = False
        self.explosion_x = 0
        self.explosion_y = 0

    def draw(self, screen):

        if self.explosionCount + 1 >= 24:
            global meter_points
            global meter_points_delta
            global cleaning_score

            if meter_points > 80:
               meter_points_delta = (100 - meter_points)
               meter_points = meter_points + meter_points_delta

            else:
                meter_points += 20

            cleaning_score += 100
            self.explosionCount = 0
            hazard_coord_list_x.pop(i)
            hazard_coord_list_y.pop(i)
            hazard_list.pop(i)
            splat.play()

        elif screen.blit(explosion[self.explosionCount//4], (hazard_coord_list_x[i], hazard_coord_list_y[i])):
             self.explosionCount += 1

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpHeight = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standStill = 0
        self.attack = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()

        self.sprites = []
        self.sprites.append(pygame.image.load('run_u_0.png'))
        self.sprites.append(pygame.image.load('run_u_1.png'))
        self.sprites.append(pygame.image.load('run_u_2.png'))
        self.sprites.append(pygame.image.load('run_u_3.png'))
        self.sprites.append(pygame.image.load('run_u_4.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.mask = pygame.mask.from_surface(self.image)

        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.attack = False
        self.flame = False
        self.standStill = False
        self.is_shoot = False
        self.walk_right = False
        self.walk_left = False
        self.direction = 0

        self.attackCount = 0
        self.walkCount = 0
        self.shoot_cooldown = 0
        self.flame_count = 0

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.speedx = 5
        self.speedy = 5

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 7
            bullet = Bullet(self.rect.centerx, self.rect.centery, player.direction)
            bullets.add(bullet)
            firing.play()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def get_keys(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shoot()

        if keys[pygame.K_LEFT] and self.rect.x > 200 + 70:
            self.rect.x -= self.speedx
            self.left = True
            self.right = False
            self.direction = -1

        elif keys[pygame.K_RIGHT] and self.rect.x < 920 - 30:
            self.rect.x += self.speedx
            self.left = False
            self.right = True
            self.direction = 1

        elif keys[pygame.K_UP] and self.rect.y > 45 + 90:
            self.rect.y -= self.speedy
            self.up = True
            self.left = False
            self.right = False
            self.down = False
            self.direction = -2

        elif keys[pygame.K_DOWN] and self.rect.y < 720 - 20:
            self.rect.y += self.speedy
            self.up = False
            self.down = True
            self.left = False
            self.right = False
            self.direction = 2

        elif keys[pygame.K_LCTRL]:
            self.attack = True
            self.left = False
            self.right = False
            self.up = False
            self.down = False

        elif keys[pygame.K_f]:
            if self.direction == 1 or self.direction == -1:
                self.flame = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False

        else:
            self.right = False
            self.left = False
            self.is_shoot = False
            self.up = False
            self.down = False
            self.attack = False
            self.flame = False
            self.walkCount = 0
            self.attackCount = 0
            self.flameCount = 0

    def update(self, screen):

        if self.walkCount + 1 >= 12:
            self.walkCount = 0

        if self.standStill + 1 >= 12:
            self.standStill = 0

        if self.attackCount + 1 >= 12:
            self.attackCount = 0

        if self.flameCount + 1 >= 12:
            self.flameCount = 0


        if self.left:
            screen.blit(walkLeft[self.walkCount//2], (self.rect.x, self.rect.y))
            self.walkCount += 1

        elif self.right:
            screen.blit(walkRight[self.walkCount//2], (self.rect.x, self.rect.y))
            self.walkCount += 1

        elif self.up:
            screen.blit(walkUp[self.walkCount//3], (self.rect.x, self.rect.y))
            self.walkCount += 1

        elif self.down:
            screen.blit(walkDown[self.walkCount//3], (self.rect.x, self.rect.y))
            self.walkCount += 1

        elif self.attack:
            screen.blit(attack_r[self.attackCount//3], (self.rect.x, self.rect.y))
            self.attackCount += 1

        elif self.flame:
            if self.direction == 1:
                screen.blit(flames_r[self.flameCount//3], (self.rect.centerx + 10, self.rect.centery - 40))
                screen.blit(walkRight[0], (self.rect.x, self.rect.y))
                self.flameCount += 1

            if self.direction == -1:
                screen.blit(flames_l[self.flameCount//3], (self.rect.centerx - 132, self.rect.centery - 32))
                screen.blit(walkLeft[0], (self.rect.x, self.rect.y))
                self.flameCount += 1

        else:
            screen.blit(char_stand_still[self.standStill//4], (self.rect.x, self.rect.y))
            self.standStill += 1

enemy = enemy(0, 0)


class MovingEnemy(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.sprites = []

        self.sprites.append(pygame.image.load('zombie/z_1.png'))
        self.sprites.append(pygame.image.load('zombie/z_2.png'))
        self.sprites.append(pygame.image.load('zombie/z_3.png'))
        self.sprites.append(pygame.image.load('zombie/z_4.png'))
        self.sprites.append(pygame.image.load('zombie/z_5.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        #self.rect.center = [pos_x, pos_y]
        self.speedx = 2
        self.speedy = 2


    def update(self):

        #checking collision between player and moving enemy zombie
        hits = pygame.sprite.spritecollide(self, all_sprites_player, False, pygame.sprite.collide_mask)

        if hits:
            print("Osui")
            print("ja upposi")

        self.current_sprite += 1
        if int(self.current_sprite) >= (len(self.sprites)):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x > 800:
            self.speedx = -2
        if self.rect.x < 400:
            self.speedx = 2
        if self.rect.y < 100:
            self.speedy = 2
        if self.rect.y > 500:
            self.speedy = -2


class Flames(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 20
        self.speedy = 10
        self.direction = direction

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,5))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 20
        self.speedy = 10
        self.direction = direction

    def update(self):

        if self.direction == 2 or self.direction == -2:
            self.rect.y += (self.direction * self.speedy)
        else:
            self.rect.x += (self.direction * self.speedx)
        if self.rect.x < 0:
            self.kill()
        if self.rect.x > 1280:
            self.kill()
        if self.rect.y < 0:
            self.kill()
        if self.rect.y > 900:
            self.kill()

#sprite groups
all_sprites_enemies = pygame.sprite.Group()
all_sprites_player = pygame.sprite.Group()
moving_enemy = MovingEnemy(400,450)
player = Player(400,400)
bullets = pygame.sprite.Group()
all_sprites_enemies.add(moving_enemy)
all_sprites_player.add(player)

#---------------------------------------------
# Game Over variables here:

game_over_state = False

game_over_text_pos = (345, 300)
replay_text_pos = (295, 390)
final_score_text_pos = (345, 510)

game_over_outline_pos = (345, 310)
replay_outline_pos = (295, 400)
final_score_outline_pos = (345, 520)

def game_over_screen():
        # let's set global variables so we can access them from here
        global game_over_state
        global meter_points
        global time_left
        global hazard_coord_list
        global cleaning_score
        global game_over_text_pos
        global replay_text_pos
        global final_score_text_pos
        global game_over_outline_pos
        global replay_outline_pos
        global final_score_outline_pos

        screen_size.blit(bg_image,(0,0))

        # Black outline for text
        font= pygame.font.SysFont(None, 120)
        game_over_outline = font.render(str("GAME OVER"), True, (BLACK))
        screen_size.blit(game_over_outline, (game_over_text_pos)) # Text location

        retry_outlie = font.render(str("Press R to replay"), True, (BLACK))
        screen_size.blit(retry_outlie, (replay_outline_pos)) # Text location

        font_SCORE= pygame.font.SysFont(None, 120)
        final_score_outline = font_SCORE.render(("SCORE: ") + str(cleaning_score), True, (BLACK))
        screen_size.blit(final_score_outline, (final_score_outline_pos)) # Text location

        # The overlay text
        font= pygame.font.SysFont(None, 120)
        game_over_text = font.render(str("GAME OVER"), True, (255, 250, 0))
        screen_size.blit(game_over_text, (game_over_text_pos)) # Text location

        font= pygame.font.SysFont(None, 120)
        retry_text = font.render(str("Press R to replay"), True, (255, 250, 0))
        screen_size.blit(retry_text, (replay_text_pos)) # Text location

        font_SCORE= pygame.font.SysFont(None, 120)
        final_score = font_SCORE.render(("SCORE: ") + str(cleaning_score), True, (GREEN))
        screen_size.blit(final_score, (final_score_text_pos)) # Text location

        screen_size.blit(bg_image,(0,0))
        screen_size.blit(game_over_outline, (game_over_outline_pos))
        screen_size.blit(retry_outlie, (replay_outline_pos))
        screen_size.blit(final_score_outline,(final_score_outline_pos))
        screen_size.blit(game_over_text, (game_over_text_pos))
        screen_size.blit(retry_text, (replay_text_pos))
        screen_size.blit(final_score,(final_score_text_pos))
        pygame.display.flip()

        #waiting user input to restart the game or quit
        waiting = True
        while waiting:
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit(); sys.exit()
                if event.type == KEYUP:
                    if event.key == K_r:
                        waiting = False

        # let's clear lists of coords and enemy, set the score to 0 and resetting Talonmies positions
        hazard_list.clear() # Gets rid of Hazards
        hazard_coord_list_x.clear()
        hazard_coord_list_y.clear()
        meter_points = 50
        time_left = 5000
        cleaning_score = 0
        game_over_state = False
        player.rect.x = 400
        player.rect.y = 400


#level_area = pygame.display.set_mode((level_width, level_height))
level_pos = (64,200)

#---------------------------------------------
# Images here

bg_image = pygame.image.load("taustakuva.jpg").convert()

hazard_roskat = [pygame.image.load("Biohazard_64.png").convert_alpha(), pygame.image.load("piss.png").convert_alpha(),
                 pygame.image.load("waste_flow.png").convert_alpha(),
                 pygame.image.load("bottles.png").convert_alpha()]


#----------------------------------------------------------------
# Hazard lists --------------------------------------------------

hazard_sprite_list = []
hazard_coord_list = []
hazard_list = []
hazard_coord_list_x = []
hazard_coord_list_y = []

#--------------------------------------------------------------
#
hazard_speed = [1,1]
piste_lista = []
nopeusLista = []
koordLista = []
explosionCount = 0
cleaning_score = 0

player_width = 84
player_height = 84

level_height = 900
level_width = 1200



#blits here
#bg_image.blit(bg_image, (0,0))
#bg_image.blit(hazardit_roskat,(0,0))

#---------------------------------------

pygame.display.flip()

#---------------------------------------------------
# Hazard Level settings              ---------------

meter_points= 100 # Starting points

#--------------------------------------------------------------
# Timer settings                                      ---------

time_left = 5000 # Duration of the timer in seconds

#----------------------------------------------------------------------
# The loop for starting the game and keeps it running   ---------------


main_menu = True


play_text_pos = replay_text_pos
play_text_dir = 1 # 1 is down, -1 is up

#clock = pygame.time.Clock()

while main_menu:
    clock.tick(12)
    screen_size.blit(bg_image,bg_image_pos)

    font= pygame.font.SysFont(None, 120)

    play_outlie = font.render(str("Press R to Play"), True, (BLACK))
    screen_size.blit(play_outlie, (replay_outline_pos)) # Text location

    play_text = font.render(str("Press R to Play"), True, (255, 250, 0))
    screen_size.blit(play_text, play_text_pos) # Text location
    play_text_pos = (play_text_pos[0], play_text_pos[1] + play_text_dir)
    if play_text_pos[1] > replay_text_pos[1] + 4 or play_text_pos[1] < replay_text_pos[1]:
        play_text_dir *= -1
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit(); sys.exit()

        #checks if a mouse is clicked
        if ev.type == KEYUP:
            if ev.key == K_r:
                game_on = True
                main_menu = False
                continue
            if ev.key == K_ESCAPE:
                pygame.quit(); sys.exit()

    pygame.display.flip()


game_on = True
game_over_state = False

while game_on:
    if game_over_state:
        game_over_screen()
    #set FPS
    clock.tick(30)

    # Update the sceen here----------------------------------------

    screen_size.blit(bg_image, bg_image_pos)

    #--------------------------------------
    # Hazard Level & UI   ----------------------

    satisfaction = GREEN if meter_points > 100 else GREENLIGHT if meter_points > 80 else YELLOW if meter_points > 55 else YELLOWLIGHT if meter_points > 35 else RED if meter_points > 20 else REDORANGE
    bar_width = int((meter_points / 100) * 106)

    # Create a surface to draw the gradient on
    gradient_surface = pygame.Surface((bar_width,11))

    # Create the gradient
    gradient = pygame.Surface((bar_width,35), depth = 32)
    gradient = gradient.convert_alpha()
    color1 = satisfaction
    color2 = satisfaction
    if satisfaction == GREEN:
        color2 = GREENLIGHT
    elif satisfaction == GREENLIGHT:
        color2 = GREEN
    elif satisfaction == YELLOW:
        color2 = YELLOWLIGHT
    elif satisfaction == YELLOWLIGHT:
        color2 = YELLOW
    elif satisfaction == RED:
        color2 = REDORANGE
    elif satisfaction == REDORANGE:
        color2 = RED
    for x in range(bar_width):
        gradient_color = int(x / bar_width * 255)
        gradient.fill((gradient_color, color2[1], color2[2], gradient_color),(x, 0, 1, 35))
        gradient_surface.blit(gradient, (0, 0))
        screen_size.blit(gradient_surface, (542, 25))
        satisfaction_points = font.render(str(meter_points), True, (250, 250, 0))

    # Create a surface to draw the gradient on
    text_surface = pygame.Surface((80, 13)) # Surface for hazard level
    text_surface2 = pygame.Surface((40, 13)) # Surface for cleaning points
    text_surface3 = pygame.Surface((75, 13))  # Surface for swipe tutorial
    text_surface4 = pygame.Surface((122, 13)) # Surface for machinegun tutorial
    text_surface5 = pygame.Surface((68, 13)) # Surface for version number

    # Set initial color of text surface
    text_color = (97, 250, 250)

    # Set the text to be rendered on the surface
    text = "HAZARD LEVEL"
    font = pygame.font.SysFont("Arial", 10)
    text_surface.blit(font.render(text, True, text_color), (0, 0))
    # Draw the text surface on the screen
    screen_size.blit(text_surface, (547, 8))

    # In the game loop, update the text color to create the animation
    # This not working.
    text_color = (text_color[0], text_color[1]-1, text_color[2]-1)
    text_surface.fill((0, 0, 0)) # Clear the text surface before blitting new text
    text_surface.blit(font.render(text, True, text_color), (0, 0))

    # Cleaning score in UI
    text_surface2.blit(font.render(str(cleaning_score), True, text_color), (0, 0))
    screen_size.blit(text_surface2, (700, 8))

    # Tutorial for buttons
    text_swipe = "CTRL for SWIPE"
    text_surface3.blit(font.render(text_swipe, True, text_color), (0, 0))
    screen_size.blit(text_surface3, (400, 8))

    text_machinegun = "SPACE for MACHINEGUN"
    text_surface4.blit(font.render(text_machinegun, True, text_color), (0, 0))
    screen_size.blit(text_surface4, (377, 24))

    # Version number
    text_version = "Ver. tm_23.zip"
    text_surface5.blit(font.render(text_version, True, text_color), (0, 0))
    screen_size.blit(text_surface5, (686, 24))


    #--------------------------------------
    # Timer          ----------------------

    total_mins = time_left//60 # minutes left
    total_sec = time_left-(60*(total_mins)) #seconds left
    time_left -= 1
    meter_points-=0.25 # time reduces hazard level

    #--------------------------------------------------------------
    # Mouse interaction

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit(); sys.exit()

        '''
        #code to use mouse in the game
        #create a code line which checks if mouse is pressed
        #create a variable to give points to the player
        if event.type == MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            if mousex < 500 or mousex > 600 and mousey < 200 or mousey > 300:
                if meter_points > 0:
                    meter_points -= 1
                elif meter_points < 0 or meter_points == 0:
                    meter_points = 0
                print(meter_points)
            elif mousex > 500 or mousex < 600 and mousey > 200 or mousey < 300:
                meter_points +=1
                print(meter_points)
        '''

    #this is the old jumping code commented out
    '''
    if not(man.isJump):
        if keys[pygame.K_UP] and man.y > 45 + 90:
            man.y -= man.vel

        if keys[pygame.K_DOWN] and man.y < 720 - 20:
            man.y += man.vel

        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.walkCount = 0

    else:
        if man.jumpHeight >= -10:
            neg = 1
            if man.jumpHeight < 0:
                neg = -1
            man.y -= (man.jumpHeight ** 2) * 0.1 * neg
            man.jumpHeight = man.jumpHeight - 1
            if man.y > 800:
                man.y -= 50

        else:
            man.isJump = False
            man.jumpHeight = 10
    '''
#---------------------------------------------

    # These give level and decorations
    give_level()
    give_decorations()

    spawn_chance = random.randint(0, 50) # Every loop random
    if spawn_chance == 50:
        randomix = random.randint(285, 848)  # The area where hazard_roskat will spawn. Starting and end point of x -axel.
        randomiy = random.randint(177, 675)  # The area where hazard_roskat will spawn. Starting and end point of y -axel.
        #screen_size.blit(hazard_roskat,(randomix,randomiy))
        hazard_list.append(random.choice(hazard_roskat))
        hazard_coord_list_x.append(randomix)
        hazard_coord_list_y.append(randomiy)


    for i in range(0,len(hazard_list)):
        if i < len(hazard_list):
            screen_size.blit(hazard_list[i], (hazard_coord_list_x[i], hazard_coord_list_y[i]))


    # collision detection when Talonmiäs wags his broom next to hazard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        for i in range(0, len(hazard_coord_list_x)):
            for i in range(0, len(hazard_coord_list_y)):
                if i < len(hazard_coord_list_x) and i < len(hazard_coord_list_y):
                    if player.rect.x + 64 - 25 > hazard_coord_list_x[i] and player.rect.x + 25 < hazard_coord_list_x[i] + 90:
                        if player.rect.y > hazard_coord_list_y[i] and player.rect.y < hazard_coord_list_y[i] + 64 or player.rect.y + 64 > hazard_coord_list_y[i] and player.rect.y < hazard_coord_list_y[i] + 64:
                            enemy.draw(screen_size)

    #collision detection if Talonmiäs is inside of hazard
    for i in range(0, len(hazard_coord_list_x)):
        for i in range(0, len(hazard_coord_list_y)):
            if i < len(hazard_coord_list_x) and i < len(hazard_coord_list_y):
                if player.rect.x > hazard_coord_list_x[i] and player.rect.x < hazard_coord_list_x[i] +20:
                    if player.rect.y > hazard_coord_list_y[i] and player.rect.y < hazard_coord_list_y[i] + 20 or player.rect.y + 20 > hazard_coord_list_y[i] and player.rect.y < hazard_coord_list_y[i]:
                        hazard_list.pop(i)
                        hazard_coord_list_x.pop(i)
                        hazard_coord_list_y.pop(i)
                        ouch.play()
                        cleaning_score += 100
                        meter_points -= 10

    # checking if time out or hazard level meter at zero, if true -> game over
    if meter_points <= 0 or time_left == 0:
        game_over_state = True

    #function calls
    player.get_keys()
    #all_sprites_enemies.draw(screen_size) # objects draw
    #all_sprites_enemies.update()
    all_sprites_player.update(screen_size)
    bullets.update()
    bullets.draw(screen_size)

    pygame.display.flip()
