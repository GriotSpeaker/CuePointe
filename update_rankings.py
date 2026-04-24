import json
import os

def update_players():
    file_path = 'players.json'
    
    # Ensure the file exists and has a valid list
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                players = json.load(f)
            except json.JSONDecodeError:
                players = []
    else:
        players = []

    print("--- CuePointe Player Update ---")
    name = input("Player Name: ")
    points = float(input("Total Points: "))
    played = int(input("Matches Played: "))

    new_player = {
        "name": name,
        "points": points,
        "played": played
    }

    players.append(new_player)

    with open(file_path, 'w') as f:
        json.dump(players, f, indent=4)
    
    print(f"Successfully added {name}!")

if __name__ == "__main__":
    update_players() 