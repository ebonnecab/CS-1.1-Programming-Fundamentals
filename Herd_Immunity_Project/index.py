
def _simulation_should_continue(self):
    while self.pop_size > 0 or not self.vacc_percentage == 1:
        return True
    else:
        return False


def run(self):
    ''' This method should run the simulation until all requirements for ending
    the simulation are met.
    '''
    if _simulation_should_continue()
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
