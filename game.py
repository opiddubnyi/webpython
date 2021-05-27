import pygame
import random


# drawing screen
def draw_screen():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption('Hanger Game')
#    pygame.display.set_icon(pygame.image.load('hanger.ico'))


    WHITE = (255, 255, 255)
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

draw_screen()
while not is_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # detecting what was entered
        if event.type == pygame.KEYDOWN:
            print('got = ', pygame.key.name(event.key))

    clock.tick(60)
