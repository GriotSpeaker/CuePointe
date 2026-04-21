import json
from datetime import datetime

# 1. Load the existing players
with open('players.json', 'r') as f:
    data = json.load(f)

# 2. Get user input for the new player
new_name = input("Enter the new player's name: ")

# 3. Create the new player record
new_player = {
    "id": len(data['players']) + 1,
    "name": new_name,
    "matches_played": 0,
    "wins": 0,
    "rating": 1200  # Standard starting rating
}

# 4. Add to our list and update the date
data['players'].append(new_player)
data['last_updated'] = datetime.now().strftime("%Y-%m-%d")

# 5. Save it back to the vault
with open('players.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Successfully added {new_name} to CuePointe Central!")