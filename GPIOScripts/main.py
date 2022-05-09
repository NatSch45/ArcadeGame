import pygame, sys
from button import Button
import RPi.GPIO as GPIO

BUTTON_PIN = 33
BUTTON_PIN_1 = 35
BUTTON_PIN_2 = 37
BUTTON_PIN_3 = 31
BUTTON_PIN_4 = 23

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        #PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("BLUE")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        #PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                main_menu()

        pygame.display.update()
    
def options():
    while True:
        #OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        #OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        #MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100)
        MENU_TEST = MENU_TEXT.render("MAIN MENU", True, (0,123,156))
        MENU_RECT = MENU_TEST.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/PlayRect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="BLUE", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/OptionsRect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="BLUE", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/QuitRect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="BLUE", hovering_color="White")

        SCREEN.blit(MENU_TEST, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            #button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
      
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            play()
            echo ("play")
        if GPIO.input(BUTTON_PIN_1) == GPIO.HIGH:
            options()
            echo ("opt")
        if GPIO.input(BUTTON_PIN_2) == GPIO.HIGH:
            echo ("quit")
            pygame.quit()
            sys.exit()

        pygame.display.update()

main_menu()