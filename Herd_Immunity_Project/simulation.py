import random
import sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''

    def __init__(self, pop_size, vacc_percentage, initial_infected=1, virus=None):
        self.logger = Logger("interactions.txt")
        self.population = []  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0
        self.virus = virus
        self.initial_infected = initial_infected  # Int
        # FIXME: Use the variables below
        self.total_infected = 0
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.newly_infected = []

    def _create_population(self):
        is_vacc_options = [True, False]
        start = 0
        first_id = 0
        while start <= self.pop_size:
            person = Person(first_id, random.choice(is_vacc_options))
            self.population.append(person)
            start += 1
            first_id += 1
        self.set_infected()
        print (self.population)

    def set_infected(self):
        infected = random.sample(self.population, self.initial_infected)
        for sick_people in infected:
            sick_people.infection = self.virus

    def _simulation_should_continue(self):
        while self.pop_size > 0 or not self.vacc_percentage == 1:
            return True
        else:
            return False

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = None

        while should_continue:
            # TODO: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation.
            # print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))
            pass

    def choose_infected(self):
        return random.choice(self.newly_infected)

    # Test later today in an index.py file
    def time_step(self):
        total_interactions = 0
        # calling get_random_person method to randomly choose person from total population
        rand_person = random.choice(self.population)
        # looping through population to find infected person
        for person in self.population:
            if person.infection == virus:
                # creates loop for sick person to interact with 100 randos
                while total_interactions <= 100:
                    # checking if rando is alive and calling interaction method
                    if rand_person.is_alive:
                        self.interaction(person, rand_person)
                        total_interactions += 1
                    else:
                        # if they're dead the method starts over
                        self.time_step()

    def append_newly_infected(self, random_person):
        if random_person.is_vaccinated() == False:
            num = random.randint(0, 1)
            if num < self.virus.repro_rate:
                self.newly_infected.append(random_person._id)
                random_person.infection = virus

    def interaction(self, person, random_person):
        # Assert statements are to check if
        assert person.is_alive == True
        assert random_person.is_alive == True
        if person.infection == virus and random_person.infection == virus:
            self.logger.log_interaction(person, random_person)
            self.check_dead(random_person)
        elif person.infection == virus and random_person.is_vaccinated == True:
            self.logger.log_interaction(person, random_person)
            self.check_dead(random_person)
        elif person.infection == virus and random_person.is_vaccinated == False:
            self.logger.log_interaction(person, random_person)
            self.check_dead(random_person)
        else:
            pass

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            self.total_infected += 1
            person.infection = self.virus
        self.newly_infected = list()

    def check_dead(self, rand_person):
        if not rand_person.is_alive:
            self.total_dead += 1
        else:
            pass


if __name__ == "__main__":
    pop_size = 150
    vacc_percentage = 0.3
    virus = Virus("Ebola", 0.2, 0.4)
    initial_infected = 3
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)
    sim._create_population()
    sim.set_infected()

    # params = sys.argv[1:]
    # virus_name = str(params[0])
    # repro_num = float(params[1])
    # mortality_rate = float(params[2])

    # pop_size = int(params[3])
    # vacc_percentage = float(params[4])

    # if len(params) == 6:
    #     initial_infected = int(params[5])

    # virus = Virus(virus_name, repro_num, mortality_rate)
    # sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
