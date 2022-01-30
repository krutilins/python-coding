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


world_width = int(input("Type width of your world. It should be at least three: "))
world_height = int(input("Type hight of your world. It should be at least two: "))

if world_width >= 3 and world_height >= 2:
  new_world = World(world_width, world_height)
  new_world.show()
else:
  print("Length should be at least three")

print("The end!")