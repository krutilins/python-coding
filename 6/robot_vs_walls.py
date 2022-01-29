import random

NOT_WALL = 0
WALL = 1
ADVENTURER = 2
GOAL = 3

class Utils:
  def fillArrayBy(array, length, fill):
    for i in range(length):
      array[i] = fill
  def random_boolean():
    return(bool(random.getrandbits(1)))


class Adventurer:
  def jump(self):
    self.y += 1
  def move_forward(self):
    self.x += 1
  def climb_up(self):
    self.jump()
    self.move_forward()
  def __init__(self, x, y):
    self.x = x
    self.y = y

class World:
  def show(self):
    for row in self.matrix:
      row_string = ""
      for item in row:
        row_string += str(item)
      print(f"{row_string}")
  def __generate_walls(self):
    last_row_index = len(self.matrix) - 1
    last_row_length = len(self.matrix[last_row_index])
    for i in range(2, last_row_length - 1):
      if (Utils.random_boolean()):
        self.matrix[last_row_index][i] = WALL

  def __init__(self, width, height):
    self.matrix = [[0] * width for i in range(height)]
    self.__generate_walls()


def place_adventurer_and_goal(world):
  return(Adventurer(0, 0))

def can_adventurer_move_forward(world, x, y):
  if y == 0:
    return world[1][x + 1] == WALL
  else:
    return world[1][x + 1] == NOT_WALL

world_width = int(input("Type width of your world. It should be at least three: "))
world_hight = int(input("Type hight of your world. It should be at least two: "))

if world_width >= 3 and world_hight >= 2:
  new_world = World(world_width, world_hight)
  new_world.show()
else:
  print("Length should be at least three")

print("The end!")