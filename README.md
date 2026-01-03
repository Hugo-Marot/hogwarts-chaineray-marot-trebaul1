1. General Presentation

Project Title
Hogwarts Adventure

Brief Description
Hogwarts Adventure is a text-based adventure game developed in Python as part of the TI101 – Programming in Python course. The game is inspired by the Harry Potter universe and takes place at Hogwarts School of Witchcraft and Wizardry. The player progresses through several chapters and interacts with the game by making choices in the terminal. During the adventure, the player creates a character, assigns attributes, is sorted into a Hogwarts house, learns spells, answers a magic quiz, and participates in a Quidditch match. The choices made by the player influence the character’s attributes and the number of points earned by their house.

Contributors
Yanis, Hugo

Installation

Instructions for cloning the Git repository
The project can be obtained by cloning the Git repository using the following command:

git clone <repository_url>


Development environment configuration
The project requires Python 3.x. No external libraries are needed, as only built-in Python modules are used. The program must be run with the original folder structure to ensure correct file loading.

Usage

How to run the application
To start the application, open a terminal in the project root directory and run:
main.py


Use cases
The game is fully played in the terminal. The player follows on-screen instructions, presses Enter to continue, and enters the number corresponding to their choice. If an invalid input is entered, the program displays an error message and asks the player to try again.

Key Features

Text-based interactive adventure

Character creation and attribute management

Hogwarts house sorting ceremony

Spell learning system

Magic quiz with randomized questions

Quidditch match simulation

House point management

Multi-chapter narrative progression

2. Logbook

Project Timeline
The project was developed over several weeks. During the first phase, the project structure was created and utility functions were implemented to handle user input and file loading. The second phase focused on the development of the first two chapters, including character creation, narrative progression, and the sorting ceremony. The third phase was dedicated to the implementation of spell learning and the magic quiz, as well as testing the previous chapters. The final phase focused on the Quidditch match simulation, bug fixing, and overall validation of the project.

Several decisions were made during development, such as enforcing consistent naming conventions for dictionary keys and avoiding the use of forbidden predefined functions. Some difficulties were encountered, mainly related to invalid user inputs and incorrect data structure usage. These problems were resolved through input validation and progressive testing.

Task Distribution
The work was divided between the two contributors. Yanis worked on the input utility functions, the house management system, the Quidditch chapter, and the documentation. Hugo worked on character management, the first three chapters of the game, and the main program structure including the menu system. All parts of the project were reviewed together.

3. Control, Testing, and Validation

Input and Error Management
The program includes input validation functions to ensure that user entries are correct. Text inputs are checked to prevent empty values. Numeric inputs are verified to ensure they are integers and fall within the required ranges. When an invalid input is detected, the program displays an error message and asks the user to enter a new value.

The code also handles file loading errors by ensuring that JSON files are correctly read before use. Consistent dictionary key naming was enforced to avoid runtime errors.

Known Bugs
No major bugs remain at the time of submission. Minor issues may occur if the project folder structure is modified or if required data files are missing.

Testing Strategies
Each chapter was tested independently to simplify debugging. Tests were performed using both valid and invalid inputs, such as empty inputs, incorrect data types, and invalid choices. These tests confirmed that the program does not crash and correctly asks the user to try again when an error occurs.

The Quidditch match was tested multiple times to verify random events such as goals and the appearance of the Golden Snitch. Manual tests were also performed to ensure that house points are correctly updated and displayed.