# Jucimar Jr
# 2024
# Thiago Ramon Martins Barros
# Matricula: 2415310038
import random

import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2024-09-02")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
initial_pos_player_1 = 50
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
initial_pos_player_2 = 1180
player_2_y = 300

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5.0
ball_dy = 5.0
ball_prevision_y = 300

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()


def get_ball_prevision(actual_x):
    global ball_prevision_y
    if ball_dx > 0:
        dist_x = initial_pos_player_2 - actual_x
        temp_x = dist_x / ball_dx
        prevision_y = ball_y + (ball_dy * temp_x)
        ball_prevision_y = prevision_y if prevision_y > 0 else prevision_y * (-1)
    else:
        ball_prevision_y = 300


def move_ai_to_ball_prevision():
    global player_2_y
    if ball_dx < 0:
        return
    if player_2_y <= ball_prevision_y:
        player_2_y += 5
    if player_2_y >= ball_prevision_y:
        player_2_y -= 5
    if player_2_y >= 570:
        player_2_y = 570
    if player_2_y <= 0:
        player_2_y = 0


# Touching in middle of the paddle, the ball velocity still the same
# Touching on paddle's corners, the ball velocity will increase 0.2 of its velocity
def update_speed_ball_touching_in_paddle(actual_y, y_paddle, height_paddle):
    global ball_dx, ball_dy
    pos_ball_in_paddle = actual_y - y_paddle
    distance_from_center = (pos_ball_in_paddle - height_paddle / 2) / (height_paddle / 2)
    speed_multiplier = 1 + abs(distance_from_center) * 0.5
    ball_dx *= speed_multiplier
    ball_dy += distance_from_center * 5
    ball_dx = max(min(ball_dx, 10), -10)
    ball_dy = max(min(ball_dy, 10), -10)


while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= (-1)
            get_ball_prevision(ball_x)
            bounce_sound_effect.play()
        if ball_y <= 0:
            ball_dy *= (-1)
            get_ball_prevision(ball_x)
            bounce_sound_effect.play()

        # Ball touches player one 's paddle
        if ball_x < initial_pos_player_1 + player_1.get_width():
            if player_1_y - 10 < ball_y < player_1_y + player_1.get_height():
                ball_dx *= (-1)
                get_ball_prevision(ball_x)
                update_speed_ball_touching_in_paddle(ball_y, player_2_y, player_2.get_height())
                bounce_sound_effect.play()

        # Ball touches player two 's paddle
        if ball_x > initial_pos_player_2:
            if player_2_y - 10 < ball_y < player_2_y + player_2.get_height():
                ball_dx *= (-1)
                get_ball_prevision(ball_x)
                update_speed_ball_touching_in_paddle(ball_y, player_2_y, player_2.get_height())
                bounce_sound_effect.play()

        # scoring points
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            player_1_y = 300
            player_2_y = 300
            ball_dy = 5
            ball_dx = 5
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            player_1_y = 300
            player_2_y = 300
            ball_dy = 5
            ball_dx = 5
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 5
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 "Artificial Intelligence"
        move_ai_to_ball_prevision()

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (initial_pos_player_1, player_1_y))
        screen.blit(player_2, (initial_pos_player_2, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
