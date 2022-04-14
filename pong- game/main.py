from ast import If
import pygame



pygame.init()

size = width, height = 700, 500

screen = pygame.display.set_mode(size)

pygame.display.set_caption("pong")
FPS = 60
color = (255, 0, 0)

paddle_width, paddle_height = 20, 100

class Paddle:
    COLOR = color
    Velocity = 4

    def __init__(self, x, y, width, height) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR,(self.x, self.y, self.width, self.height))

    def move(self, up = True):
        if up:
            self.y -= self.Velocity 
        else:
            self.y += self.Velocity 


def draw(win, paddles):
    win.fill("green")

    for paddle in paddles:
        paddle.draw(screen)

    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.Velocity >=0 :
        left_paddle.move(up = True)
    
    if keys[pygame.K_s] and left_paddle.y + left_paddle.Velocity + left_paddle.height <= height:
        left_paddle.move(up = False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.Velocity >=0:
        right_paddle.move(up = True)
    
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.Velocity + right_paddle.height <= height:
        right_paddle.move(up = False)



def main():
    run = True;
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, height//2 - paddle_height//2, paddle_width, paddle_height)
    right_paddle = Paddle(width - 10 - paddle_width, height//2 - paddle_height//2, paddle_width, paddle_height)

    while run:
        clock.tick(FPS)
        draw(screen, [left_paddle,right_paddle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break;


        keys = pygame.key.get_pressed()

        handle_paddle_movement(keys, left_paddle, right_paddle) 

    pygame.quit()

if __name__ == '__main__':
    main()