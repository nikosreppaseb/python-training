# Python Training Scripts

This repository contains a collection of simple Python scripts created for learning and experimentation purposes. They cover fundamental Python concepts.

## Features

This project includes scripts demonstrating:

*   **Rock Paper Scissors Game:** A command-line game where the user plays against the computer (`rock_paper_scissors.py`). Includes unit tests (`rock_paper_scissors_test.py`).
*   **Basic Output:** Printing strings and variables to the console (`helloWorld.py`).
*   **Integer Data Type Exploration:** Examples of integer properties, type checking, and manipulation (`data_types_integers.py`).
*   **String Data Type Exploration:** Examples of string manipulation, methods, formatting, and properties (`data_types_strings.py`).
*   **Conditional Logic:** Basic `if/else` statements and ternary operators (`meaning.py`).
*   **User Input:** Reading input from the user via the command line (`user_input_training.py`).

## Technology Stack

*   **Language:** Python 3
*   **Libraries:** Standard Libraries (`random`, `unittest`, `io`, `math`)

## Prerequisites

*   Python 3 installed on your system.

## Installation

1.  Clone the repository (or download the scripts). If cloning the parent repository, navigate to this directory:
    ```bash
    # Example if cloning the parent repository
    git clone <repository_url>
    cd <path_to_repo>/python_training
    ```
    If you only have this directory, simply navigate into it.
2.  No external dependencies need to be installed beyond standard Python 3.

## Usage

Navigate to the `python_training` directory in your terminal and run any of the scripts using the Python interpreter:

```bash
python helloWorld.py
python data_types_integers.py
python data_types_strings.py
python meaning.py
python user_input_training.py
python rock_paper_scissors.py
```

For the `rock_paper_scissors.py` script, follow the prompts to enter your choice (rock, paper, or scissors).

## Testing

Unit tests are available for the Rock Paper Scissors game. To run the tests, navigate to the parent directory of `python_training` (e.g., `/home/nikosr556/projects` in this case) and run the following command:

```bash
python -m unittest python_training/rock_paper_scissors_test.py
```
Alternatively, from within the `python_training` directory:
```bash
python -m unittest rock_paper_scissors_test.py
```

## Configuration

No specific configuration is required to run these scripts.
