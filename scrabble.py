# Initial lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# 1. Combining the two lists with list comprehension
letters_to_points = letter_to_points = {key: value for key, value in zip(letters, points)}

# 2. Adding an element to letters_to_points that has a key of " " and a point value of 0
letters_to_points[" "] = 0

# Score a Word

# 3. Defining a function called score_word with a parameter word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.pop(letter, 0)
  return(point_total)

# 4. Testing the function
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Score a game

# 5. Creating a dictionary
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"], 
  "wordNerd": ["EARTH, EYES, MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# 6. Creating an empty dictionary
player_to_points = {}

# 7. Iterating through each items
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)
