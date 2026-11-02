import tkinter as tk
from tkinter import messagebox

def bootWindows():
    print("Run bat file here")

def bootUbuntu():
    print("Bro idfk how to do ts on mint")

def checkOS():
    ubuntu = messagebox.askquestion("Wait!", "Are you running Ubuntu?")
    if ubuntu == "yes":
        run = messagebox.askokcancel("Holy peak", "Booting now!")
        if run:
            bootUbuntu()
        else:
            return
    else:
        win11 = messagebox.askquestion("Hmm...", "Windows 11?")
        if win11 == "yes":
            run = messagebox.askokcancel("Not my first choice but it's your pc i suppose...", "Booting now!")
            if run:
                bootWindows()
            else:
                return
        else:
            retry = messagebox.askretrycancel("I haven't thought that far ahead, I'll be honest.", "Sorry... You're on your own mate.", icon = "warning")
            if retry:
                checkOS()

checkOS()