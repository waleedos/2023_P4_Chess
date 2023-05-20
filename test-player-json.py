# Create a new player
original_player = Player("Test Player", "01/01/1980", "Male", 1000)

# Convert the player to JSON
player_json = original_player.to_json()

# Recreate the player from the JSON
recreated_player = Player.from_json(player_json)

# Check if the original and recreated player are the same
print(original_player == recreated_player)  # Should print: True
