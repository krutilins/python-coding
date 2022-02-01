from typing import List


travel_log = []

def add_to_travel_log(country: str, times: int, cities: List[str]):
  travel_log.append({
    "country": country,
    "times": times,
    "cities": cities,
  })

add_to_travel_log("Belarus", 1, ["Vitebsk", "Polotsk", "Novopolotsk", "Minsk", "Beshenkovichi"])
add_to_travel_log("Belarus", 1, ["Vitebsk", "Polotsk", "Novopolotsk", "Minsk", "Beshenkovichi"])
add_to_travel_log("Belarus", 1, ["Vitebsk", "Polotsk", "Novopolotsk", "Minsk", "Beshenkovichi"])
add_to_travel_log("Belarus", 1, ["Vitebsk", "Polotsk", "Novopolotsk", "Minsk", "Beshenkovichi"])
add_to_travel_log("Belarus", 1, ["Vitebsk", "Polotsk", "Novopolotsk", "Minsk", "Beshenkovichi"])

for log in travel_log:
  print(log)