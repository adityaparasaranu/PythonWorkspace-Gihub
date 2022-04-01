import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
final_name = ""
greatest_matching_numbers = 0

for player_dict in players:
   name = player_dict.get('name')
   number_set = player_dict.get('numbers')
   intersected_numbers = lottery_numbers.intersection(number_set)
   if len(intersected_numbers) > greatest_matching_numbers:
       greatest_matching_numbers = len(intersected_numbers)
       final_name = name
       final_number_set = number_set
       final_intersected_numbers = intersected_numbers

print(f"The winner is {final_name} and won by {100 * len(final_intersected_numbers)}")
