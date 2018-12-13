<<<<<<< HEAD
# CS 1.1 Programming fundamentals

## Course Description

This course covers the foundations of software development and programming fundamentals including variables, naming, data types, control flow, loops, lists/arrays, dictionaries, functions, parameters and arguments, classes, objects, and object-oriented programming (OOP) concepts including inheritance, polymorphism, and instance method overriding. Build projects that take user input, manipulate strings, use libraries, make requests to web servers, and parse JSON data. Master top-level concepts in the landscape of software development including writing pseudocode, technical project planning, programming language paradigms, common software architectures, web development patterns and frameworks.

### Why you should know this

This course is designed to equip students with the technical skills and foundational knowledge necessary
to succeed at Make School. A strong foundation in CS concepts is the foundation for learning in any other course.  

## Course Specifics

Weeks to Completion:  7 <br>
Total Seat Hours:  37.5 hours <br>
Total Out-of-Class Hours: 75 hours <br>
Total Hours: 112.5 hours <br>
Units:  3 units <br>
Delivery Method:  Residential <br>
Class Sessions:  14 classes, 7 labs

## Prerequisites:  
None.

## Learning Objectives or Competencies

Students by the end of the course will be able to ...

1. Understand how to break down a problem into a programable algorithm.
1. Translate user stories and requirements into a program.
1. Master core programming concepts including data structures, control flow, repetition, functions, and object oriented programming.
1. Implement core programming concepts in Python.
1. Implement programming best practices, debugging, and testing in Python.


## Tutorials & Projects

Tutorials
- [Captain Rainbow's Color Checklist](https://www.makeschool.com/academy/track/captain-rainbow-s-color-checklist) or [GitHub Version of Captain Rainbow's Color Checklist](https://github.com/MakeSchool-Tutorials/Rainbow-Checklist)
- [MadLibs](Madlibs_Project/README.md)
- [Spaceman](Spaceman_Project/README.md)
- [Super Hero Team Dueler](http://make.sc/superhero-team-dueler)
- [Herd_Immunity]()

## Evaluation

To pass this course you must meet the following requirements:

- No more than two no call no shows
- No more than four excused absences
- Make up all classwork from all absences
- Finish all required tutorials and projects
- Pass the final exam (summative assessment) >=80%

## Lessons

1. [Class Introduction & Programming Basics](01. Class Intro)
    - **Before Class**
        - Prep Work
    - **In Class Activities**
        - Introductions
        - Pseudocode & Program Structure
        - Atom bits
    - **After Class**
        - Python tutorials
        - Atom Tutorials
        - Captain Rainbow's Color Selector
1. [Control Flow and Basic Data Structures](02. Control Flow)
    - **In Class Activities**
        - Discuss Captain Rainbow's Color Selector
        - Strings, Lists and Functions
        - Control Flow
        - Design Madlibs
    - **After Class**
        - MadLibs  
1. **  No class Mon. Sept 3 (Labor Day) **
1. Data Structures
    - **In Class Activities**
        - Design Spaceman
    - **After Class**
        - Spaceman
1. Object Oriented Programming
    - **In Class Activities**
    - **After Class**
        - Super Hero OOP Project
1. Object Oriented Programming
    - **In Class Activities**
    - **After Class**

** ... More to come ... **

## Resources
1. Python
    - [Python Documentation](https://docs.python.org/3/index.html)
        - [Tutorial in Python Documentation](https://docs.python.org/3/tutorial/index.html)
    - [Python Tutorial](https://learnpythonthehardway.org/python3/)
1. Atom Tutorials
1. CS fundamentals
    - [Project Euler](https://projecteuler.net/)

## Make School Course Policies

[Academic Honesty](https://github.com/Product-College-Courses/Common-Syllabus-Sections/blob/master/Academic-Honesty-and-Plagiarism.md)<br>
[Accommodation Policy](https://github.com/Product-College-Courses/Common-Syllabus-Sections/blob/master/Accommodation-Policy.md)<br>
[Diversity Statement](https://github.com/Product-College-Courses/Common-Syllabus-Sections/blob/master/Diversity-Statement.md)<br>
[Evaluation Methods](https://github.com/Product-College-Courses/Common-Syllabus-Sections/blob/master/Evaluation-Methods.md)
<br>
[Title IX Disclaimer](https://github.com/Product-College-Courses/Common-Syllabus-Sections/blob/master/Evaluations-Title-X-Disclaimer.md)<br>
[Program Learning Outcomes](https://github.com/Product-College-Courses/Common-Syllabus-Sections/blob/master/Program-Learning-Outcomes.md)
=======
## Final Project: Herd Immunity Simulation

We're going to create a basic simulation of herd immunity by modeling how a virus moves through a population where some (but not all) of a population is vaccinated against this virus.

### Goals

* Finish the code in these files to create a working simulation that creates log files of major events.  
* Design your program to follow the rules of the simulation.å  
* During every time step of the simulation, **every sick person** should randomly interact with **100 other people** in the population. The chance of a sick person infecting a person that they interact with is the virus's reproductive rate.  Example: if a virus has a reproductive rate of 15, then, on average, a sick person should infect 15 of the 100 people they interact with during that time step.

#### Rules
1. A sick person only has a chance at infecting healthy, unvaccinated people they encounter.  
1. An infected person cannot infect a vaccinated person.  This still counts as an interaction.  
1. An infected person cannot infect someone that is already infected.  This still counts as an interaction.
1. At the end of a time step, an infected person will either die of the infection or get better.  The chance they will die is the percentage chance stored in mortality_rate.  
1. For simplicity's sake, if the person does not die, we will consider them immune to the virus and change is_vaccinated to True when this happens.  
1. Dead people can no longer be infected, either.  Any time an individual dies, we should also change their .infected attribute to False.  
1. All state changes for a person should occur at the **end** of a time step, after all infected persons have finished all of their interactions.  
1. During the interactions, make note of any new individuals infected on this turn.  After the interactions are over, we will change the .infected attribute of all newly infected individuals to True.  1. Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.  
1. The simulation should output a logfile that contains a record of every interaction that occurred during the simulation.  We will use this logfile to determine final statistics and answer questions about the simulation.

#### Answer These Questions
Once you have successfully run a simulation, use your python skills to answer to analyze the simulation results
1. What were the inputs you gave the simulation? (Population size, percent vaccinated, virus name, mortality rate,  reproductive rate)
1. What percentage of the population became infected at some point before the virus burned out?
1.  What percentage of the population died from the virus?
1.  Out of all interactions sick individuals had during the entire simulation, how many total interactions did we see where a vaccination saved a person from potentially becoming infected?
<br>
<br>
*When you have answered these questions, please put your answers in a file called 'answers.txt' and commit this to your repo.*


### Running the program

The program is designed to be run from the command line.  You can do this by running
`python3 simulation.py` followed by the command line arguments in the following order,
separated by spaces:
 {population size} {vacc_percentage} {virus_name} {mortality_rate} {repro_rate} {optional: number of people initially infected (default is 1)}

 Let's look at an example:
 * Population Size: 100,000
 * Vaccination Percentage: 90%
 * Virus Name: Ebola
 * Mortality Rate: 70%
 * Reproduction Rate: 25%
 * People Initially Infected: 10

 Then I would type: <br>
 `python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10` in the terminal.

### Basic Structure
 s

When you run `simulation.py` with the corresponding command-line arguments necessary for a simulation, a simulation object is created.  This simulation object then calls the `.run()` method.  This method should continually check if the simulation needs to run another step using a helper method contained in the class, and then call `.time_step()` if the simulation has not ended yet.  Within the `time_step()` method, you'll find all the logic necessary for actually simulating everything--that is, once you write it.  As is, the file just contains a bunch of method stubs, as well as numerous comments for explaining what you need to do to get everything working.  

*Found a bug or a problem? Contact Alan, Justin, and Phyllis!*

The template code was written in a cottage on the coast of Ireland with spotty power during the strongest hurricane Ireland has seen in 61 years, so... **there are probably some bugs in the template code**. If you think something doesn't make sense, double check with your classmates and/or the instructor.  If you feel the need to modify the template code to make it work another way, that's totally fine! The template code is there to help you, but it isn't a requirement that you use all of it.

**WRITE TESTS!**

This is a big project.  There's no way that all the code you write is going to work the first time.  Also, see the paragraph above about all of this being coded by a man on a mountain during a 61-year storm while fighting off mountain lions with only a soup-ladle to defend himself.  Starting by thinking about your test cases and aiming for good test coverage is a great way to vaccinate yourself against any pre-existing bugs in the template. Not sure how to write tests? Look at the tests for the Super Hero project and utilize some strategies from those tests.

### Project Completion

For this project to be considered complete, you need to add your repo link to the course tracker. Please do not change the random seed set in the Simulation class! It is currently set to 42, and we will use this to double check that your simulation works and spits out the expected results.

**Your repo should contain:**
  * Completed classes for `logger.py`, `simulation.py`, and `person.py`.
  * At least 1 log file generated from running your simulation. 
  * `simulation_test.py` file should be created that allows for testing the simulation.
  * Answers to the questions asked above listed in a file named `answers.txt`.

>>>>>>> 88a25e53a81d2df2595944ec9cbc6f7991d0aa29
