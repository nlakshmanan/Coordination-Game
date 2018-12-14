# revolution_game

revolution.py simulates the game

Set:
Total number of players
Percentage of players needed for the revolt to succeed,
Percentage of players willing to revolt

by creating revolution class object

Functions below can be uded to modify certain parameters:
- set_force_revolution_possibility
- set_frequency_deviation

Sample:
r = revolution(1000,49,50)
r.set_frequency_deviation(5)
r.run()
