import random
import sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1, ):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = Logger("interactions.txt")
        self.population = self._create_population(initial_infected)
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.newly_infected = []

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        pass

    def _simulation_should_continue(self):
        return len(self.population) == 0 or self.vacc_percentage == 1

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            self.logger.log_time_step(time_step_counter)
            time_step_counter += 1
        print('The simulation has ended after {time_step_counter} turns.'.format(
            time_step_counter))

    def time_step(self):

        healthy_people = []
        infected_people = []

        # Seperates the sick/healthy ppl
        for person in self.population:
            if person.infection:
                infected_people.append(person)
            else:
                healthy_people.append(person)

        # Every infected interacts with 100 random people
        for person in infected_people:
            for _ in range(100):
                self.interaction(person, random.choice(healthy_people))

        for person in infected_people:
            if person.did_survive_infection:
                self.logger.log_infection_survival(
                    person, did_die_from_infection=False)
            else:
                self.logger.log_infection_survival(
                    person, did_die_from_infection=True)

        just_died = 0
        self.total_dead += just_died
        self._infect_newly_infected()

    def interaction(self, person, random_person):
        '''
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        assert person.is_alive == True
        assert random_person.is_alive == True

        # Checking if the random person is healthy
        if random_person.is_vaccinated:
            self.logger.log_interaction(
                person, random_person, random_person_vacc=True, did_infect=False)

        # Already sick, can't get sick again!
        elif random_person.infection is self.virus or random_person._id in self.newly_infected:
            self.logger.log_interaction(
                person, random_person, random_person_sick=True)

        else:
            # This is when a healthy person can get sick
            if random.random() <= self.virus.repro_rate:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(
                    person, random_person, did_infect=True,)
            else:
                self.logger.log_interaction(
                    person, random_person, did_infect=False)

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.current_infected = len(self.newly_infected)
        self.total_infected += self.current_infected
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
