# Python Password Generator

## Overview

This is a simple password generator I developed as a beginner project while learning Python.

The program supports two generation modes and branches based on user input.

## Features

### Word Based Passwords

If the user selects word mode, the program generates a password using a dictionary of approximately 3,000 words. Four random words are selected and combined into a single passphrase.

Example:
rivercoffeelanterntiger

### Character Based Passwords

If the user selects character mode, the program generates a password based on user defined parameters such as:

* Password length
* Uppercase letters
* Numbers
* Symbols

Example:
K7f@2c9a

The program uses Python’s `secrets` module to generate cryptographically secure random values.

## What I Learned

This project helped me practice:

* Writing and organizing Python functions
* Reading data from files
* Secure random number generation
* Structuring a small program across multiple modules
* Building a simple command line tool

It also reinforced an important concept: computers cannot generate truly random numbers because their operations are deterministic. However, Python’s `secrets` module provides cryptographically secure randomness suitable for tasks like password generation.

## Project Structure

PasswordGenerator/

* main.py
* generation.py
* prompt.py
* dictionary.txt
* README.md

## How to Run

1. Navigate to the project directory.

2. Run the program:

python3 main.py

3. Follow the prompts to generate either a word based passphrase or a character based password.

## Requirements

* Python 3.x
* No external libraries required

## Future Improvements

Possible future improvements include:

* Expanding the word dictionary
* Allowing optional separators for word passwords
* Adding password strength indicators
* Supporting additional password generation modes
