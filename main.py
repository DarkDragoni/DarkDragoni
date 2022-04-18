from random import randint, shuffle
from functools import reduce 
import re

class BadUserInputError(Exception):
  def __str__(self):
    return 'Invalid input. Please try again.'

class IllegalMoveError(Exception):
  def __str__(self):
    return 'Illegal move. Please try again.'

class Domino:
  def __init(self):
    self.stock = [[i, j] for i in range(7) for j in range(i, 7)]
    self.doubles = self.stock[:-4:-2]
    self.snake = []
    self.snake_left_end = None
    self.snake_right_end = None
    self.snake_ends = None
    self.computer = []
    self.player = []

  #USER ENTRY
  def get_command(self):
    while True:
      command = input()
      if command == '':
        return self.get_ai_command()
      try:
        if re.match(r'^-?\d{,2}$', command) is None or abs(int(command)) > len(self.player):
          raise BadUserInputError
        command = int(command)
        if command > 0 and self.snake_right_end not in self.player[command - 1] or \
        command < 0 and self.snake_left_end not in self.player[abs(command) - 1]:
          raise IllegalMoveError
        return command
      except BadUserInputError as error:
        print(error)
      except IllegalMoveError as error:
        print(error)
  # AI MOVE COMPUTATION
  def get_ai_command(self):
    move_option = [opt for opt in self.computer if opt[0] in self.snake_ends or opt[1] in self.snake_ends]
    if move_options:
      move_choice = choice(move_options)
      command_right: int = self.computer.index(move_choice) + 1
      command_left: int = command_right * -1
      if all((self.snake_right_end in move_choice, self.snake_left_end in move_choice)):
        command = choice((command_right, command_left))
      elif self.snake_right_end in move_choice:
        command = command_right
      else:
        command = command_left
    else:
      command = 0
    return command

    
  # MOVE (USER, AI)
  def place_on_board(self, turn, command):
    who = self.computer if turn == 'computer' else self.player
    whi = self.flip_if_needed(who.pop(abs(command) - 1), command)
    self.snake.insert(len(self.snake) if command > 0 else 0, what)

  
  def flip_if_needed(self, what, command):
    if command > 0 and self.snake_right_end  != what[0] or \
    command < 0 and self.snake_right_end != what[1]:
      return [what[1]. what[0]]
    return what


  def pull_from_stock(self, turn):
    who = self.computer if turn == 'computer' else self.player
    who.append(self.stock.pop(randint(0, len(self.stock) - 1)))
  # /MOVE (USER, AI)


  # PRE-GAME
  def get_distributtion(self, each=7):
    while not any([double in self.stock[:each * 2] for double in self.doubles]):
      shuffle(self.stock)
    for double in self.doubles:
      if double in self.stock[:each * 2]:
        self.snake = [self.stock.pop(self.stock.index(double))]
        break
    self.computer, self.player = self.stock[:each - 1], self.stock[each - 1:each * 2 - 1]
    self.stock = self.stock[each * 2 - 1:]
    if randint(1, 2) == 2:
      self.player, self.computer = self.computer, self.player


  # IN-GAME