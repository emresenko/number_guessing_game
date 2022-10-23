import random

number = random.randint(0,100)

EASY_GAME = 10
HARD_GAME = 5

def player_guess():
  guess = int(input("Guess a number!"))
  return guess

def game():
  lives = 0
  game_level = input("Select difficulty: 'easy' or 'hard' or impossible \n").lower()
  if game_level == "easy":
    lives = EASY_GAME
  elif game_level == "hard":
    lives = HARD_GAME
  elif game_level == "impossible":
    return "Game Over"
  while lives != 0:
    guess = player_guess()
    if guess > number:
      lives -= 1 
      print("Too High")
    elif guess < number:
      lives -= 1
      print("Too Low")
    elif guess == number:
      return "You Win"
    print(f"{lives} lives left!") 
    
  return f"Game Over, Number was {number} :(" 

print(game())
    

  
  