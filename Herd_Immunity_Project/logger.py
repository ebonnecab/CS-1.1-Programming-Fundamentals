from virus import Virus
import pytest


class Logger:
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        data = ["=====================\nStats of the virus\nVirus name: {} \n".format(
            virus_name), "Population size: {} \n".format(pop_size), "Vaccination Percentage: {} \n".format(vacc_percentage), "Mortality Rate: {}\n".format(mortality_rate), "Basic reproduction number: {}\n=====================\n".format(basic_repro_num)]

        with open(self.file_name, "w") as file:
            file.writelines(data)
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        pass

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        pass

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.
        '''
        with open(self.file_name, "a") as file:
            if person.is_alive:
                file.writelines(
                    ["{} survived infection \n".format(person._id)])
                did_die_from_infection = False
            else:
                file.writelines(
                    ["{} died from infection \n".format(person._id)])
                did_die_from_infection = True

    def log_time_step(self, time_step_number):
        with open(self.file_name, "a") as file:
            file.writelines(["Time step number {} ended, beginning {} \n".format(
                time_step_number, time_step_number + 1)])


def test_write_metadata():
    logger = Logger("interactions.txt")
    logger.write_metadata(100000, 0.4, "Snapple", 0.2, 0.3)


def test_log_time_step():
    logger = Logger("interactions.txt")
    logger.log_time_step(10)


def test_log_infection_survival():
    from person import Person
    logger = Logger("interactions.txt")
    virus = Virus("Snapple", 0.2, 0.4)
    person = Person(1, True, virus)
