# Coordination Game

Introduction:

In today's world there are two types of major communication technologies, one being mass media and other is social media.In this project, I analyze how coordination can help revoluition a community.I model this as a game where there are multiple players, one being the dictator and other his people. People have choice of supporting the dictator or not. If majority of the people do not support the dictator then the dictator is overthrown by the people. We call this game "Overthrowing the Dictator". Here, we analyze the coordination among the people that helps to overthrow the dictator. 

Please see "Overthrowing the dictator.pdf" in the root directory for more information on the game and its game theoretic appraoch.

Please see "report.pdf" in root directory for a more detailed anlaysis on the game using the simulation.

Simulation:
This github repository simulates the game. To use the simulation use "revolution" API in revolution.py.

Steps for simulation:
(1) Initialize below parameters by creating "revolution" class object:
    Total number of players
    Percentage of players needed for the revolt to succeed,
    Percentage of players willing to revolt

(2) (Optional)Functions below are used to modify certain parameters:
- set_force_revolution_possibility
- set_frequency_deviation

(3) Sample:
r = revolution(1000,49,50)
r.set_frequency_deviation(5)
r.run()

