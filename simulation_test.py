import pytest
from simulation import Simulation
from virus import Virus
from person import Person


def test_infect_newly_infected():
    simulation = Simulation(1000, 0.2, Virus("Snapple", 0.2, 0.4), 1)
    simulation.newly_infected = [
        Person(0, False), Person(1, False), Person(2, False)]
    simulation._infect_newly_infected()
