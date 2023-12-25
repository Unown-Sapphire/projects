import clashroyale
import requests
import tkinter as tk
import pandas as pd

token = clashroyale.official_api.Client("#YOUR OWN API KEY")

headers = {
    "Content-Type": "text/plain", 
    "Authorization": "Bearer #YOUR OWN API KEY"
}

bg = '#333333'
fg = '#ffffff'

app = tk.Tk()
app.geometry("500x500")
app.configure(bg=bg)

heading = tk.Label(app, text="Clash Royale Account Searcher", font=('Arial', 20), bg=bg, fg=fg)
heading.pack()

player_heading = tk.Label(app, text="Please enter the player tag (without the #)", bg=bg, fg=fg)
player_heading.pack()
player_tag = tk.Entry(app, justify="center", bg=bg, fg=fg) #208J8JPLV --MegaNyte (example)
player_tag.pack()

def onButtonClick():
    player_tag_get = str(player_tag.get())
    global player_info
    def player_info():
        player_url = f'https://api.clashroyale.com/v1/players/%23{player_tag_get}/'
        player_json = requests.get(player_url, headers=headers).json()
        
        global player_name
        player_name = player_json['name']

        global player_wins
        player_wins = player_json['wins']
        
        global player_3_crownwins
        player_3_crownwins = player_json["threeCrownWins"]
        
        global player_clan
        player_clan = player_json['clan']
        
        print(f"Player's name: {player_name}")
        print(f"Wins: {player_wins}")
        print(f"3 Crown wins: {player_3_crownwins}")
        print(f"Player's clan: {player_clan['name']}")
        print(f"Player's clan role: {player_json['role']}")

    global chest
    def chest():
        chest_url = f"https://api.clashroyale.com/v1/players/%23{player_tag_get}/upcomingchests"
        chest_json = requests.get(chest_url, headers=headers).json()
        # print(json.dumps(chest_json, indent=2))

        chest_json_items = chest_json["items"]
        chest_list = list(chest_json_items[0:])
        
        global chestNumber
        chestNumber = []
        global upcomingChest
        upcomingChest = []

        for i in chest_list:
            chest_number = i['index']
            upcoming_chest = i['name']
            chestNumber.append(chest_number)
            upcomingChest.append(upcoming_chest)

        chest_dict = {
            'chest_number' : chestNumber,
            'name_chest' : upcomingChest
        }      
        df = pd.DataFrame(data=chest_dict)
        print(df)
    player_info()
    chest()

entry_button = tk.Button(app, text="Submit Data", command=lambda:[onButtonClick()], bg=bg, fg=fg)
entry_button.pack()

app.mainloop()
