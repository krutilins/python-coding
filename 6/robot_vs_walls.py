import random

NOT_WALL = 0
WALL = 1
ADVENTURER = 2
GOAL = 3

def random_boolean():
  return(bool(random.getrandbits(1)))

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

def generate_world(world_length):
  return([
    generate_sky(world_length), 
    generate_ground_with_walls(world_length)
  ])

def place_adventurer_and_goal(world):
  world[0] = ADVENTURER
  world[len(world) - 1] = GOAL

def print_world(matrix):
  print(matrix)
  for row in matrix:
    row_string = ""
    for item in row:
      row_string += str(item)
    print(f"{row_string}")  

def climb_up(x, y):
  x += 1
  y += 1

def move_forward(x, y):
  x += 1

def jump(x, y):
  y += 1

def can_adventurer_move_forward(world, x, y):
  if y == 0:
    return world[1][x + 1] == WALL
  else:
    return world[1][x + 1] == NOT_WALL


length_of_path = int(input("Type length of your path. It should be at least three: "))

if length_of_path >= 3:
  new_world = generate_world(length_of_path)
  print_world(new_world)
  place_adventurer_and_goal(new_world)

  
  
else:
  print("Length should be at least three")

print("The end!")