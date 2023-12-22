import clashroyale
import requests
import tkinter
import pandas as pd

token = clashroyale.official_api.Client("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJkNDY4MmZjLWJmNGQtNDY5ZC04NDhlLWU2NTE3NjhmMjlkNiIsImlhdCI6MTcwMzE4NTExNSwic3ViIjoiZGV2ZWxvcGVyLzhkZWI0YWEwLWU5YjgtYzM4Mi01MmZjLWQ3NTIxM2MyODI1MSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyMjMuMjMzLjgwLjE3MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.9w7Ux_eLODqg_ln6n9z9CvfQaILOYXRe5Y3qy_ojjpNYl7-lNL8lhtDJ_5A-JR3ySCJEmuTyBfdTxicGJX1dcw")

headers = {
    "Content-Type": "text/plain", 
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJkNDY4MmZjLWJmNGQtNDY5ZC04NDhlLWU2NTE3NjhmMjlkNiIsImlhdCI6MTcwMzE4NTExNSwic3ViIjoiZGV2ZWxvcGVyLzhkZWI0YWEwLWU5YjgtYzM4Mi01MmZjLWQ3NTIxM2MyODI1MSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyMjMuMjMzLjgwLjE3MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.9w7Ux_eLODqg_ln6n9z9CvfQaILOYXRe5Y3qy_ojjpNYl7-lNL8lhtDJ_5A-JR3ySCJEmuTyBfdTxicGJX1dcw"
}

player_tag = input("Please enter the player tag: ") #208J8JPLV --MegaNyte (example)

player = token.get_player(f'#{player_tag}')

def player_info():
    player_url = f'https://api.clashroyale.com/v1/players/%23{player_tag}/'
    player_json = requests.get(player_url, headers=headers).json()
    player_name = player_json['name']
    player_wins = player_json['wins']
    player_3_crownwins = player_json["threeCrownWins"]
    player_clan = player_json['clan']
    print(f"Player's name: {player_name}")
    print(f"Wins: {player_wins}")
    print(f"3 Crown wins: {player_3_crownwins}")
    print(f"Player's clan: {player_clan['name']}")
    print(f"Player's clan role: {player_json['role']}")


def chest():
    chest_url = f"https://api.clashroyale.com/v1/players/%23{player_tag}/upcomingchests"
    chest_json = requests.get(chest_url, headers=headers).json()
    # print(json.dumps(chest_json, indent=2))

    chest_json_items = chest_json["items"]
    chest_list = list(chest_json_items[0:])

    print(chest_list)

    chestNumber = []
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
