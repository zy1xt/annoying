import pygame
import keyboard
import threading
import os
import random

pygame.init()

sound_folder = "D:/neoc/sound"

pygame.mixer.init()
pygame.mixer.set_num_channels(10)

def burenyuu():
    channel = pygame.mixer.find_channel()
    if channel:
        sound_files = os.listdir(sound_folder)
        random_sound = random.choice(sound_files)
        sound_path = os.path.join(sound_folder, random_sound)
        sound = pygame.mixer.Sound(sound_path)
        channel.play(sound)

def CHINA(event):
    if event.event_type == keyboard.KEY_DOWN:
        threading.Thread(target=burenyuu).start()

keyboard.hook(CHINA)

while True:
    keyboard.wait(9999999999)