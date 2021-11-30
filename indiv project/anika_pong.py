# Anika Bajpai
# ACADEMIC INTEGRITY STATEMENT
# I have not used source code obtained from any other unauthorized
# source, either modified or unmodified. Neither have I provided
# access to my code to another. The project I am submitting
# is my own original work.
# ===============================================================================
import random
import pygame
from pygame.locals import *
from anika_pong_variables import * #this is my imported data
from anika_pong_game_class import * #this is my user-defined function from another file

#set up screen
screen_measure = pygame.display.set_mode((display_width, display_height), 0, 32)

class Paddle(): #user-defined function 2
    def __init__(self, left):
        self.left = left
        self.top = display_height/2 - paddle_height/2
        self.dy = 0
        self.draw(self.left, self.top)
    def draw(self, left, top):
        self.rect = pygame.draw.rect(screen_measure, (255,255,255), (left, top, paddle_width, paddle_height))
    def steer(self, direction, operation):
        if operation == stop:
            self.dy = 0
        elif operation == start:
            self.dy = {up: -paddle_move, down: paddle_move}[direction]
    def update(self): #this makes the new top border posy+newposy
        new_top = self.top + self.dy
        #limits display boundary for the paddle
        if(new_top < 0):
            new_top = 0
        if((new_top + paddle_height) > display_height): #if statement requirement
            new_top = display_height - paddle_height
        self.draw(self.left, new_top)
        self.top = new_top 

class Ball(): #user-defined function 3
    def draw(self, x, y):
        self.rect = pygame.draw.circle(screen_measure, (255, 255, 255), (x, y), ball_size)
    def __init__(self): #initializing position
        self.orientation = random.randint(2,5)
        self.draw(display_width/2, display_height/2)
    def update(self): #allowing for ball movement
        x_position = self.rect.center[0]
        y_position = self.rect.center[1]
        altered_height = self.rect.width/2
        if((y_position - altered_height - ball_move) < 0): #if the ball hits the top of the screen
            self.hitsborder(self.orientation)
        if((y_position + altered_height + ball_move) > display_height): #if the ball hits the bottom of the screen
            self.hitsborder(self.orientation)            
        #attribute ball movement to screen quadrants 
        if(self.orientation == upright):
            self.dy = -ball_move
            self.dx = ball_move
        if(self.orientation == upleft):
            self.dy = -ball_move
            self.dx = -ball_move
        if(self.orientation == downright):
            self.dy = ball_move
            self.dx = ball_move
        if(self.orientation == downleft):
            self.dy = ball_move
            self.dx = -ball_move
        self.draw(x_position + self.dx, y_position + self.dy)
    def hitspaddle(self):
        if(self.orientation == downright): self.orientation = downleft
        elif(self.orientation == upleft): self.orientation = upright
        elif(self.orientation == upright): self.orientation = upleft
        elif(self.orientation == downleft): self.orientation = downright
    def hitsborder(self, direction):
        if(direction == upright):
            self.orientation = downright
        elif(direction == upleft):
            self.orientation = downleft
        elif(direction == downright):
            self.orientation = upright
        elif(direction == downleft):
            self.orientation = upleft

def main():
    ball = Ball()     # define all sprites (variables that move)
    game = Game()     # creates the game
    right_paddle = Paddle(display_width - paddle_start_pos - 20)
    left_paddle = Paddle(paddle_start_pos)
    # out player messages 
    #error checking 2:
    textPlayer1Wins = game.font.render("Player 1 Wins", True, (255,255,255))
    textPlayer2Wins = game.font.render("Player 2 Wins", True, (255,255,255))
    
#here is the nested loop requirement
    while True: #while loop requirement
        game.clock.tick(frames_per_second)  # define frames per second
        #create background
        screen_measure.blit(game.background, (0, 0))
        # configure keyboard usage
        for event in pygame.event.get(): #for loop requirement
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game.quit() #error checking 1: if ball hits screen border game is quit
            if event.type == KEYDOWN:
                if event.key == K_s: left_paddle.steer(down, start)
                if event.key == K_w: left_paddle.steer(up, start)
                if event.key == K_DOWN: right_paddle.steer(down, start)
                if event.key == K_UP: right_paddle.steer(up, start)
            # defines keyboard functions
            if event.type == KEYUP:
                if event.key == K_s: left_paddle.steer(down, stop)
                if event.key == K_w: left_paddle.steer(up, stop)
                if event.key == K_DOWN: right_paddle.steer(down, stop)
                if event.key == K_UP: right_paddle.steer(up, stop)
        # ball to left border
        if(ball.rect[0] <= ball_move):
            screen_measure.blit(textPlayer2Wins,(display_width / 2 - (textPlayer2Wins.get_width() / 2), display_height / 2 - (textPlayer2Wins.get_height() / 2)))
            pygame.display.update()
            pygame.time.wait(3000)
            ball = Ball()
        # ball to right border
        if(ball.rect[0] >= (display_width - ball_move - ball.rect.width)):
            screen_measure.blit(textPlayer1Wins,(display_width / 2 - (textPlayer1Wins.get_width() / 2), display_height / 2 - (textPlayer1Wins.get_height() / 2)))
            pygame.display.update()
            pygame.time.wait(3000)
            ball = Ball()
        # ball hitting left/right paddle
        if((ball.rect.colliderect(left_paddle.rect)) or (ball.rect.colliderect(right_paddle.rect))):
            ball.hitspaddle()

        right_paddle.update()
        left_paddle.update()
        ball.update()
        pygame.display.update()
    game.quit()
if __name__ == '__main__':
    main()
#is over the 85 min requirement
    #anika pong: edition 1
    

    