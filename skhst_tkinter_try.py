from tkinter import *
import pygame

def CheckInputConfirmation(inputtext,window):
    _value = inputtext.get("1.0",'end-1c')
    _match = 'I understand the consequences'
    # print(_value, _value==_match)
    if(_value == _match or _value == _match.upper()):
        window.destroy()

def play_sound():
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play(loops=0)

def increase_play_sound_on_cancel(toplevel):
    pygame.mixer.music.set_volume(0.8)
    toplevel.destroy()

def disable_close_button():
    pass 

def clickAbout(window):
    pygame.mixer.music.set_volume(0.3)
    toplevel = Toplevel()
    toplevel.protocol("WM_DELETE_WINDOW", lambda:increase_play_sound_on_cancel(toplevel))
    toplevel.title('Confirm')
    toplevel.geometry("500x300")
    toplevel.configure(bg="#FF9F45")
    lbl1 = Label(toplevel, text="Confirm", bg="#FF9F45", fg="white", font="none 25 bold")
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    lbl1 = Label(toplevel, text="Please type in I understand the consequences in the input box", bg="#FF9F45", fg="white", font="none 11 bold")
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    inputtxt = Text(toplevel,height = 1,width = 30, pady=5)
    inputtxt.pack(ipadx = 1,ipady = 1, expand=True)
    b2 = Button(toplevel, text = "CONFIRM", command= lambda : CheckInputConfirmation(inputtxt,window),width=20,foreground='white', background='#F76E11',activeforeground='white' ,activebackground='#F76E11',relief = FLAT)
    b2.pack(expand = True, ipady = 10)


def main():
    window = Tk()
    window.title("StudioX")
    window.geometry("700x450")
    window.configure(bg="#FF9F45")
    pygame.mixer.init()
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=0)

    #center this label
    lbl1 = Label(window, text="ALERT", bg="#FF9F45", fg="white", font="none 45 bold")
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    
    lbl2 = Label (window, text="Temperature Breach", bg="#FF9F45", fg="white", font="none 12 bold")
    lbl2.config(anchor=CENTER)
    lbl2.pack()

    last_temp = 10
    lbl3 = Label(window, text='Last Temperature Reading : ' + str(last_temp), bg='#FF9F45', fg='white',font="none 10 bold")
    lbl3.config(anchor=CENTER)
    lbl3.pack()

    b2 = Button(window, text = "Supress Alert", command=lambda : clickAbout(window),width=20, font="none 15",
    foreground='white', background='#F76E11',activeforeground='white' ,activebackground='#F76E11',relief = FLAT)
    b2.pack(expand = True, ipady = 10, )
    window.protocol("WM_DELETE_WINDOW", disable_close_button)
    
    window.mainloop()