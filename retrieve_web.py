import requests, time
import skhst_tkinter_try
import pygame
import webbrowser
threshold_temp = 30.0

def play_sound():
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play(loops=10)

def increase_play_sound_on_cancel(toplevel):
    pygame.mixer.music.set_volume(0.8)
    # toplevel.destroy()

pygame.mixer.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.set_volume(0.8)
# pygame.mixer.music.play(loops=0)
while(True):
    msg=requests.get("https://thingspeak.com/channels/1361501/field/1")
    msg=msg.json()['feeds'][-1]['field1']
    temp_reading = float(str(msg).strip())
    print(temp_reading)
    if(temp_reading>threshold_temp):
        # site = open('mail.html')
        webbrowser.open_new_tab('main.html')
        play_sound()
        # skhst_tkinter_try.main(temp_reading)
        break
print('Restart the service..')