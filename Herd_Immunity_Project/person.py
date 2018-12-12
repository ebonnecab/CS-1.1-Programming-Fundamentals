import random
# import pytest
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_alive = True
        self.is_vaccinated = is_vaccinated
        self.infection = infection

    def did_survive_infection(self):
        random_num = random.randint(0, 1)
        if (random_num < self.infection.mortality_rate):
            return False
        else:
            self.is_vaccinated = True
            return True


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''


def test_vacc_person_instantiation():
    person = Person(1, True, None)
    assert person._id == 1
    assert person.is_alive == True
    assert person.is_vaccinated == True
    assert person.infection == None


def test_not_vacc_person_instantiation():
    person = Person(1, False)
    # TODO: complete your own assert statements that test
    assert person._id == 1
    assert person.is_vaccinated == False
    assert person.is_alive == True


def test_sick_person_instantiation():
    # the values at each attributes
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(1, False, virus)
    assert person._id == 1
    assert person.is_vaccinated == False
    assert person.infection == virus
