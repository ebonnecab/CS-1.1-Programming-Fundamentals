#!/usr/bin/env python
import pytest


class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("MRSA", 0.2, 0.2)
    assert virus.name == "MRSA"
    assert virus.repro_rate == 0.2
    assert virus.mortality_rate == 0.2


def test_virus_instantiation():
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("Death", 0.5, 1)
    assert virus.name == "Death"
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 1


def test_virus_instantiation():
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("Tile", 0.6, 0.8)
    assert virus.name == "Tile"
    assert virus.repro_rate == 0.6
    assert virus.mortality_rate == 0.8
