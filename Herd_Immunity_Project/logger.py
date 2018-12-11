import csv
from virus import Virus
# from person import Person
# from simulation import Simulation

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
        data = ["Virus name: {} \t".format(
            virus_name), "Population size: {} \t".format(pop_size), "Vaccination Percentage: {} \t".format(vacc_percentage), "Mortality Rate: {}\t".format(mortality_rate), "Basic reproduction number: {}\t \n".format(basic_repro_num)]

        with open(self.file_name, "w") as file:
            file.writelines(data)

            # TODO: Finish this method. This line of metadata should be tab-delimited
            # it should create the text file that we will store all logs in.
            # TIP: Use 'w' mode when you open the file. For all other methods, use
            # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
            # NOTE: Make sure to end every line with a '/n' character to ensure that each
            # event logged ends up on a separate line!
            pass

    def log_interaction(self, person, random_person, random_sick_person=None,
                        random_vacc_person=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        '''sick_person
            vacc_person

        '''
        sick_person = person.infection == Virus
        random_sick_person = random_person.infection == Virus
        random_vacc_person = random_person.is_vaccinated

        with open(self.file_name, "a") as file:

            if sick_person and not random_vacc_person and did_infect == True:
                file.writelines(
                    ["{} infects {} \n because they are not vaccinated.".format(person._id, random_person._id)]
                )

            elif sick_person and not random_vacc_person and did_infect == False:
                file.writelines(
                    ["{} did not infect {} \n because of good fortune.".format(person._id, random_person._id)]
                )
            elif sick_person and random_vacc_person and did_infect == False:
                file.writelines(
                    ["{} did not infect {} \n they are vaccinated.".format(person._id, random_person._id)]
                )
            elif sick_person and random_sick_person and did_infect == False:
                file.writelines (
                    ["{} did not infect {} \n they are already sick.".format(person._id, random_person._id)]
                )
                
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        
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
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass


