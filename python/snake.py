import pygame
import random


pygame.init()


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)


WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % (WIDTH // CELL_SIZE), (head_y + dir_y) % (HEIGHT // CELL_SIZE))
        
        if new_head in self.body:
            return False  
        
        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
        return True 
    def grow_snake(self):
        self.grow = True

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, BLUE, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def change_direction(self, new_direction):
        if [sum(x) for x in zip(self.direction, new_direction)] != [0, 0]:
            self.direction = new_direction

def draw_food(position, screen):
    pygame.draw.rect(screen, YELLOW, (position[0] * CELL_SIZE, position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)
                elif event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)

        screen.fill(MAGENTA)
        
        if snake.body[0] == food:
            snake.grow_snake()
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))

        alive = snake.move()
        if not alive:
            font = pygame.font.Font(None, 36)
            text = font.render(f'Your Score: {len(snake.body) - 3}', True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            main()  # Restart the game

        snake.draw(screen)
        draw_food(food, screen)

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
