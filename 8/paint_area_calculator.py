from math import ceil

def calculate_area(width, height):
  return width * height

def calculate_cans(area, coverage):
  return ceil(area / coverage)

wall_height = int(input("Height of wall: "))
wall_width = int(input("Width of wall: "))
COVERAGE = 5

print(f"You need {calculate_cans(calculate_area(height = wall_height, width = wall_width), coverage = COVERAGE)} cans")