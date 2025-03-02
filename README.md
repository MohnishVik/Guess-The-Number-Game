
Overview

The "Guess the Number Game" is a web-based interactive game where players attempt to guess a randomly selected number within a specified range. The game provides instant feedback and keeps track of the number of attempts taken. It is built using Python and Streamlit, making it accessible through a simple web interface.

Features

Random number generation for each session.

User-friendly interface with real-time feedback.

Tracks the number of attempts taken to guess correctly.

Option to restart the game after completion.

Technologies Used

Python: Core programming language for the game logic.

Streamlit: Web framework to create an interactive user interface.

Random Module: Used for generating random numbers.

How to Run the Project

1. Install Dependencies

Ensure you have Python installed. Then, install the required library:

pip install streamlit

2. Run the Application

Navigate to the project directory and execute the following command:

streamlit run main.py

Game Instructions

The system selects a random number between 1 and 100.

The player enters a guess in the input field.

The game provides feedback:

"Too low! Try again." if the guess is smaller than the target.

"Too high! Try again." if the guess is larger than the target.

"Congratulations!" message when the correct number is guessed.

The number of attempts is displayed.

A "Play Again" button resets the game with a new random number.

Project Files

main.py – Main script for the game.

Conclusion

This project demonstrates how Python and Streamlit can be used to create an engaging and interactive number guessing game. It is an excellent example of how basic programming logic and web-based interactivity can be combined to develop a fun application.
