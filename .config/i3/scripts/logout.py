import os
import tkinter as tk
from tkinter import font


class Window:
    def __init__(self):
        # Creating window
        self.main_window = tk.Tk()
        self.main_window.geometry("350x125")
        self.main_window.attributes('-type', 'dialog')
        self.main_window.configure(bg="#282A36")

        # Fonts
        self.font1 = font.Font(family="FiraCode Nerd Font", size=16)
        self.font2 = font.Font(family="FiraCode Nerd Font", size=12)

        # Adding widgets
        self.add_widgets()

        # Autoclose window after 60 seconds
        self.main_window.after(60000, self.main_window.destroy)

        # Keybindings
        self.main_window.bind("<Return>", self.logout)
        self.main_window.bind("<Escape>", self.cancel)

        # Starting mainloop
        self.main_window.mainloop()

    def add_widgets(self):
        tk.Label(
            self.main_window,
            text="Do you want to Logout?",
            bg="#282A36",
            fg="#FFFFFF",
            font=self.font1,
        ).grid(row=0, column=0, columnspan=2, ipadx=30, ipady=30)

        tk.Button(
            self.main_window,
            text="Cancel",
            bg="#282A36",
            fg="#FFFFFF",
            font=self.font2,
            command=self.cancel,
        ).grid(row=1, column=0, sticky="nsew")

        tk.Button(
            self.main_window,
            text="Yes",
            bg="#282A36",
            fg="#FFFFFF",
            font=self.font2,
            command=self.logout,
        ).grid(row=1, column=1, sticky="nsew")

    def logout(self, event=None):
        # Close the Window
        self.main_window.destroy()

        # Logout
        os.system("i3 exit")

    def cancel(self, event=None):
        # Close window
        self.main_window.destroy()


Window()
