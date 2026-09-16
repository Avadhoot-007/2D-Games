import pygame
import sys
from flappy_bird import main as flappy_bird_main
from pong import main as pong_game_main

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 128, 255)
HOVER_COLOR = (0, 255, 255)

# Load background image
background = pygame.image.load('G:\\College\\MCA\\Sem 1\\Project\\Project\\bckgrnd.jpeg')  
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
# Create the game selection function
def game_selector():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Selector")

    # Define font
    font = pygame.font.SysFont(None, 48)

    # Define buttons
    flappy_button = font.render("Flappy Bird", True, WHITE)
    pong_button = font.render("Pong Game", True, WHITE)

    # Define button positions
    flappy_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - flappy_button.get_width() // 2, SCREEN_HEIGHT // 2 - 40, flappy_button.get_width(), flappy_button.get_height())
    pong_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - pong_button.get_width() // 2, SCREEN_HEIGHT // 2 + 40, pong_button.get_width(), pong_button.get_height())

    # Main loop
    running = True
    while running:
        screen.blit(background, (0, 0))  # Draw background

        mouse_pos = pygame.mouse.get_pos()
        # Check if buttons are hovered
        if flappy_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_COLOR, flappy_button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, flappy_button_rect)

        if pong_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_COLOR, pong_button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, pong_button_rect)

        # Draw buttons
        screen.blit(flappy_button, flappy_button_rect.topleft)
        screen.blit(pong_button, pong_button_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if Flappy Bird button is clicked
                if flappy_button_rect.collidepoint(mouse_pos):
                    flappy_bird_main()  # Redirect to Flappy Bird
                # Check if Pong Game button is clicked
                if pong_button_rect.collidepoint(mouse_pos):
                    pong_game_main()  # Redirect to Pong Game

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == ("__main"
                "__"):
    game_selector()
