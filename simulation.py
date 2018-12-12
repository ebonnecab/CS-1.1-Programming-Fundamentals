import random
import sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation():
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        self.logger = Logger("interactions.txt")
        self.population = self._create_population()
        self.pop_size = pop_size  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.newly_infected = []

    def _create_population(self):
        population = []
        id = 0
        while len(population) != self.pop_size:
            person = Person(id, True)
            population.append(person)
            id += 1
        self.set_infected()
        return population

    def set_infected(self):
        infected = random.sample(self.population, self.initial_infected)
        for sick_people in infected:
            sick_people.infection = self.virus

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
            if person.did_survive_infection():
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
