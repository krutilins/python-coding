import random

NOT_WALL = 0
WALL = 1
ADVENTURER = 2
GOAL = 3

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
  def print_world(matrix):
    print(matrix)
    for row in matrix:
      row_string = ""
      for item in row:
        row_string += str(item)
      print(f"{row_string}")  

  def generate_ground_with_walls(length):
    new_ground = []
    for i in range(length):
      if random_boolean():
        new_ground[i] = WALL
      else:
        new_ground[i] = NOT_WALL
    return(new_ground)

  def generate_sky(length):
    sky_path = []
    for i in range(length):
      sky_path.append(NOT_WALL)
    return(sky_path)

  def __init__(self,width,height):
    return([
      self.generate_sky(height - 1), 
      self.generate_ground_with_walls(width)
    ])

def random_boolean():
  return(bool(random.getrandbits(1)))

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
  place_adventurer_and_goal(new_world)


else:
  print("Length should be at least three")

print("The end!")