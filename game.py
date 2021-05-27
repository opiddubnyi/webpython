import pygame
import random
import pygame_textinput

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
font = pygame.font.SysFont("georgia", 24)


# getting word from file
def pick_word(difficulty, filename='10000_words.txt'):
    with open(filename, 'r') as file:
        words = file.readlines()
        interesting_word = False

        while not interesting_word:
            word = random.choice(words)
            if len(word) == difficulty:
                interesting_word = True
                return word


clock = pygame.time.Clock()
is_end = False
guessed = []
die_count = 7

#    pygame.display.set_icon(pygame.image.load('hanger.ico'))
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Hanger Game')

text = font.render("Welcome to Hanger game!", 1, WHITE, BLACK)
screen.blit(text, (150, 100))

pygame.display.flip()

def draw_hanger():

    # drawing foundation
    pygame.draw.rect(screen, WHITE, (470, 450, 100, 50))
    # drawing hanger stand
    pygame.draw.rect(screen, WHITE, (510, 150, 20, 300))
    # drawing hor bulk
    pygame.draw.rect(screen, WHITE, (320, 150, 210, 15))
    pygame.draw.line(screen, WHITE, (460, 155), (520, 190), 5)
    # drawing rope
    pygame.draw.rect(screen, WHITE, (340, 150, 2, 40))
    pygame.display.flip()

draw_hanger()
while not is_end:
    text_input = pygame_textinput.TextInput(initial_string='Welcome')

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            print('got = ', pygame.key.name(event.key))

        text_input.update(events)
    # Blit its surface onto the screen
        if text_input.update(events):
           print(text_input.get_text())
        screen.blit(text_input.get_surface(), (10, 10))

        pygame.display.update()

    clock.tick(60)
