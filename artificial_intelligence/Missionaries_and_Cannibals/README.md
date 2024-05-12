# Missionaries and Cannibals Problem

## Representaion of the search space for the problem
e: (LM, LC, B-pos, RM, RC) : 5-tupleStat
Transition Model: (delta-M, delta-C) : 2-tuple
Actions: [(2, 0), (0, 1), (1, 0), (0, 2), (1, 1)] , so the cap. of the boat is only two
Configurations:
			- initial # of Ms and Cs
			- Parent Node

## How to Run
`python main.py`
**Note: written in __Python 3.12.1__**