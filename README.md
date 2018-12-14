# revolution_game

revolution.py simulates the game

Initialize below parameters by creating revolution class object:
Total number of players
Percentage of players needed for the revolt to succeed,
Percentage of players willing to revolt

Functions below are used to modify certain parameters:
- set_force_revolution_possibility
- set_frequency_deviation

Sample:
r = revolution(1000,49,50)
r.set_frequency_deviation(5)
r.run()
