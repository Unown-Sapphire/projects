import tkinter as tk
import chestImages
import API
from PIL import ImageTk, Image

upcomingChest = chestImages.canvas
account_name = API.player_name
account_wins = API.player_wins
account_3CW = API.player_3_crownwins
account_clans = API.player_clan['name']

bg = '#333333'
fg = '#ffffff'

app = tk.Tk()
app.geometry("1000x500")
app.configure(bg=bg)


accountName = tk.Label(app, text=f"{account_name}", font=("Supercell-Magic", 20), bg=bg, fg=fg)
accountName.pack()

accountWins = tk.Label(app, text=f'Wins: {account_wins}', font=("Supercell-Magic", 12), bg=bg, fg=fg)
accountWins.pack()

account3CW = tk.Label(app, text=f'3 Crown Wins: {account_3CW}', font=("Supercell-Magic", 12), bg=bg, fg=fg)
account3CW.pack()

accountClan = tk.Label(app, text=f'Clan: {account_clans}', font=("Supercell-Magic", 12), bg=bg, fg=fg)
accountClan.pack()

blank_space = tk.Label(app, text=" ", bg=bg, fg=fg)
blank_space.pack()

chestUpcoming = tk.Label(app, text="Upcoming Chests:", font=("Supercell-Magic", 12), bg=bg, fg=fg)
chestUpcoming.pack()

blank_space = tk.Label(app, text=" ", bg=bg, fg=fg)
blank_space.pack()

img = Image.open("chest.png")
img = img.resize(size=(800,184))
img = ImageTk.PhotoImage(img)

chest_images = tk.Label(app, image=img, bg=bg, fg=fg)
chest_images.pack()

app.mainloop()