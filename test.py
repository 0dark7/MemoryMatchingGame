import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

CARD_WIDTH = 100
CARD_HEIGHT = 100

CARD_COUNT = 16
NUM_UNIQUE_NUMBERS = CARD_COUNT // 2

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Memory Matching Game")

font = pygame.font.SysFont(None, 48)

card_numbers = list(range(1, NUM_UNIQUE_NUMBERS + 1)) * 2

random.shuffle(card_numbers)

cards = []
for i in range(CARD_COUNT):
    x = (i % 4) * (CARD_WIDTH + 10) + 10
    y = (i // 4) * (CARD_HEIGHT + 10) + 50
    card = pygame.sprite.Sprite()
    card.image = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
    card.image.fill(WHITE)
    card.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
    card.number = card_numbers[i]
    cards.append(card)

flipped_cards = []
matched_cards = []
game_over = False
move_counter = 0
score = 0

def draw_card(card):
    if card in matched_cards:
        pygame.draw.rect(window, GREEN, card.rect)
        number_text = font.render(str(card.number), True, BLACK)
        number_rect = number_text.get_rect()
        number_rect.center = card.rect.center
        window.blit(number_text, number_rect)
    elif card in flipped_cards:
        pygame.draw.rect(window, RED, card.rect)
        number_text = font.render(str(card.number), True, BLACK)
        number_rect = number_text.get_rect()
        number_rect.center = card.rect.center
        window.blit(number_text, number_rect)
    else:
        # check if the mouse cursor is within the bounds of the card
        mouse_pos = pygame.mouse.get_pos()
        if card.rect.collidepoint(mouse_pos):
            pygame.draw.rect(window, WHITE, card.rect)
        else:
            pygame.draw.rect(window, BLUE, card.rect)



def draw_game_over():
    game_over_text = font.render("GAME OVER", True, WHITE)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
    window.blit(game_over_text, game_over_rect)

    move_counter_text = font.render("Moves: " + str(move_counter), True, WHITE)
    move_counter_rect = move_counter_text.get_rect()
    move_counter_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 10)
    window.blit(move_counter_text, move_counter_rect)

    score_text = font.render("Score: " + str(score), True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
    window.blit(score_text, score_rect)

def draw_move_counter():
    move_counter_text = font.render("Moves: " + str(move_counter), True, WHITE)
    move_counter_rect = move_counter_text.get_rect()
    move_counter_rect.topright = (WINDOW_WIDTH - 10, 10)
    window.blit(move_counter_text, move_counter_rect)


def draw_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)
    window.blit(score_text, score_rect)


while not game_over:
    start_time = pygame.time.get_ticks()
    while not game_over:
        elapsed_time = pygame.time.get_ticks() - start_time
        seconds = elapsed_time // 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(flipped_cards) < 2:
                    for card in cards:
                        if card.rect.collidepoint(event.pos):
                            if card not in flipped_cards and card not in matched_cards:
                                flipped_cards.append(card)
                                draw_card(card)
                                pygame.display.update()
                                if len(flipped_cards) == 2:
                                    move_counter += 1
                                    draw_move_counter()
                                    if flipped_cards[0].number == flipped_cards[1].number:
                                        matched_cards.extend(flipped_cards)
                                        flipped_cards = []
                                        score += 1
                                        if score == NUM_UNIQUE_NUMBERS:
                                            game_over = True
                                    else:
                                        pygame.time.wait(500)
                                        for card in flipped_cards:
                                            draw_card(card)
                                        pygame.display.update()
                                        flipped_cards = []

        window.fill(BLACK)
        for card in cards:
            draw_card(card)
        draw_move_counter()
        draw_score()
        time_text = font.render("Time: " + str(seconds), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, 50)
        window.blit(time_text, time_rect)
        if game_over:
            window.fill(BLACK)
            draw_game_over()
            time_text = font.render("Time: " + str(seconds), True, WHITE)
            time_rect = time_text.get_rect()
            time_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70)
            window.blit(time_text, time_rect)
        pygame.display.update()

pygame.time.delay(5000)
pygame.quit()