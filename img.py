import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

CARD_WIDTH = 100
CARD_HEIGHT = 100

CARD_COUNT = 16
NUM_UNIQUE_IMAGES = CARD_COUNT // 2

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Memory Matching Game")

font = pygame.font.SysFont(None, 48)

image_paths = [
    "images/card.png",
    "images/card0.png",
    "images/card1.png",
    "images/cs.png",
    "images/cs0.png",
    "images/cs1.png",
    "images/speak.png",
    "images/mute.png",
]

random.shuffle(image_paths)
image_paths *= 2

cards = []
for i in range(CARD_COUNT):
    x = (i % 4) * (CARD_WIDTH + 10) + 10
    y = (i // 4) * (CARD_HEIGHT + 10) + 50
    card = pygame.sprite.Sprite()
    card.image_back = pygame.image.load("images/card_back.png")
    card.image_back = pygame.transform.scale(card.image_back, (CARD_WIDTH, CARD_HEIGHT))
    card.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
    cards.append(card)

random.shuffle(cards)

for i, card in enumerate(cards):
    card.image = pygame.image.load(image_paths[i])
    card.image = pygame.transform.scale(card.image, (CARD_WIDTH, CARD_HEIGHT))
    card.number = i // 2
    card.image_path = image_paths[i]  # Store the image path for comparison

flipped_cards = []
matched_cards = []
game_over = False
move_counter = 0
score = 0

def draw_card(card):
    if card in matched_cards:
        window.blit(card.image, card.rect)
    elif card in flipped_cards:
        window.blit(card.image, card.rect)
    elif card.image_back != None:  # Draw card back only if it exists
        window.blit(card.image_back, card.rect)


def draw_game_over():
    game_over_text = font.render("GAME OVER", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    window.blit(game_over_text, game_over_rect)

    move_counter_text = font.render("Moves: " + str(move_counter), True, WHITE)
    move_counter_rect = move_counter_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 10))
    window.blit(move_counter_text, move_counter_rect)

    score_text = font.render("Score: " + str(score), True, WHITE)
    score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30))
    window.blit(score_text, score_rect)


def draw_move_counter():
    move_counter_text = font.render("Moves: " + str(move_counter), True, WHITE)
    move_counter_rect = move_counter_text.get_rect(topright=(WINDOW_WIDTH - 10, 10))
    window.blit(move_counter_text, move_counter_rect)


def draw_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    score_rect = score_text.get_rect(topleft=(10, 10))
    window.blit(score_text, score_rect)


while not game_over:
    start_time = pygame.time.get_ticks()

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
                                if flipped_cards[0].image_path == flipped_cards[1].image_path:
                                    matched_cards.extend(flipped_cards)
                                    flipped_cards = []
                                    score += 100
                                    if len(matched_cards) == CARD_COUNT:  # tüm kartlar eşlenince
                                        pygame.time.delay(1000)
                                        game_over = True
                                    if len(matched_cards) == CARD_COUNT and score == 800:  # tüm kartlar dogru eşlenirşe
                                        pygame.time.delay(1500)
                                        game_over = True
                                else:

                                    score -= 10
                                    pygame.display.update()  # Update the display before flipping the cards back
                                    for card in flipped_cards:
                                        draw_card(card)
                                    pygame.display.update()
                                    pygame.time.wait(500)  # Delay before flipping the cards back
                                    for card in flipped_cards:
                                        draw_card(card)
                                    pygame.display.update()
                                    flipped_cards = []

        window.fill(BLACK)
        for card in cards:
            draw_card(card)
        draw_move_counter()
        draw_score()
        elapsed_time = pygame.time.get_ticks() - start_time
        seconds = elapsed_time // 1000
        time_text = font.render("Time: " + str(seconds), True, WHITE)
        time_rect = time_text.get_rect(topright=(WINDOW_WIDTH - 10, 50))
        window.blit(time_text, time_rect)
        if game_over:
            window.fill(BLACK)
            draw_game_over()
            time_text = font.render("Time: " + str(seconds), True, WHITE)
            time_rect = time_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70))
            window.blit(time_text, time_rect)
        pygame.display.update()

pygame.time.delay(5000)
pygame.quit()

