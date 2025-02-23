import pgzrun
import random

WIDTH = 500
HEIGHT = 500

bird = Actor('bird', (40, 250))
bottom = Actor('bottom', (WIDTH, HEIGHT + 100))
top = Actor('top', (WIDTH, random.randint(-200, -50)))

bird.velocity = 1
game_over = False

obstacles = [top, bottom]

def draw():
    screen.clear()
    screen.fill((235, 245, 255))
    bird.draw()
    
    for obstacle in obstacles:
            obstacle.draw()
    
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="red")
        screen.draw.text("Press Enter to play again", center=(WIDTH // 2, HEIGHT // 2 + 30), fontsize=25, color="red")
    
def update():
    global game_over
    
    if game_over:
        return
    
    bird.y += bird.velocity
    
    if bird.y > HEIGHT or bird.y < 0:
        bird.y = 0
        
    for obstacle in obstacles:
        obstacle.x -= 2
    
    if top.x < 0:
        top.pos = WIDTH, random.randint(-200, -50)
    if bottom.x < 0:
        bottom.pos = WIDTH, random.randint(HEIGHT, HEIGHT +150)
        
    if bird.colliderect(top) or bird.colliderect(bottom):
        game_over = True
        
        
def on_key_down(key):
    if key == keys.UP: 
        bird.velocity -= 5
    if key == keys.RETURN:
        reset_game()
def on_key_up(key):
    if key == keys.UP: 
        bird.velocity = 1

def reset_game():
    global game_over
    game_over = False  

    bird.pos = 40, 250

    top.pos = WIDTH, random.randint(-200, -50)
    bottom.pos = WIDTH, random.randint(HEIGHT, HEIGHT +150)   

pgzrun.go()