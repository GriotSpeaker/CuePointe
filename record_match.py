import json

# 1. Load the data
with open('players.json', 'r') as f:
    data = json.load(f)

# 2. Show the players so you can pick
print("--- CuePointe Players ---")
for p in data['players']:
    print(f"ID: {p['id']} | Name: {p['name']}")

# 3. Get match results
winner_id = int(input("\nEnter the ID of the Winner: "))
loser_id = int(input("Enter the ID of the Loser: "))

# 4. Update the records
for p in data['players']:
    if p['id'] == winner_id:
        p['wins'] += 1
        p['matches_played'] += 1
        p['rating'] += 20  # Winner gains points
    if p['id'] == loser_id:
        p['matches_played'] += 1
        p['rating'] -= 10  # Loser loses some points

# 5. Save back to the vault
with open('players.json', 'w') as f:
    json.dump(data, f, indent=4)

print("\nMatch Recorded! Rankings updated.")