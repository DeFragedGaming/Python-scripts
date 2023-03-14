import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 640
HEIGHT = 480
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game clock
CLOCK = pygame.time.Clock()

# Set up the font for displaying the score
FONT = pygame.font.SysFont("Arial", 24)

# Define the Snake class
class Snake:
    def __init__(self):
        self.segments = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.color = GREEN
    
    def move(self):
        x, y = self.segments[0]
        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10
        self.segments.insert(0, (x, y))
        self.segments.pop()
    
    def grow(self):
        x, y = self.segments[-1]
        if self.direction == "UP":
            y += 10
        elif self.direction == "DOWN":
            y -= 10
        elif self.direction == "LEFT":
            x += 10
        elif self.direction == "RIGHT":
            x -= 10
        self.segments.append((x, y))
    
    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, self.color, (segment[0], segment[1], 10, 10))

# Define the Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10)
        self.color = RED
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], 10, 10))

# Initialize the game objects
snake = Snake()
food = Food()

# Define the game loop
score = 0
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
    
    # Move the snake
    snake.move()
    
    # Check for collision with food
    if snake.segments[0] == food.position:
        snake.grow()
        food = Food()
        score += 1
    
    # Check for collision with walls
     if snake.segments[0][0] < 0 or snake.segments[0][0] > WIDTH or snake.segments[0][1] < 0 or snake.segments[0][1]:
