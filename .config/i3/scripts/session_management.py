import os
import sys
import tkinter as tk
from tkinter import font


class Window:
    def __init__(self, text, command):
        self.text = text
        self.command = command

        # Colors
        self.bg_color = "#282A36"
        self.fg_color = "#FFFFFF"
        self.alt_bg_color = "#44475A"

        # Creating window
        self.root = tk.Tk()

        # Configuring the window
        # self.root.geometry("350x125")
        self.root.configure(bg=self.bg_color)
        self.root.attributes("-type", "dialog")

        # Adding Fonts
        self.font1 = font.Font(
            family="FiraCode Nerd Font",
            size=16,
            weight="bold",
        )
        self.font2 = font.Font(
            family="FiraCode Nerd Font",
            size=12,
        )

        # Adding Widgets
        self._add_widgets()

        # Autoclose window
        self.root.after(60000, self.cancel)

        # Keybindings
        self.root.bind("<Return>", self.confirm)
        self.root.bind("<Escape>", self.cancel)

        self.root.mainloop()

    def _add_widgets(self):
        # Creating a Label
        tk.Label(
            self.root,
            text=self.text,
            bg=self.bg_color,
            fg=self.fg_color,
            font=self.font1,
            anchor="center",
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            ipadx=25,
            ipady=25,
            sticky="nsew",
        )

        # Creating Buttons
        tk.Button(
            self.root,
            text="Cancel",
            background=self.bg_color,
            foreground=self.fg_color,
            activebackground=self.alt_bg_color,
            activeforeground=self.fg_color,
            highlightbackground=self.alt_bg_color,
            font=self.font2,
            bd=0,
            relief="flat",
            command=self.cancel,
        ).grid(
            row=1,
            column=0,
            sticky="nsew",
        )

        tk.Button(
            self.root,
            text="Yes",
            background=self.bg_color,
            foreground=self.fg_color,
            activebackground=self.alt_bg_color,
            activeforeground=self.fg_color,
            highlightbackground=self.alt_bg_color,
            font=self.font2,
            bd=0,
            relief="flat",
            command=self.confirm,
        ).grid(
            row=1,
            column=1,
            sticky="nsew",
        )

    def confirm(self, event=None):
        # Close the window
        self.root.destroy()

        # Execute the command
        os.system(self.command)

    def cancel(self, event=None):
        # Close the window
        self.root.destroy()


def main():
    if len(sys.argv) < 2:
        print("No command specified...")
    elif sys.argv[1] == "logout":
        Window("Do you want to Logout?", "i3 exit")
    elif sys.argv[1] == "reboot":
        Window("Do you want to Reboot?", "reboot")
    elif sys.argv[1] == "poweroff":
        Window("Do you want to Poweroff?", "poweroff")


if __name__ == "__main__":
    main()
