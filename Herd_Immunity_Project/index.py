def log_interaction(self, person, random_person, random_person_sick=None,
                    random_person_vacc=None, did_infect=None):
                    if person.infection == Virus and random_person.infection == Virus:
                      with open(self.file_name, "a") as file:
                        file.writelines(
                            ["{} didn't infect {} because they both are already sick"])

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
