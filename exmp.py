import pygame

import button
from pygame import mixer
import winsound
import time
import random
import mysql.connector

mixer.init()
mixer.music.load('bgmusic.wav')
mixer.music.load('bgmusic0.wav')
mixer.music.load('bgmusic1.wav')
# sesler
while pygame.mixer.get_busy():
    pygame.time.delay(7)
mixer.music.set_volume(0.01)

song_list = ["bgmusic.wav", "bgmusic0.wav", "bgmusic1.wav"]
current_song = 0


def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()


play_song(song_list[current_song])


def prev_song():
    global current_song
    current_song -= 1
    if current_song < 0:
        current_song = len(song_list) - 1
    play_song(song_list[current_song])


def next_song():
    global current_song
    current_song += 1
    if current_song >= len(song_list):
        current_song = 0
    play_song(song_list[current_song])


def change_volume(amount):
    current_volume = pygame.mixer.music.get_volume()
    new_volume = max(0, min(1, current_volume + amount))
    pygame.mixer.music.set_volume(new_volume)


pygame.init()

gameWidth = 1280
gameHeight = 760
# ekran
screen = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption('Memory Matching Game')
gameIcon = pygame.image.load('images/icon.png')
pygame.display.set_icon(gameIcon)

game_menu = True
menu_durum = "main"

# görsel tasarım
play_image = pygame.image.load('images/playbutton.png').convert_alpha()
cover_image = pygame.image.load('images/cover.png').convert_alpha()
bests_image = pygame.image.load('images/bests.png').convert_alpha()
settings_image = pygame.image.load('images/settings.png').convert_alpha()
htp_image = pygame.image.load('images/htp.png').convert_alpha()
mute_image = pygame.image.load('images/mute.png').convert_alpha()
speak_image = pygame.image.load('images/speak.png').convert_alpha()
back_image = pygame.image.load('images/back.png').convert_alpha()
bestscorestext_image = pygame.image.load('images/bestscores_text.png').convert_alpha()
settingstext_image = pygame.image.load('images/settings_text.png').convert_alpha()
backmenutext_image = pygame.image.load('images/backmenu_text.png').convert_alpha()
htptext_image = pygame.image.load('images/htp_text.png').convert_alpha()
tfptext_image = pygame.image.load('images/tfp_text.png').convert_alpha()
playagaintext_image = pygame.image.load('images/playagain_text.png').convert_alpha()
welldonetext_image = pygame.image.load('images/welldone_text.png').convert_alpha()
exit_image = pygame.image.load('images/exit.png').convert_alpha()
exit_image1 = pygame.image.load('images/exit.png').convert_alpha()
p1_image = pygame.image.load('images/p1.png').convert_alpha()
p2_image = pygame.image.load('images/p2.png').convert_alpha()
p1s_image = pygame.image.load('images/p1s.png').convert_alpha()
p2s_image = pygame.image.load('images/p2s.png').convert_alpha()
onalti_image = pygame.image.load('images/3.png').convert_alpha()
otuz_image = pygame.image.load('images/4.png').convert_alpha()
kirk_image = pygame.image.load('images/5.png').convert_alpha()
circle_image = pygame.image.load('images/circle.png').convert_alpha()
prevsong_image = pygame.image.load('images/prev.png').convert_alpha()
nextsong_image = pygame.image.load('images/next.png').convert_alpha()
down_image = pygame.image.load('images/down.png').convert_alpha()
up_image = pygame.image.load('images/up.png').convert_alpha()
cs_image = pygame.image.load('images/cs.png').convert_alpha()
cs0_image = pygame.image.load('images/cs0.png').convert_alpha()
cs1_image = pygame.image.load('images/cs1.png').convert_alpha()
card_image = pygame.image.load('images/card.png').convert_alpha()
card_image0 = pygame.image.load('images/card0.png').convert_alpha()
card_image1 = pygame.image.load('images/card1.png').convert_alpha()
stoc_image = pygame.image.load('images/stoc.png').convert_alpha()
spec_image = pygame.image.load('images/spec.png').convert_alpha()

# butonlar
play_button = button.Button(600, 350, play_image, 0.5)
cover_button = button.Button(330, 100, cover_image, 0.8)
cover_button1 = button.Button(260, 190, cover_image, 1)
bests_button = button.Button(1166, 210, bests_image, 0.5)
settings_button = button.Button(1160, 340, settings_image, 0.5)
htp_button = button.Button(1167, 470, htp_image, 0.5)
mute_button = button.Button(30, 40, mute_image, 0.5)
speak_button = button.Button(25, 110, speak_image, 0.5)
back_button = button.Button(50, 40, back_image, 0.5)
bestscorestext_button = button.Button(450, 140, bestscorestext_image, 0.5)
settingstext_button = button.Button(500, 140, settingstext_image, 0.5)
backmenutext_button = button.Button(90, 590, backmenutext_image, 0.5)
htptext_button = button.Button(450, 140, htptext_image, 0.5)
tfptext_button = button.Button(430, 600, tfptext_image, 0.6)
playagaintext_button = button.Button(970, 590, playagaintext_image, 0.5)
welldonetext_button = button.Button(310, 230, welldonetext_image, 0.5)
exit_button = button.Button(40, 650, exit_image, 0.150)
exit_button1 = button.Button(1190, 700, exit_image1, 0.1)
p1_button = button.Button(550, 468, p1_image, 0.3)
p2_button = button.Button(650, 464.5, p2_image, 0.3)
p1s_button = button.Button(550, 465, p1s_image, 0.3)
p2s_button = button.Button(650, 461.5, p2s_image, 0.3)
onalti_button = button.Button(100, 270, onalti_image, 0.5)
otuz_button = button.Button(300, 276, otuz_image, 0.5)
kirk_button = button.Button(500, 274, kirk_image, 0.5)
circle_button0 = button.Button(542, 460, circle_image, 0.3)
prevsong_button = button.Button(230, 480, prevsong_image, 0.2)
nextsong_button = button.Button(431, 479, nextsong_image, 0.2)
down_button = button.Button(325, 510, down_image, 0.033)
up_button = button.Button(325, 440, up_image, 0.033)
cs_button = button.Button(680, 419, cs_image, 0.599)
cs0_button = button.Button(835, 420, cs0_image, 0.5)
cs1_button = button.Button(990, 420, cs1_image, 0.5)
card_button = button.Button(680, 420, card_image, 0.8)
card0_button = button.Button(835, 422, card_image0, 0.8)
card1_button = button.Button(990, 421, card_image1, 0.8)
stoc_button = button.Button(700, 341, stoc_image, 0.6)
spec_button = button.Button(960, 341, spec_image, 0.6)

# renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREEN1 = (94, 198, 94)
ORANGE = (255, 135, 0)
YELLOW = (255, 255, 150)
RED = (255, 0, 0)
GRAY = (77, 77, 77)
GRAY1 = (180, 205, 205)
GRAY3 = (130, 130, 130)
DARK_GRAY = (64, 64, 64)
BLUE1 = (173, 216, 230)
PURPLE = (203, 195, 227)
CARD = (138, 43, 226)
CARD0 = (95, 158, 160)
CARD1 = (199, 199, 199)

font4 = pygame.font.SysFont("arialblack", 20)
font5 = pygame.font.SysFont("arialblack", 24)
font = pygame.font.SysFont("arialblack", 30)
font1 = pygame.font.SysFont("arialblack", 50)
font3 = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

# sayac
start_time = time.time()
current_time = time.time()
elapsed_time = current_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
time_str = f"{int(minutes):02d}:{int(seconds):02d}"
print(f"Time: {time_str}", font, TEXT_COL, 300, 50)

btime = 0
bscore = 0
bmove = 0
elapsed_timee = 0
clock = pygame.time.Clock()
falling = 0


def loading():
    global falling
    global menu_durum
    # Kartların başlangıç konumları
    card_positions = generate_random_positions(start_x=0)

    # Kart resimlerini yükleme
    card_images = [
        pygame.image.load("images/cstrans.png"),
        pygame.image.load("images/cstrans0.png"),
        pygame.image.load("images/cstrans1.png")
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                falling = 1

        cover_button1.draw(screen)

        for i, pos in enumerate(card_positions):
            card_x, card_y = pos

            # Kartı çizme
            card_image_index = i % len(card_images)  # Kart resmi indeksini döngü içinde dönüşümlü olarak seçme
            screen.blit(card_images[card_image_index], (card_x, card_y))

            # Kartların yukarıdan aşağıya düşmesi
            card_y += 4

            # Kart ekranın altına ulaştığında yeni bir sayfa çizilir
            if card_y > gameHeight:
                card_positions[i] = generate_random_positions(card_x)
                draw_text("Please click to continue", font, BLACK, 440, 490)
            if card_y == gameHeight:
                winsound.PlaySound("Flip", 1)

            card_positions[i] = (card_x, card_y)

        pygame.display.flip()
        clock.tick(60)
        if falling == 1:
            menu_durum = "main"
            return


def generate_random_positions(start_x):
    positions = []
    for _ in range(10):
        x = start_x - 40
        y = random.randint(-300, -300)
        positions.append((x, y))
        start_x += 199  # Sütunlar arası mesafe, 100 piksel olarak varsayılan olarak ayarlanmıştır
    return positions


fallcard = pygame.image.load("images/cstrans.png").convert_alpha()


# fonksiyonlar
def reset_timer():
    global start_time
    start_time = time.time()


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def htptext():
    box = pygame.Surface((1000, 330), pygame.SRCALPHA)
    box.fill((0, 0, 0, 128))
    screen.blit(box, (150, 240))
    draw_text("Click reversed cards and try to find their matches.", font, TEXT_COL, 160, 260)
    draw_text("You can change card themes according to your style.", font, TEXT_COL, 160, 320)
    draw_text("Set your nicknames or colors.", font, TEXT_COL, 160, 380)
    draw_text("Match the cards quickly and in less moves.", font, TEXT_COL, 160, 440),
    draw_text("The player with the most points wins.", font, TEXT_COL, 160, 500)
    draw_text("Muhammet Emir Cayir", font4, GRAY, 900, 540)


card_type = "stock"
card_typee = " "


def setttext():
    global onalti_button
    global otuz_button
    global kirk_button
    global CARD_COUNT
    global card_type
    global card_typee
    box = pygame.Surface((490, 270), pygame.SRCALPHA)
    box.fill((0, 0, 0, 128))
    screen.blit(box, (110, 370))
    draw_text("Card Themes", font1, TEXT_COL, 730, 260)
    draw_text("Background Music", font, TEXT_COL, 200, 380)
    if prevsong_button.draw(screen):
        prev_song()
    if nextsong_button.draw(screen):
        next_song()
    if down_button.draw(screen):
        change_volume(-0.07)
        print("Volume -")
    if up_button.draw(screen):
        change_volume(0.07)
        print("Volume +")
    if onalti_button.draw(screen):
        winsound.PlaySound('Click', 1)
        onalti()
        print("Created 4x4")
    if otuz_button.draw(screen):
        winsound.PlaySound('Click', 1)
        otuz()
        print("Created 6x5")
    if kirk_button.draw(screen):
        winsound.PlaySound('Click', 1)
        kirk()
        print("Created 8x5")
    if CARD_COUNT == 16:
        draw_text("____", font1, TEXT_COL, 105, 280)
        if card_type == "stock":
            draw_text("_____", font1, TEXT_COL, 695, 580)
    if CARD_COUNT == 30:
        draw_text("____", font1, TEXT_COL, 304, 280)
        if card_type == "stock":
            draw_text("_____", font1, TEXT_COL, 846, 580)
    if CARD_COUNT == 40:
        draw_text("____", font1, TEXT_COL, 504, 280)
        if card_type == "stock":
            draw_text("_____", font1, TEXT_COL, 1003, 580)
    draw_text("(Instrumental)", font4, GRAY, 180, 610)
    if current_song == 0:
        draw_text("Somebody That I Used To Know", font4, GRAY, 180, 590)
    if current_song == 1:
        draw_text("Relax, Take It Easy", font4, GRAY, 180, 590)
    if current_song == 2:
        draw_text("Never Gonna Give You Up", font4, GRAY, 180, 590)
    if stoc_button.draw(screen):
        winsound.PlaySound('Click', 1)
        card_type = "stock"
    if spec_button.draw(screen):
        winsound.PlaySound('Click', 1)
        card_type = "special"

    if card_type == "stock":
        draw_text("_____", font1, TEXT_COL, 704, 330)
        cs_button.draw(screen)
        cs0_button.draw(screen)
        cs1_button.draw(screen)
    if card_type == "special":
        draw_text("______", font1, TEXT_COL, 968, 330)

        mouse_pos = pygame.mouse.get_pos()

        if card_button.rect.collidepoint(mouse_pos):
            box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
            box1.fill((138, 43, 226, 128))
            screen.blit(box1, (678, 415))
        if card0_button.rect.collidepoint(mouse_pos):
            box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
            box1.fill((95, 158, 160, 128))
            screen.blit(box1, (832, 415))
        if card1_button.rect.collidepoint(mouse_pos):
            box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
            box1.fill((199, 199, 199, 128))
            screen.blit(box1, (986, 415))
        if card_button.draw(screen):
            card_typee = "ps"
            winsound.PlaySound('mor', 1)
        if card0_button.draw(screen):
            card_typee = "ps0"
            winsound.PlaySound('yesil', 1)
        if card1_button.draw(screen):
            card_typee = "ps1"
            winsound.PlaySound('kara', 1)

        if card_typee == "ps":
            draw_text("______", font1, TEXT_COL, 677, 590)
            box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
            box1.fill((138, 43, 226, 70))
            screen.blit(box1, (678, 415))

        if card_typee == "ps0":
            draw_text("______", font1, TEXT_COL, 831, 590)
            box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
            box1.fill((95, 158, 160, 70))
            screen.blit(box1, (832, 415))

        if card_typee == "ps1":
            draw_text("______", font1, TEXT_COL, 985, 590)
            box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
            box1.fill((199, 199, 199, 70))
            screen.blit(box1, (986, 415))


def besttext():
    global player_name
    if CARD_COUNT == 16:
        draw_text("Nick       |  Score  |   Time   |  Move  ", font3, TEXT_COL, 340, 235)
        draw_text("__________________________________________", font3, TEXT_COL, 239, 245)
        draw_text("________________________________________________________", font, TEXT_COL, 239, 550)
        draw_text("(4x4)", font, TEXT_COL, 619, 585)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="players"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM score16 ORDER BY player_score DESC")
        myresult = mycursor.fetchall()
        text_name = font3.render(('1. {0}'.format(myresult[0][1])), 1, (255, 199, 0))
        text_name1 = font3.render(('2. {0}'.format(myresult[1][1])), 1, (255, 255, 140))
        text_name2 = font3.render(('3. {0}'.format(myresult[2][1])), 1, (255, 255, 199))
        text_name3 = font3.render(('4. {0}'.format(myresult[3][1])), 1, (255, 255, 255))
        text_name4 = font3.render(('5. {0}'.format(myresult[4][1])), 1, (255, 255, 255))

        text_points = font3.render(('|    {0}'.format(myresult[0][2])), 1, (255, 199, 0))
        text_points1 = font3.render(('|    {0}'.format(myresult[1][2])), 1, (255, 255, 140))
        text_points2 = font3.render(('|    {0}'.format(myresult[2][2])), 1, (255, 255, 199))
        text_points3 = font3.render(('|    {0}'.format(myresult[3][2])), 1, (255, 255, 255))
        text_points4 = font3.render(('|    {0}'.format(myresult[4][2])), 1, (255, 255, 255))

        text_time = font3.render(('  |   {0}'.format(myresult[0][3])), 1, (255, 199, 0))
        text_time1 = font3.render(('  |   {0}'.format(myresult[1][3])), 1, (255, 255, 140))
        text_time2 = font3.render(('  |   {0}'.format(myresult[2][3])), 1, (255, 255, 199))
        text_time3 = font3.render(('  |   {0}'.format(myresult[3][3])), 1, (255, 255, 255))
        text_time4 = font3.render(('  |   {0}'.format(myresult[4][3])), 1, (255, 255, 255))

        text_move = font3.render(('  |    {0}'.format(myresult[0][4])), 1, (255, 199, 0))
        text_move1 = font3.render(('  |    {0}'.format(myresult[1][4])), 1, (255, 255, 140))
        text_move2 = font3.render(('  |    {0}'.format(myresult[2][4])), 1, (255, 255, 199))
        text_move3 = font3.render(('  |    {0}'.format(myresult[3][4])), 1, (255, 255, 255))
        text_move4 = font3.render(('  |    {0}'.format(myresult[4][4])), 1, (255, 255, 255))

        screen.blit(text_name, (230, 300))
        screen.blit(text_name1, (230, 350))
        screen.blit(text_name2, (230, 400))
        screen.blit(text_name3, (230, 450))
        screen.blit(text_name4, (230, 500))
        screen.blit(text_points, (530, 300))
        screen.blit(text_points1, (530, 350))
        screen.blit(text_points2, (530, 400))
        screen.blit(text_points3, (530, 450))
        screen.blit(text_points4, (530, 500))
        screen.blit(text_time, (690, 300))
        screen.blit(text_time1, (690, 350))
        screen.blit(text_time2, (690, 400))
        screen.blit(text_time3, (690, 450))
        screen.blit(text_time4, (690, 500))
        screen.blit(text_move, (890, 300))
        screen.blit(text_move1, (890, 350))
        screen.blit(text_move2, (890, 400))
        screen.blit(text_move3, (890, 450))
        screen.blit(text_move4, (890, 500))
    if CARD_COUNT == 30:
        draw_text("Nick       |  Score  |   Time   |  Move  ", font3, TEXT_COL, 340, 235)
        draw_text("__________________________________________", font3, TEXT_COL, 239, 245)
        draw_text("________________________________________________________", font, TEXT_COL, 239, 550)
        draw_text("(6x5)", font, TEXT_COL, 619, 585)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="players"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM score30 ORDER BY player_score DESC")
        myresult = mycursor.fetchall()
        text_name = font3.render(('1. {0}'.format(myresult[0][1])), 1, (255, 199, 0))
        text_name1 = font3.render(('2. {0}'.format(myresult[1][1])), 1, (255, 255, 140))
        text_name2 = font3.render(('3. {0}'.format(myresult[2][1])), 1, (255, 255, 199))
        text_name3 = font3.render(('4. {0}'.format(myresult[3][1])), 1, (255, 255, 255))
        text_name4 = font3.render(('5. {0}'.format(myresult[4][1])), 1, (255, 255, 255))

        text_points = font3.render(('|    {0}'.format(myresult[0][2])), 1, (255, 199, 0))
        text_points1 = font3.render(('|    {0}'.format(myresult[1][2])), 1, (255, 255, 140))
        text_points2 = font3.render(('|    {0}'.format(myresult[2][2])), 1, (255, 255, 199))
        text_points3 = font3.render(('|    {0}'.format(myresult[3][2])), 1, (255, 255, 255))
        text_points4 = font3.render(('|    {0}'.format(myresult[4][2])), 1, (255, 255, 255))

        text_time = font3.render(('  |   {0}'.format(myresult[0][3])), 1, (255, 199, 0))
        text_time1 = font3.render(('  |   {0}'.format(myresult[1][3])), 1, (255, 255, 140))
        text_time2 = font3.render(('  |   {0}'.format(myresult[2][3])), 1, (255, 255, 199))
        text_time3 = font3.render(('  |   {0}'.format(myresult[3][3])), 1, (255, 255, 255))
        text_time4 = font3.render(('  |   {0}'.format(myresult[4][3])), 1, (255, 255, 255))

        text_move = font3.render(('  |    {0}'.format(myresult[0][4])), 1, (255, 199, 0))
        text_move1 = font3.render(('  |    {0}'.format(myresult[1][4])), 1, (255, 255, 140))
        text_move2 = font3.render(('  |    {0}'.format(myresult[2][4])), 1, (255, 255, 199))
        text_move3 = font3.render(('  |    {0}'.format(myresult[3][4])), 1, (255, 255, 255))
        text_move4 = font3.render(('  |    {0}'.format(myresult[4][4])), 1, (255, 255, 255))

        screen.blit(text_name, (230, 300))
        screen.blit(text_name1, (230, 350))
        screen.blit(text_name2, (230, 400))
        screen.blit(text_name3, (230, 450))
        screen.blit(text_name4, (230, 500))
        screen.blit(text_points, (530, 300))
        screen.blit(text_points1, (530, 350))
        screen.blit(text_points2, (530, 400))
        screen.blit(text_points3, (530, 450))
        screen.blit(text_points4, (530, 500))
        screen.blit(text_time, (690, 300))
        screen.blit(text_time1, (690, 350))
        screen.blit(text_time2, (690, 400))
        screen.blit(text_time3, (690, 450))
        screen.blit(text_time4, (690, 500))
        screen.blit(text_move, (890, 300))
        screen.blit(text_move1, (890, 350))
        screen.blit(text_move2, (890, 400))
        screen.blit(text_move3, (890, 450))
        screen.blit(text_move4, (890, 500))
    if CARD_COUNT == 40:
        draw_text("Nick       |  Score  |   Time   |  Move  ", font3, TEXT_COL, 340, 235)
        draw_text("__________________________________________", font3, TEXT_COL, 239, 245)
        draw_text("________________________________________________________", font, TEXT_COL, 239, 550)
        draw_text("(8x5)", font, TEXT_COL, 619, 585)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="players"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM score40 ORDER BY player_score DESC")
        myresult = mycursor.fetchall()
        text_name = font3.render(('1. {0}'.format(myresult[0][1])), 1, (255, 199, 0))
        text_name1 = font3.render(('2. {0}'.format(myresult[1][1])), 1, (255, 255, 140))
        text_name2 = font3.render(('3. {0}'.format(myresult[2][1])), 1, (255, 255, 199))
        text_name3 = font3.render(('4. {0}'.format(myresult[3][1])), 1, (255, 255, 255))
        text_name4 = font3.render(('5. {0}'.format(myresult[4][1])), 1, (255, 255, 255))

        text_points = font3.render(('|    {0}'.format(myresult[0][2])), 1, (255, 199, 0))
        text_points1 = font3.render(('|    {0}'.format(myresult[1][2])), 1, (255, 255, 140))
        text_points2 = font3.render(('|    {0}'.format(myresult[2][2])), 1, (255, 255, 199))
        text_points3 = font3.render(('|    {0}'.format(myresult[3][2])), 1, (255, 255, 255))
        text_points4 = font3.render(('|    {0}'.format(myresult[4][2])), 1, (255, 255, 255))

        text_time = font3.render(('  |   {0}'.format(myresult[0][3])), 1, (255, 199, 0))
        text_time1 = font3.render(('  |   {0}'.format(myresult[1][3])), 1, (255, 255, 140))
        text_time2 = font3.render(('  |   {0}'.format(myresult[2][3])), 1, (255, 255, 199))
        text_time3 = font3.render(('  |   {0}'.format(myresult[3][3])), 1, (255, 255, 255))
        text_time4 = font3.render(('  |   {0}'.format(myresult[4][3])), 1, (255, 255, 255))

        text_move = font3.render(('  |    {0}'.format(myresult[0][4])), 1, (255, 199, 0))
        text_move1 = font3.render(('  |    {0}'.format(myresult[1][4])), 1, (255, 255, 140))
        text_move2 = font3.render(('  |    {0}'.format(myresult[2][4])), 1, (255, 255, 199))
        text_move3 = font3.render(('  |    {0}'.format(myresult[3][4])), 1, (255, 255, 255))
        text_move4 = font3.render(('  |    {0}'.format(myresult[4][4])), 1, (255, 255, 255))

        screen.blit(text_name, (230, 300))
        screen.blit(text_name1, (230, 350))
        screen.blit(text_name2, (230, 400))
        screen.blit(text_name3, (230, 450))
        screen.blit(text_name4, (230, 500))
        screen.blit(text_points, (530, 300))
        screen.blit(text_points1, (530, 350))
        screen.blit(text_points2, (530, 400))
        screen.blit(text_points3, (530, 450))
        screen.blit(text_points4, (530, 500))
        screen.blit(text_time, (690, 300))
        screen.blit(text_time1, (690, 350))
        screen.blit(text_time2, (690, 400))
        screen.blit(text_time3, (690, 450))
        screen.blit(text_time4, (690, 500))
        screen.blit(text_move, (890, 300))
        screen.blit(text_move1, (890, 350))
        screen.blit(text_move2, (890, 400))
        screen.blit(text_move3, (890, 450))
        screen.blit(text_move4, (890, 500))


def gameptext():
    global time_str
    current_time = time.time()
    elapsed_time = current_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    time_str = f"{int(minutes):02d}:{int(seconds):02d}"
    draw_text(f"Time: {time_str}", font, TEXT_COL, 290, 50)
    draw_text(f"Scores: {score}", font, TEXT_COL, 580, 50)
    draw_text(f"Moves: {move_counter}", font, TEXT_COL, 870, 50)
    draw_text(f"> {player_name}", font, TEXT_COL, 200, 670)
    if CARD_COUNT == 16:
        draw_text("(16)", font, GRAY, 1050, 670)
    if CARD_COUNT == 30:
        draw_text("(30)", font, GRAY, 1050, 670)
    if CARD_COUNT == 40:
        draw_text("(40)", font, GRAY, 1050, 670)


def gameptext2():
    global time_str
    current_time = time.time()
    elapsed_time = current_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    time_str = f"{int(minutes):02d}:{int(seconds):02d}"
    draw_text(f"Time: {time_str}", font, TEXT_COL, 290, 50)
    draw_text(f"Moves: {move_counter}", font, TEXT_COL, 870, 50)
    draw_text(f" {player_name}: {p1score}", font, TEXT_COL, 300, 670)
    draw_text(f" {player2_name}: {p2score}", font, TEXT_COL, 700, 670)
    if current_player == 1:
        draw_text(">", font, TEXT_COL, 285, 670)
    if current_player == 2:
        draw_text(">", font, TEXT_COL, 685, 670)


def draw_score():
    score_text = font.render("Score: " + str(p1score), True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)
    screen.blit(score_text, score_rect)


def gameotext():
    global player_name
    '''
    draw_text(f"Time: {time_str}", font, BLACK, 290, 353)
    draw_text("Scores: " + str(p1score), font, BLACK, 580, 353)
    draw_text("Moves: " + str(move_counter), font, BLACK, 870, 353)
    '''
    draw_text(f"Time: {time_str}", font, TEXT_COL, 290, 370)
    draw_text("Scores: " + str(score), font, TEXT_COL, 580, 370)
    draw_text("Moves: " + str(move_counter), font, TEXT_COL, 870, 370)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database="players"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT MAX(player_score) FROM score16")
    max = mycursor.fetchone()[0]

    if score > max:
        draw_text("New Best Score !", font, TEXT_COL, 485, 470)

    draw_text(str(player_name), font1, BLACK, 684, 226)
    draw_text(str(player_name), font1, WHITE, 680, 226)


def gameotext2():
    global player_name
    '''
    draw_text(f"Time: {time_str}", font, BLACK, 290, 353)
    draw_text("Scores: " + str(p1score), font, BLACK, 580, 353)
    draw_text("Moves: " + str(move_counter), font, BLACK, 870, 353)
    '''
    draw_text(f"Time: {time_str}", font, TEXT_COL, 290, 370)
    draw_text("Scores: " + str(kscore), font, TEXT_COL, 580, 370)
    draw_text("Moves: " + str(move_counter), font, TEXT_COL, 870, 370)

    draw_text(str(kazanan), font1, BLACK, 684, 226)
    draw_text(str(kazanan), font1, WHITE, 680, 226)


def get_time_str():
    return time.strftime("%H:%M:%S", time.gmtime())


CARD_WIDTH = 130
CARD_HEIGHT = 100

# kart ciftleri
CARD_COUNT = 16
NUM_UNIQUE_NUMBERS = CARD_COUNT // 2

# kartlardaki rakamlar
card_numbers = list(range(1, NUM_UNIQUE_NUMBERS + 1)) * 2

# kartlari kariştir
random.shuffle(card_numbers)

image_paths = [
    "images/cardi/yem1.png",
    "images/cardi/yem2.png",
    "images/cardi/yem3.png",
    "images/cardi/yem4.png",
    "images/cardi/yem5.png",
    "images/cardi/yem6.png",
    "images/cardi/yem7.png",
    "images/cardi/yem8.png",
]

random.shuffle(image_paths)
image_paths *= 2

# kart biçimleri
cards = []
for i in range(CARD_COUNT):
    x = (i % 4) * (CARD_WIDTH + 130) + 200
    y = (i // 4) * (CARD_HEIGHT + 30) + 150
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
    card.image_path = image_paths[i]


def onalti():
    global CARD_WIDTH
    global CARD_HEIGHT
    global CARD_COUNT
    global NUM_UNIQUE_NUMBERS
    global card_numbers
    global cards
    global card
    CARD_WIDTH = 130
    CARD_HEIGHT = 100

    # kart ciftleri
    CARD_COUNT = 16
    NUM_UNIQUE_NUMBERS = CARD_COUNT // 2

    # kartlardaki rakamlar
    card_numbers = list(range(1, NUM_UNIQUE_NUMBERS + 1)) * 2

    # kartlari kariştir
    random.shuffle(card_numbers)

    # kart biçimleri
    cards = []
    for i in range(CARD_COUNT):
        x = (i % 4) * (CARD_WIDTH + 130) + 200
        y = (i // 4) * (CARD_HEIGHT + 30) + 150
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
        card.image_path = image_paths[i]


def otuz():
    global CARD_WIDTH
    global CARD_HEIGHT
    global CARD_COUNT
    global NUM_UNIQUE_NUMBERS
    global card_numbers
    global cards
    global card
    CARD_WIDTH = 110
    CARD_HEIGHT = 70

    # kart ciftleri
    CARD_COUNT = 30
    NUM_UNIQUE_NUMBERS = CARD_COUNT // 2

    # kartlardaki rakamlar
    card_numbers = list(range(1, NUM_UNIQUE_NUMBERS + 1)) * 2

    # kartlari kariştir
    random.shuffle(card_numbers)

    # kart biçimleri
    cards = []
    for i in range(CARD_COUNT):
        x = (i % 5) * (CARD_WIDTH + 100) + 170
        y = (i // 5) * (CARD_HEIGHT + 20) + 140
        card = pygame.sprite.Sprite()
        card.image = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        card.image.fill(WHITE)
        pygame.draw.rect(card.image, GRAY, card.image.get_rect(), border_radius=10)
        pygame.draw.rect(card.image, BLACK, card.image.get_rect(), width=2, border_radius=10)
        card.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        card.number = card_numbers[i]
        cards.append(card)


def kirk():
    global CARD_WIDTH
    global CARD_HEIGHT
    global CARD_COUNT
    global NUM_UNIQUE_NUMBERS
    global card_numbers
    global cards
    global card
    CARD_WIDTH = 110
    CARD_HEIGHT = 60

    # kart ciftleri
    CARD_COUNT = 40
    NUM_UNIQUE_NUMBERS = CARD_COUNT // 2

    # kartlardaki rakamlar
    card_numbers = list(range(1, NUM_UNIQUE_NUMBERS + 1)) * 2

    # kartlari kariştir
    random.shuffle(card_numbers)

    # kart biçimleri
    cards = []
    for i in range(CARD_COUNT):
        x = (i % 5) * (CARD_WIDTH + 90) + 200
        y = (i // 5) * (CARD_HEIGHT + 10) + 120
        card = pygame.sprite.Sprite()
        card.image = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        card.image.fill(WHITE)
        pygame.draw.rect(card.image, GRAY, card.image.get_rect(), border_radius=10)
        pygame.draw.rect(card.image, BLACK, card.image.get_rect(), width=2, border_radius=10)
        card.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        card.number = card_numbers[i]
        cards.append(card)


flipped_cards = []
matched_cards = []
game_over = False
move_counter = 0
p1score = 0
p2score = 0
score = 0

card_back = pygame.image.load('images/card_back.png')
cardback_width = CARD_WIDTH
cardback_height = CARD_HEIGHT
card_back = pygame.transform.scale(card_back, (cardback_width, cardback_height))
card_back0 = pygame.image.load('images/card_back0.png')
cardback_width = CARD_WIDTH
cardback_height = CARD_HEIGHT
card_back0 = pygame.transform.scale(card_back0, (cardback_width, cardback_height))
card_back1 = pygame.image.load('images/card_back1.png')
cardback_width = CARD_WIDTH
cardback_height = CARD_HEIGHT
card_back1 = pygame.transform.scale(card_back1, (cardback_width - 23, cardback_height - 40))

ps_back = pygame.image.load('images/cardd.png')
cardback_width = CARD_WIDTH
cardback_height = CARD_HEIGHT
ps_back = pygame.transform.scale(ps_back, (cardback_width, cardback_height))

ps_back0 = pygame.image.load('images/cardd0.png')
cardback_width = CARD_WIDTH
cardback_height = CARD_HEIGHT
ps_back0 = pygame.transform.scale(ps_back0, (cardback_width, cardback_height))

ps_back1 = pygame.image.load('images/cardd1.png')
cardback_width = CARD_WIDTH
cardback_height = CARD_HEIGHT
ps_back1 = pygame.transform.scale(ps_back1, (cardback_width, cardback_height))


# kartlar
def draw_card(card):
    global ps_back
    global ps_back0
    global ps_back1

    if card_type == "stock":
        if card in matched_cards:
            pygame.draw.rect(screen, GREEN, card.rect, border_radius=10)
            pygame.draw.rect(screen, BLACK, card.rect, width=3, border_radius=10)
            number_text = font.render(str(card.number), True, BLACK)
            number_rect = number_text.get_rect()
            number_rect.center = card.rect.center
            screen.blit(card.image, card.rect)
        elif card in flipped_cards:
            pygame.draw.rect(screen, GRAY1, card.rect, border_radius=10)
            pygame.draw.rect(screen, BLACK, card.rect, width=3, border_radius=10)
            number_text = font.render(str(card.number), True, BLACK)
            number_rect = number_text.get_rect()
            number_rect.center = card.rect.center
            screen.blit(card.image, card.rect)
        else:
            if CARD_COUNT == 16:
                screen.blit(card_back, card.rect)
                mouse_pos = pygame.mouse.get_pos()
                if card.rect.collidepoint(mouse_pos):
                    screen.blit(card_back, card.rect)
                    pygame.draw.rect(screen, ORANGE, card.rect, width=5, border_radius=7)
            if CARD_COUNT == 30:
                screen.blit(card_back0, card.rect)
                mouse_pos = pygame.mouse.get_pos()
                if card.rect.collidepoint(mouse_pos):
                    screen.blit(card_back0, card.rect)
                    pygame.draw.rect(screen, BLUE1, card.rect, width=3, border_radius=7)
            if CARD_COUNT == 40:
                screen.blit(card_back1, card.rect)
                mouse_pos = pygame.mouse.get_pos()
                if card.rect.collidepoint(mouse_pos):
                    screen.blit(card_back1, card.rect)
                    pygame.draw.rect(screen, PURPLE, card.rect, width=5, border_radius=7)

    if card_type == "special":
        if card in matched_cards:
            if card_typee == "ps":
                pygame.draw.rect(screen, (75, 0, 130), card.rect, border_radius=10)
                pygame.draw.rect(screen, (255, 223, 0), card.rect, width=3, border_radius=10)
                number_text = font.render(str(card.number), True, (255, 223, 0))
            if card_typee == "ps0":
                pygame.draw.rect(screen, (0, 100, 90), card.rect, border_radius=10)
                pygame.draw.rect(screen, YELLOW, card.rect, width=3, border_radius=10)
                number_text = font.render(str(card.number), True, BLACK)
            if card_typee == "ps1":
                pygame.draw.rect(screen, GREEN, card.rect, border_radius=10)
                pygame.draw.rect(screen, BLACK, card.rect, width=3, border_radius=10)
                number_text = font.render(str(card.number), True, BLACK)
            number_rect = number_text.get_rect()
            number_rect.center = card.rect.center
            screen.blit(number_text, number_rect)
        elif card in flipped_cards:
            if card_typee == "ps":
                pygame.draw.rect(screen, (138, 43, 226), card.rect, border_radius=10)
                pygame.draw.rect(screen, YELLOW, card.rect, width=3, border_radius=10)
                number_text = font.render(str(card.number), True, BLACK)
            if card_typee == "ps0":
                pygame.draw.rect(screen, (32, 178, 170), card.rect, border_radius=10)
                pygame.draw.rect(screen, BLACK, card.rect, width=3, border_radius=10)
                number_text = font.render(str(card.number), True, BLACK)
            if card_typee == "ps1":
                pygame.draw.rect(screen, GRAY1, card.rect, border_radius=10)
                pygame.draw.rect(screen, BLACK, card.rect, width=3, border_radius=10)
                number_text = font.render(str(card.number), True, BLACK)
            number_rect = number_text.get_rect()
            number_rect.center = card.rect.center
            screen.blit(number_text, number_rect)
        else:
            if card_typee == "ps":
                if CARD_COUNT == 16:
                    ps_back = pygame.transform.scale(ps_back, (cardback_width, cardback_height))
                if CARD_COUNT == 30:
                    ps_back = pygame.transform.scale(ps_back, (cardback_width - 23, cardback_height - 30))
                if CARD_COUNT == 40:
                    ps_back = pygame.transform.scale(ps_back, (cardback_width - 23, cardback_height - 40))
                screen.blit(ps_back, card.rect)
                mouse_pos = pygame.mouse.get_pos()
                if card.rect.collidepoint(mouse_pos):
                    screen.blit(ps_back, card.rect)
                    pygame.draw.rect(screen, CARD, card.rect, width=5, border_radius=7)
            if card_typee == "ps0":
                if CARD_COUNT == 16:
                    ps_back0 = pygame.transform.scale(ps_back0, (cardback_width, cardback_height))
                if CARD_COUNT == 30:
                    ps_back0 = pygame.transform.scale(ps_back0, (cardback_width - 23, cardback_height - 30))
                if CARD_COUNT == 40:
                    ps_back0 = pygame.transform.scale(ps_back0, (cardback_width - 23, cardback_height - 40))
                screen.blit(ps_back0, card.rect)
                mouse_pos = pygame.mouse.get_pos()
                if card.rect.collidepoint(mouse_pos):
                    screen.blit(ps_back0, card.rect)
                    pygame.draw.rect(screen, CARD0, card.rect, width=5, border_radius=7)
            if card_typee == "ps1":
                if CARD_COUNT == 16:
                    ps_back1 = pygame.transform.scale(ps_back1, (cardback_width, cardback_height))
                if CARD_COUNT == 30:
                    ps_back1 = pygame.transform.scale(ps_back1, (cardback_width - 23, cardback_height - 30))
                if CARD_COUNT == 40:
                    ps_back1 = pygame.transform.scale(ps_back1, (cardback_width - 23, cardback_height - 40))
                screen.blit(ps_back1, card.rect)
                mouse_pos = pygame.mouse.get_pos()
                if card.rect.collidepoint(mouse_pos):
                    screen.blit(ps_back1, card.rect)
                    pygame.draw.rect(screen, CARD1, card.rect, width=5, border_radius=7)


# değerleri sifirlama
def reset():
    global flipped_cards
    flipped_cards = []
    global matched_cards
    matched_cards = []
    global game_over
    game_over = False
    global move_counter
    move_counter = 0
    global p1score
    global p2score
    p1score = 0
    p2score = 0
    global score
    score = 0
    reset_timer()


def drawtextbox():
    global player_name
    player_name = ""
    text_font = pygame.font.SysFont(None, 40)
    textbox_rect = pygame.Rect(500, 470, 300, 60)
    name_entered = False
    while not name_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        pygame.draw.rect(screen, WHITE, textbox_rect)
        pygame.draw.rect(screen, BLACK, textbox_rect, 5)

        if player_name == "":
            text_font = pygame.font.SysFont(None, 30)
            player_text = text_font.render("Player1 Name...", True, GRAY)
        else:
            player_text = text_font.render(player_name, True, BLACK)
        player_rect = player_text.get_rect()
        player_rect.center = textbox_rect.center
        screen.blit(player_text, player_rect)

        pygame.display.update()


def drawtextbox1():
    global player2_name
    player2_name = ""
    text_font = pygame.font.SysFont(None, 40)
    textbox_rect = pygame.Rect(500, 470, 300, 60)
    name_entered = False
    while not name_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    player2_name = player2_name[:-1]
                else:
                    player2_name += event.unicode

        pygame.draw.rect(screen, WHITE, textbox_rect)
        pygame.draw.rect(screen, BLACK, textbox_rect, 5)

        if player2_name == "":
            text_font = pygame.font.SysFont(None, 30)
            player_text = text_font.render("Player2 Name...", True, GRAY)
        else:
            player_text = text_font.render(player2_name, True, BLACK)
        player_rect = player_text.get_rect()
        player_rect.center = textbox_rect.center
        screen.blit(player_text, player_rect)

        pygame.display.update()


def shuffle_cards():
    global card
    global cards
    global flipped_cards
    global matched_cards
    random.shuffle(card_numbers)
    cards = []
    for i in range(CARD_COUNT):
        x = (i % 4) * (CARD_WIDTH + 130) + 200
        y = (i // 4) * (CARD_HEIGHT + 30) + 150
        card = pygame.sprite.Sprite()
        card.image = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        card.image.fill(WHITE)
        card.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        card.number = card_numbers[i]
        cards.append(card)
    flipped_cards = []
    matched_cards = []


# arkaplan
bgImage = pygame.image.load('Background.png')
bgImage = pygame.transform.scale(bgImage, (gameWidth, gameHeight))
bgImageRect = bgImage.get_rect()
mixer.music.play()

player_name = ""
player2_name = ""
oyuncular = [player_name, player2_name]
current_player = 1
gamemode = 0
selected_button = p1_button

# oyun döngüsü
run = True
while run:

    screen.blit(bgImage, bgImageRect)

    if falling == 0:
        cover_button1.draw(screen)
        loading()

    if game_menu == True:

        if menu_durum == "main":
            cover_button.draw(screen)
            if htp_button.draw(screen):
                winsound.PlaySound('Click', 1)
                print("information")
                menu_durum = "htp"
            if bests_button.draw(screen):
                print("bests")
                winsound.PlaySound('Click', 1)
                menu_durum = "bests"
            if settings_button.draw(screen):
                print("settings")
                winsound.PlaySound('Click', 1)
                menu_durum = "settings"
            if mute_button.draw(screen):
                print("muted")
                winsound.PlaySound('Click', 1)
                mixer.music.pause()
            if speak_button.draw(screen):
                print("speak")
                winsound.PlaySound('Click', 1)
                mixer.music.unpause()
            if play_button.draw(screen):
                if CARD_COUNT == 16:
                    onalti()
                if CARD_COUNT == 30:
                    otuz()
                if CARD_COUNT == 40:
                    kirk()
                reset()
                print("started")
                winsound.PlaySound('Click', 1)
                if gamemode == 0:
                    drawtextbox()
                    menu_durum = "started"
                else:
                    drawtextbox()
                    drawtextbox1()
                    menu_durum = "started2"
            if exit_button.draw(screen):
                pygame.quit()
            circle_button0.draw(screen)

            if p1_button.draw(screen):
                circle_button0 = button.Button(542, 460, circle_image, 0.3)
                print("selected 1p")
                winsound.PlaySound('Click', 1)
                gamemode = 0
            if p2_button.draw(screen):
                draw_text("multiplayer", font5, GRAY1, 560, 540)
                circle_button0 = button.Button(643, 459, circle_image, 0.3)
                print("selected 2p")
                winsound.PlaySound('Click', 1)
                gamemode = 1
            if gamemode == 0:
                draw_text("singleplayer", font5, YELLOW, 560, 555)
            else:
                draw_text("multiplayer", font5, YELLOW, 571, 555)

        if menu_durum == "settings":
            settingstext_button.draw(screen)
            setttext()
            if back_button.draw(screen):
                winsound.PlaySound('Click', 1)
                if (card_typee != " " or card_type == "stock"):
                    menu_durum = "main"
                if (card_typee == " " and card_type != "stock"):
                    box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
                    box1.fill((199, 199, 199, 90))
                    screen.blit(box1, (678, 415))
                    box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
                    box1.fill((199, 199, 199, 90))
                    screen.blit(box1, (832, 415))
                    box1 = pygame.Surface((150, 230), pygame.SRCALPHA)
                    box1.fill((199, 199, 199, 90))
                    screen.blit(box1, (986, 415))
                    pygame.display.update()
                    pygame.time.wait(1000)

        if menu_durum == "htp":
            htptext_button.draw(screen)
            htptext()
            tfptext_button.draw(screen)
            if back_button.draw(screen):
                winsound.PlaySound('Click', 1)
                menu_durum = "main"
        if menu_durum == "bests":
            bestscorestext_button.draw(screen)
            besttext()
            if back_button.draw(screen):
                winsound.PlaySound('Click', 1)
                menu_durum = "main"
        if menu_durum == "gameover":
            bmove = move_counter
            if score > bscore:
                bscore = score
            btime = time_str
            welldonetext_button.draw(screen)
            gameotext()
            if playagaintext_button.draw(screen):
                if CARD_COUNT == 16:
                    onalti()
                if CARD_COUNT == 30:
                    otuz()
                if CARD_COUNT == 40:
                    kirk()
                reset()
                if gamemode == 0:
                    menu_durum = "started"
                else:
                    menu_durum = "started2"
            if backmenutext_button.draw(screen):
                if CARD_COUNT == 16:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="0000",
                        database="players"
                    )
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO score16 (id,player_name,player_score,player_time,player_move) VALUES (%s,%s,%s,%s,%s)"
                    val = (None, player_name, bscore, btime, bmove)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "kaydedildi")
                if CARD_COUNT == 30:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="0000",
                        database="players"
                    )
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO score30 (id,player_name,player_score,player_time,player_move) VALUES (%s,%s,%s,%s,%s)"
                    val = (None, player_name, bscore, btime, bmove)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "kaydedildi")
                if CARD_COUNT == 40:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="0000",
                        database="players"
                    )
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO score40 (id,player_name,player_score,player_time,player_move) VALUES (%s,%s,%s,%s,%s)"
                    val = (None, player_name, bscore, btime, bmove)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "kaydedildi")
                menu_durum = "main"

        if menu_durum == "gameoverr":
            kscore = p1score
            if p1score > p2score:
                kazanan = player_name
                kscore = p1score
            if p2score > p1score:
                kazanan = player2_name
                kscore = p2score
            if p1score == p2score:
                kazanan = "Draw !"
            welldonetext_button.draw(screen)
            gameotext2()
            if playagaintext_button.draw(screen):
                if CARD_COUNT == 16:
                    onalti()
                if CARD_COUNT == 30:
                    otuz()
                if CARD_COUNT == 40:
                    kirk()
                reset()
                if gamemode == 0:
                    menu_durum = "started"
                else:
                    menu_durum = "started2"
            if backmenutext_button.draw(screen):
                menu_durum = "main"

        if menu_durum == "started":
            if exit_button1.draw(screen):
                game_over = True
                menu_durum = "gameover"
            if back_button.draw(screen):
                reset()
                winsound.PlaySound('Click', 1)
                menu_durum = "main"
                print("Timer reset")
            gameptext()
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(flipped_cards) < 2:
                    for card in cards:
                        if card.rect.collidepoint(event.pos):
                            if card not in flipped_cards and card not in matched_cards:
                                winsound.PlaySound('Flip', 1)
                                flipped_cards.append(card)
                                draw_card(card)
                                pygame.display.update()
                                if len(flipped_cards) == 2:
                                    move_counter += 1
                                    if flipped_cards[0].image_path == flipped_cards[1].image_path:
                                        if card_typee == "ps":
                                            winsound.PlaySound('mor', 1)
                                        if card_typee == "ps0":
                                            winsound.PlaySound('yesil', 1)
                                        if card_typee == "ps1":
                                            winsound.PlaySound('kara', 1)
                                        if card_type == "stock":
                                            winsound.PlaySound('Correct', 1)
                                        matched_cards.extend(flipped_cards)
                                        flipped_cards = []
                                        score += 100
                                        if len(matched_cards) == CARD_COUNT:  # tüm kartlar eşlenince
                                            winsound.PlaySound('Won', 1)
                                            pygame.time.delay(1000)
                                            game_over = True
                                        if len(matched_cards) == CARD_COUNT and score == 800:  # tüm kartlar dogru eşlenirşe
                                            winsound.PlaySound('Choir', 1)
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

            # Draw all cards
            for card in cards:
                draw_card(card)

            # Oyun bittiğinde
            if game_over:
                shuffle_cards()
                menu_durum = "gameover"
            pygame.display.flip()

        if menu_durum == "started2":
            if exit_button1.draw(screen):
                game_over = True
                menu_durum = "gameoverr"
            if back_button.draw(screen):
                reset()
                winsound.PlaySound('Click', 1)
                menu_durum = "main"
                print("Timer reset")
            gameptext2()
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(flipped_cards) < 2:
                    for card in cards:
                        if card.rect.collidepoint(event.pos):
                            if card not in flipped_cards and card not in matched_cards:
                                winsound.PlaySound('Flip', 1)
                                flipped_cards.append(card)
                                draw_card(card)
                                pygame.display.update()
                                if len(flipped_cards) == 2:
                                    move_counter += 1
                                    if flipped_cards[0].number == flipped_cards[1].number:
                                        if card_typee == "ps":
                                            winsound.PlaySound('mor', 1)
                                        if card_typee == "ps0":
                                            winsound.PlaySound('yesil', 1)
                                        if card_typee == "ps1":
                                            winsound.PlaySound('kara', 1)
                                        if card_type == "stock":
                                            winsound.PlaySound('Correct', 1)
                                        matched_cards.extend(flipped_cards)
                                        flipped_cards = []
                                        if current_player == 1:
                                            p1score += 100
                                            current_player = 1
                                        else:
                                            p2score += 100
                                            current_player = 2
                                        if len(matched_cards) == CARD_COUNT:  # tüm kartlar eşlenince
                                            pygame.time.delay(1000)
                                            game_over = True
                                    else:
                                        if current_player == 1:
                                            p1score -= 10
                                            current_player = 2
                                        else:
                                            p2score -= 10
                                            current_player = 1
                                        pygame.time.wait(500)
                                        for card in flipped_cards:
                                            draw_card(card)
                                        pygame.display.update()
                                        flipped_cards = []
            for card in cards:
                draw_card(card)

                # oyun bittiğinde
            if game_over:
                menu_durum = "gameoverr"
            pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # ekran güncelle
        pygame.display.update()

pygame.quit()
