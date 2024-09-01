import tkinter
import customtkinter
import refresh
import configparser


# Load the configuration file
config = configparser.ConfigParser()
config.read("config.ini")

# Parse the configuration file
HOST1 = config["DEFAULT"]["HOST1"]
PORT1 = int(config["DEFAULT"]["PORT1"])

HOST2 = config["DEFAULT"]["HOST2"]
PORT2 = int(config["DEFAULT"]["PORT2"])

HOSTS = [(HOST1, PORT1), (HOST2, PORT2)]


theme = config["APPEARANCE"]["THEME"]
color = config["APPEARANCE"]["COLOR"].lower()

# System settings
customtkinter.set_appearance_mode(theme)
customtkinter.set_default_color_theme(color)


# Window frame settings
app = customtkinter.CTk()
app.title("Is The Port Open - v0.3")

app.geometry("450x350")
app.resizable(False, False)

# UI Elements
title = customtkinter.CTkLabel(app, text="Is The Port Open", font=("Arial", 22))
title.pack(pady=15)

address1 = customtkinter.CTkLabel(app, text="Host: " + HOST1 + " | Port: " + str(PORT1), font=("Arial", 15))
address1.pack()

address2 = customtkinter.CTkLabel(app, text="Host: " + HOST2 + " | Port: " + str(PORT2), font=("Arial", 15))
address2.pack()

adresses = [address1, address2]

def load():
    refresh.refreshConnection(HOSTS, adresses)

load()

refresh_button = customtkinter.CTkButton(
    app,
    text="Refresh",
    command=lambda: refresh.refreshConnection(HOSTS, adresses),
    width=100,
    height=35,
    corner_radius=10,
    font=("Arial", 18)
)
refresh_button.pack(pady=25)

# Open the app
app.mainloop()
