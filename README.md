# Overthrowing the dictator: a game-theoretic approach

Introduction:
In today's world there are two types of major communication technologies, one being mass media and other is social media. We model this as a game where players are a dictator and people. People have choice of supporting the dictator or not. If majority of the people do not support the dictator then the dictator is overthrown by the people. In this game, we analyze the coordination failure among the people to overthrow the dictator. This project is a simulation on effect of communication technology influence to overthrow a dictator.   

The Game:
Players
 - Finite set of individuals, N = {1,2,….,n}, and a dictator
Strategies
 - Each individual chooses an action ai ∈ {r,s}, r-> revolt, s->stays at home
Type
 - Each individual is either of type τi = w (willing to revolt) or τi = x (unwilling)
 - W is the number of individuals who are willing to revolt
   #{i: τi = w} = W, W ∈ (0,n)
Individuals decide in a sequence.
 - Type vector τ = (τ1 , τ2, .....,τn)

Simulation:
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
